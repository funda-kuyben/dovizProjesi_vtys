import requests
import time
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WriteOptions

# -----------------------------
# Open Exchange Rates API URL (Anahtar gerektirir)
API_URL = "https://openexchangerates.org/api/latest.json?app_id=b1d8d4dca64840d2a1ec29b662d1a4ac"  # Buraya API anahtarınızı ekleyin

# -----------------------------
# InfluxDB bağlantı ayarları
bucket = "doviz"
org = "vtys"
token = "nds8NTLBpgQ4HvDEluOPkLcmUrTFOMmVhg1mqqc3jZaIWFgm-LgCjMaPsc6F5FufguASd__oyZa8cDHm5r7nAA=="
url = "http://localhost:8086"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=WriteOptions(batch_size=1))

# -----------------------------
# Her 1 dakikada bir veri çek ve InfluxDB'ye gönder
while True:
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # HTTP hatalarını kontrol et
        data = response.json()
        print("API Yanıtı:", data)
        
        rates = data.get("rates", {})
        if not rates:
            print("Hata: 'rates' verisi alınamadı.")
            time.sleep(60)
            continue

        now = datetime.utcnow()

        for currency, rate in rates.items():
            point = (
                Point("doviz_kuru")
                .tag("para_birimi", currency)
                .field("kur", float(rate))
                .time(now)
            )
            write_api.write(bucket=bucket, org=org, record=point)

        print(f"[{now}] Veriler InfluxDB’ye kaydedildi: {rates}")

    except Exception as e:
        print("Hata oluştu:", e)

    time.sleep(60)
