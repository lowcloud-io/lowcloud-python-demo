# Python API Demo

Eine einfache FastAPI-basierte REST-API, die Dummy-Daten aus JSON-Dateien zurückgibt.

## Features

- **User-Endpunkte**: Liste und Details von Benutzern
- **Product-Endpunkte**: Liste und Details von Produkten
- **Order-Endpunkte**: Liste und Details von Bestellungen (verknüpfen User mit Products)

## Installation

```bash
pip install -r requirements.txt
```

## First time getting started

### 1. Prüfe Python-Version

python3 --version

### 2. Erstelle ein virtuelles Environment im Projektordner

cd /Users/fabiansander/dev/lowcloud-python-demo
python3 -m venv venv

### 3. Aktiviere das virtuelle Environment

source venv/bin/activate

### 4. Installiere die Pakete

pip install -r requirements.txt

### 5. Starte die API

uvicorn app.main:app --reload

## Starten der API

```bash
uvicorn app.main:app --reload
```

Die API läuft dann auf `http://localhost:8000`

## API-Dokumentation

Nach dem Starten der API ist die interaktive Dokumentation verfügbar unter:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpunkte

### Users

- `GET /users` - Liste aller Benutzer
- `GET /users/{id}` - Details eines Benutzers

### Products

- `GET /products` - Liste aller Produkte
- `GET /products/{id}` - Details eines Produkts

### Orders

- `GET /orders` - Liste aller Bestellungen
- `GET /orders/{id}` - Details einer Bestellung

## Projektstruktur

```
app/
├── main.py              # FastAPI-App Initialisierung
├── models/              # Pydantic Models
├── routers/             # API-Endpunkte
├── services/            # Business-Logik
└── repositories/        # Datenzugriff
data/                    # JSON-Daten-Dateien
```
