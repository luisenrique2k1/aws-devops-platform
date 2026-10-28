from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(title="AWS DevOps Platform API")


@app.get("/")
def root():
    return {
        "message": "Welcome to AWS DevOps Platform",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }