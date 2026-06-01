import json
import os

import pytest
from fastapi.testclient import TestClient

from dz6.app import app
from dz6.database import init_db
from dz6.utils import parse_json_payload

pytestmark = pytest.mark.unit


@pytest.fixture
def client(monkeypatch: pytest.MonkeyPatch) -> TestClient:
    monkeypatch.setenv("API_KEY", "test-secret-key")
    init_db()
    return TestClient(app)


def test_parse_json_rejects_invalid() -> None:
    with pytest.raises(json.JSONDecodeError):
        parse_json_payload("{not json}")


def test_api_requires_token(client: TestClient) -> None:
    response = client.post("/users", json={"username": "alice"})
    assert response.status_code == 401


def test_api_works_with_valid_token(client: TestClient) -> None:
    headers = {"Authorization": "Bearer test-secret-key"}
    created = client.post("/users", json={"username": "bob"}, headers=headers)
    assert created.status_code == 200

    fetched = client.get("/users/bob", headers=headers)
    assert fetched.status_code == 200
    assert fetched.json()["username"] == "bob"


def test_get_api_key_requires_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("API_KEY", raising=False)
    from dz6.auth import get_api_key

    get_api_key.cache_clear()
    with pytest.raises(RuntimeError):
        get_api_key()
    get_api_key.cache_clear()
    monkeypatch.setenv("API_KEY", "x")
    assert get_api_key() == "x"
    get_api_key.cache_clear()
