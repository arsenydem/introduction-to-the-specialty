"""Минимальный сервис: использует requests для исходящего HTTP (сканируется Trivy)."""

import os

import requests
from fastapi import FastAPI, HTTPException

app = FastAPI(title="dz7 Dependency Demo")

UPSTREAM_URL = os.environ.get(
    "UPSTREAM_URL", "https://httpbin.org/get"
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/proxy-check")
def proxy_check() -> dict[str, object]:
    """Проверка цепочки зависимостей requests → urllib3 → certifi."""
    try:
        response = requests.get(UPSTREAM_URL, timeout=5)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return {"upstream": UPSTREAM_URL, "status_code": response.status_code}
