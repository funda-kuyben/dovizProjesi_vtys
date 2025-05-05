# Döviz Kuru Takip ve Görselleştirme Projesi
Bu proje, döviz kuru verilerini InfluxDB'ye kaydedip, Grafana kullanarak görselleştirmeyi amaçlamaktadır. Döviz kuru verileri, Open Exchange Rates API'den alınarak her dakika güncellenir. Grafana ile, döviz kuru verileri zaman serisi grafikleri şeklinde görselleştirilmekte ve kullanıcıya interaktif bir panel sunulmaktadır.

## Teknolojiler ve Kullanılan Araçlar
Python 3.x: Döviz kuru verilerini almak ve veritabanına kaydetmek için kullanılmıştır.

InfluxDB 2.x: Verilerin zaman serisi şeklinde depolanmasını sağlar.

Grafana: Verilerin görselleştirilmesi için kullanılır.

Open Exchange Rates API: Döviz kuru verilerini almak için kullanılan API.

## Proje Yapısı
bash
Kopyala
dovizProjesi/
│
├── dovizProjesi.py       # Python scripti - Döviz kuru verilerini almak ve InfluxDB'ye kaydetmek
├── README.md             # Proje açıklaması ve kurulum talimatları
├── requirements.txt      # Gerekli Python kütüphanelerinin listesi
└── influxdb_data/        # InfluxDB veritabanı dosyaları (veri ve konfigürasyon)
## Kurulum Talimatları
### Gereksinimler
Projenin çalışabilmesi için aşağıdaki araçların yüklü olması gerekmektedir:

#### Python 3.x

#### InfluxDB 2.x

#### Grafana

## Gerekli Kütüphanelerin Yüklenmesi
Projenin çalışması için gerekli olan Python kütüphaneleri requirements.txt dosyasında belirtilmiştir. Aşağıdaki komutu kullanarak gerekli kütüphaneleri yükleyebilirsiniz:

bash
Kopyala
pip install -r requirements.txt
requirements.txt şu kütüphaneleri içermektedir:

nginx
Kopyala
requests
influxdb-client
## InfluxDB ve Grafana Kurulumu
### InfluxDB
1. InfluxDB’yi kurduktan sonra, influxd komutunu çalıştırarak InfluxDB’yi başlatın.

2. InfluxDB’ye bağlantı sağlayın ve veritabanınızı oluşturun.

### Grafana
1. Grafana'yı kurduktan sonra, Grafana’yı başlatın ve tarayıcınızda localhost:3000 adresine gidin.

2. Grafana'ya giriş yaptıktan sonra, Data Sources sekmesinden InfluxDB'yi veri kaynağı olarak ekleyin.

3. Grafana üzerinde görselleştirme yapmak için Dashboard oluşturun ve verileri sorgulayıp görselleştirin.

## Kullanım
Python scriptini çalıştırarak döviz kuru verilerini almak ve InfluxDB'ye kaydetmek için aşağıdaki komutu kullanın:

bash
Kopyala
python dovizProjesi.py
Grafana üzerinde verileri görselleştirmek için dashboard oluşturun ve InfluxDB veri kaynağını kullanarak döviz kuru verilerini sorgulayın.

## API Bilgileri
Open Exchange Rates API üzerinden döviz kuru verileri alınmaktadır. API anahtarınızı almak için buraya giderek kaydolabilirsiniz.

## Projenin Sağladığı Avantajlar
1. Zaman Serisi Analizi: Grafana ile zaman içinde döviz kuru değişimlerini görselleştirebilirsiniz. Bu sayede döviz kuru hareketlerini daha iyi analiz edebilirsiniz.

2. Gerçek Zamanlı Veri: Her dakika güncellenen veriler ile döviz kuru anlık olarak takip edilebilir.

3. İnteraktif Görselleştirme: Grafana’nın sunduğu güçlü görselleştirme araçları sayesinde veriler kolayca analiz edilebilir. Kullanıcılar, veriyi filtreleyebilir ve farklı zaman dilimlerini inceleyebilirler.

4. Kolay Erişim: Grafana’nın web tabanlı arayüzü sayesinde, kullanıcılar veriye herhangi bir cihazdan kolayca erişebilir.

5. Esnek Yapı: InfluxDB ve Grafana'nın esnek yapısı, gelecekteki projeler için de benzer verilerin görselleştirilmesine olanak tanır.

## Sonuç
Bu proje, döviz kuru verilerini sürekli güncel tutmak ve görselleştirmek isteyen kullanıcılar için kapsamlı bir çözüm sunmaktadır. Python, InfluxDB ve Grafana'nın gücüyle, verilerin yönetimi ve görselleştirilmesi oldukça basit ve etkili bir hale gelmiştir.
