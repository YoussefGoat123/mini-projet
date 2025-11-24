from fastapi import FastAPI

# Import prometheus instrumentation only if available (allows running tests
# under older Python versions where the package may use newer typing features).
try:
    from prometheus_fastapi_instrumentator import Instrumentator
except Exception:
    Instrumentator = None


app = FastAPI(title="Mini API", version="0.1.0")

if Instrumentator is not None:
    Instrumentator().instrument(app).expose(app)
else:
    # Fallback: expose a basic /metrics endpoint using prometheus_client
    try:
        from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
        from fastapi.responses import Response

        @app.get("/metrics")
        def metrics():
            data = generate_latest()
            return Response(content=data, media_type=CONTENT_TYPE_LATEST)
    except Exception:
        # prometheus_client not available; /metrics stays absent
        pass

@app.get("/hello")
def hello():
    return {"message": "Hello world"}

@app.get("/")
def root():
    return {"message": "OK"}

