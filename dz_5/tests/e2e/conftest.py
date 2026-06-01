import os
import subprocess
import time
from pathlib import Path

import httpx
import pytest

BASE_URL = "http://127.0.0.1:8765"
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"


@pytest.fixture(scope="session")
def live_server() -> str:
    """Поднимает реальный uvicorn для e2e (не TestClient)."""
    env = os.environ.copy()
    env["PYTHONPATH"] = str(SRC_PATH)

    proc = subprocess.Popen(
        [
            "python",
            "-m",
            "uvicorn",
            "dz5.app:app",
            "--host",
            "127.0.0.1",
            "--port",
            "8765",
        ],
        cwd=PROJECT_ROOT,
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        for _ in range(50):
            try:
                response = httpx.get(f"{BASE_URL}/health", timeout=1.0)
                if response.status_code == 200:
                    break
            except httpx.HTTPError:
                time.sleep(0.2)
        else:
            proc.terminate()
            pytest.fail("Server did not start in time")
        yield BASE_URL
    finally:
        proc.terminate()
        proc.wait(timeout=5)
