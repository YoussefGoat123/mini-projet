# Mini projet – API FastAPI

Cette app expose une API REST minimale en FastAPI.

## Endpoints
- GET `/` -> {"message":"OK"}
- GET `/hello` -> {"message":"Hello world"}

## Démarrer avec Docker

1) Construire l'image:
```bash
docker build -t mini-api:latest .
```

2) Lancer le conteneur:
```bash
docker run --rm -p 8000:8000 mini-api:latest
```

3) Tester:
```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/hello
```

## Démarrage local (optionnel, sans Docker)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Ouvrir: http://127.0.0.1:8000
