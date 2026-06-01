from fastapi.testclient import TestClient

from dz7.app import app


def test_health() -> None:
    client = TestClient(app)
    assert client.get("/health").json() == {"status": "ok"}
