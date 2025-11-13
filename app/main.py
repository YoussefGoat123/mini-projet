from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

# Instance FastAPI exposée sous le nom 'app' pour uvicorn (app.main:app)
app = FastAPI(title="Mini API", version="0.1.0")

# Instrumentation Prometheus: enregistre métriques et expose /metrics
Instrumentator().instrument(app).expose(app)

@app.get("/hello")
def health():
    return {"message": "Hello world"}

# Endpoint exemple simple
@app.get("/")
def root():
    return {"message": "OK"}