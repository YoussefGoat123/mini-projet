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
curl http://127.0.0.1:8000/metrics  # métriques Prometheus
```

## Monitoring & métriques (Prometheus)

Un endpoint `/metrics` est exposé via `prometheus-fastapi-instrumentator`.

### Lancer API + Prometheus avec docker-compose

```bash
docker compose up -d --build
```

Accès:
- API: http://localhost:8000/
- Metrics: http://localhost:8000/metrics
- Prometheus UI: http://localhost:9090/

## Visualisation (Grafana)

Setup volontairement minimal (aucun dashboard pré-provisionné) pour apprendre à créer les panels soi‑même.

Lancer toute la stack:
```bash
docker compose up -d --build
```

Accès:
- Grafana: http://localhost:3000/  (admin / admin)
- Prometheus: http://localhost:9090/

### Datasource Prometheus
Une datasource `Prometheus` devrait déjà exister (provisionnée) avec l’URL interne: `http://prometheus:9090`.
Si elle n’apparaît pas:
1. Connections > Data sources > Add data source
2. Choisir Prometheus
3. URL: `http://prometheus:9090`
4. Access: `Server (Proxy)` puis "Save & test" (doit être vert)

### Créer un premier dashboard
1. Dashboards > New > New dashboard > Add visualization
2. Sélectionner datasource `Prometheus`
3. Ajouter des panels , puis Save .

