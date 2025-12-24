<div align="center">
  <h1>Dokumentasi dan Validasi Arsitektur Data</h1>
</div>
<div align="center">
  <h3><i>Transform Data, Unlock Insights, Drive Innovation</i></h3>
  <img src="https://img.shields.io/github/last-commit/RakhaRabbani/DataWrangling-AGREGASI_DAN_TRANSFORMASI_STRUKTURAL?style=flat-square&color=blue" alt="Last Commit">
  <img src="https://img.shields.io/github/languages/top/RakhaRabbani/DataWrangling-AGREGASI_DAN_TRANSFORMASI_STRUKTURAL?style=flat-square&color=blue" alt="Top Language">
  <img src="https://img.shields.io/github/languages/count/RakhaRabbani/DataWrangling-AGREGASI_DAN_TRANSFORMASI_STRUKTURAL?style=flat-square&color=blue" alt="Language Count">
  <br><br>
</div>

Repository ini berisi implementasi teknis dan dokumentasi teoretis mengenai **Data Lineage**, **Data Provenance**, dan **Praktik Terbaik Arsitektur Data** dalam konteks studi kasus transaksi E-Commerce.

---

## Teknologi yang Digunakan

* **Python 3.x**
* **Pandas** (Manipulasi data)
* **JSON** (Format metadata standar)
* **Datetime & Random** (Simulasi data)


---

## Dokumentasi Arsitektur Data

Sesuai dengan praktik terbaik pendokumentasian arsitektur data, berikut adalah rincian standar yang diterapkan dalam proyek ini:

### 1Dokumentasi Diagram Sistem
* **Source**: Aplikasi Mobile & Web E-Commerce.
* **Ingestion**: Apache Kafka (Message Broker).
* **Processing**: Apache Spark (ETL & Validation).
* **Storage**: Google BigQuery (Data Warehouse).
* **Output**: Tableau Dashboard (Analytics).

### Data Dictionary (Kamus Data)
[cite_start]Definisi atribut data yang digunakan dalam dataset transaksi

| Nama Kolom | Tipe Data | Deskripsi | Contoh |
| :--- | :--- | :--- | :--- |
| `transaction_id` | String | Identitas unik setiap transaksi | `TXN-10045` |
| `user_id` | String | ID unik pengguna terdaftar | `USER-881` |
| `amount` | Integer | Nilai nominal transaksi (IDR) | `450000` |
| `payment_method` | String | Metode pembayaran yang dipilih | `credit_card` |
| `status` | String | Status akhir transaksi | `success` |
| `timestamp` | Datetime | Waktu pencatatan (ISO 8601) | `2025-12-12T10:00:00` |

### Menyimpan Metadata
* **Owner**: Data Engineering Team.
* **Created By**: DE_Rabbani.
* **Timestamp**: Waktu terakhir ETL berjalan.
* **Version**: Versi skema dataset (misal: v1.2).

### Versioning Dokumentasi
* Setiap perubahan logika bisnis pada pipeline harus melalui *Commit* dan *Pull Request*.
* Dokumentasi historis disimpan dalam folder `/archive` di repository.

### Standardisasi Nama dan Format
* **Snake Case**: Digunakan untuk nama tabel dan kolom (contoh: `user_transactions`, `created_at`).
* **ISO 8601**: Format standar untuk tanggal dan waktu (`YYYY-MM-DDTHH:MM:SS`).

---

## Contoh Output JSON (Provenance)

Berikut adalah cuplikan metadata yang dihasilkan oleh script:

```json
{
    "dataset_info": {
        "dataset_name": "ecommerce_transaction_clean",
        "source_system": "Payment Gateway API v2",
        "owner": "Data Engineering Team",
        "created_by": "DE_Rakha",
        "version": "v1.2",
        "usage_policy": "Internal Analytics Only"
    },
    "lineage_history": [
        {
            "step": "Ingestion",
            "source": "PaymentGatewayAPI",
            "target": "df_raw",
            "transformation": "Generate/Load 1500 rows"
        },
        {
            "step": "Filtering",
            "source": "df_raw",
            "target": "df_clean",
            "transformation": "Filter status == success"
        }
    ]
}
