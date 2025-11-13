from fastapi import FastAPI

# Instance FastAPI exposée sous le nom 'app' pour uvicorn (app.main:app)
app = FastAPI(title="Mini API", version="0.1.0")

@app.get("/hello")
def health():
    return {"message": "Hello world"}

# Endpoint exemple simple
@app.get("/")
def root():
    return {"message": "OK"}