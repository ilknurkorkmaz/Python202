# Python 202 — Kütüphane Uygulaması (OOP + Open Library + FastAPI)

Bu repo, üç aşamalı olarak geliştirilen bir Python projesini içerir:
1) OOP ile terminal uygulaması
2) Open Library API ile ISBN'den kitap bilgisi çekme
3) FastAPI ile kendi API’nizi yayınlama

## Başlangıç

```bash
# Depoyu klonlayın
git clone <repo-url>
cd python202-library-api

# Sanal ortam (opsiyonel ama tavsiye edilir)
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# Bağımlılıkları yükleyin
pip install -r requirements.txt
```

### Aşama 1 ve 2 — Terminal Uygulaması

```bash
python main.py
```
- **Kitap Ekle** menüsü ISBN sorar ve Open Library'den başlık/yazarları çeker.
- Veriler `library.json` dosyasında **kalıcı**dır.

### Aşama 3 — FastAPI Sunucusu

```bash
uvicorn api:app --reload
```
- Tarayıcıdan **http://127.0.0.1:8000/docs** adresine gidip endpoint’leri deneyin.

### Testler

```bash
pytest -q
```

## Proje Yapısı

```
.
├── api.py               # FastAPI uygulaması
├── library.py           # Library sınıfı ve JSON depolama
├── main.py              # CLI menüsü
├── models.py            # Pydantic modelleri ve Book sınıfı
├── openlibrary.py       # Open Library istemcisi (httpx ile)
├── requirements.txt
├── tests/
│   ├── test_api.py
│   └── test_library.py
└── README.md
```

> Not: Bu proje, bootcamp dökümanındaki zorunlu maddeleri karşılaması için tasarlanmıştır: public GitHub repo, README, *.py dosyaları, httpx ile Open Library entegrasyonu, FastAPI endpoint’leri ve pytest testleri.
