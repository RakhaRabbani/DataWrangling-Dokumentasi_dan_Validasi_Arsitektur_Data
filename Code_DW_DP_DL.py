import pandas as pd
import json
import random
from datetime import datetime, timedelta

#GENERATE DATA (>1000 baris)G
def generate_dummy_data(n=1500):
    data = []
    statuses = ['success', 'failed', 'pending', 'fraud_suspect']
    payment_methods = ['credit_card', 'ewallet', 'bank_transfer']
    
    for i in range(1, n + 1):
        tx_time = datetime.now() - timedelta(days=random.randint(0, 30))
        record = {
            "transaction_id": f"TXN-{10000+i}",
            "user_id": f"USER-{random.randint(100, 999)}",
            "amount": random.randint(10000, 5000000),
            "payment_method": random.choice(payment_methods),
            "status": random.choice(statuses),
            "timestamp": tx_time.isoformat()
        }
        data.append(record)
    return pd.DataFrame(data)

#DATA LINEAGE & PROVENANCE FUNCTION 
lineage_log = []

def log_lineage(step, source, target, transformation):
    """Mencatat setiap langkah perubahan data (Lineage)"""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "step": step,
        "source": source,
        "target": target,
        "transformation": transformation
    }
    lineage_log.append(entry)


#BAGIAN 3: EKSEKUSI PROSES 
#Load 
df_raw = generate_dummy_data(1500)
log_lineage("Ingestion", "PaymentGatewayAPI", "df_raw", "Generate/Load 1500 rows")

#Transformasi
df_clean = df_raw[df_raw['status'] == 'success'].copy()
log_lineage("Filtering", "df_raw", "df_clean", "Filter status == success")

#Konversi USD ke IDRT
df_clean['amount_usd'] = df_clean['amount'] / 15000
log_lineage("Transformation", "df_clean", "df_final", "Calculate USD amount")

#DATA PROVENANCE (JSON Metadata) 
data_provenance = {
    "dataset_info": {
        "dataset_name": "ecommerce_transaction_clean",
        "source_system": "Payment Gateway API v2",
        "owner": "Data Engineering Team",
        "created_by": "DE_Rakha",
        "creation_timestamp": datetime.now().isoformat(),
        "version": "v1.2",
        "total_records": len(df_clean),
        "usage_policy": "Internal Analytics Only"
    },
    "lineage_history": lineage_log
}

#HSIL
print("=== SAMPLE DATA (5 Baris Teratas) ===")
print(df_clean.head())
print("\n=== DATA PROVENANCE & LINEAGE (JSON) ===")
print(json.dumps(data_provenance, indent=4))