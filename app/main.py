from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Mini API", version="0.1.0")

Instrumentator().instrument(app).expose(app)

@app.get("/hello")
def hello():
    return {"message": "Hello world"}

@app.get("/")
def root():
    return {"message": "OK"}

