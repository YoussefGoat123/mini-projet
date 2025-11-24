from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "OK"}


def test_hello():
    r = client.get("/hello")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello world"}


def test_metrics():
    r = client.get("/metrics")
    assert r.status_code == 200
    # should contain Prometheus HELP lines
    assert b"# HELP" in r.content or b"python_gc_objects_collected_total" in r.content
