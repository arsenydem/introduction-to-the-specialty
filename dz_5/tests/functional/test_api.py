import pytest
from fastapi.testclient import TestClient

from dz5.app import create_app
from dz5.tasks import TaskStore

pytestmark = pytest.mark.functional


@pytest.fixture
def client() -> TestClient:
    return TestClient(create_app(store=TaskStore()))


def test_health(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_greet_endpoint(client: TestClient) -> None:
    response = client.get("/api/greet/Student")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Student!"}


def test_greet_bad_request(client: TestClient) -> None:
    response = client.get("/api/greet/%20")
    assert response.status_code == 400


def test_tasks_lifecycle(client: TestClient) -> None:
    create = client.post("/api/tasks", json={"title": "Write tests"})
    assert create.status_code == 201
    task_id = create.json()["id"]

    listing = client.get("/api/tasks")
    assert listing.status_code == 200
    assert len(listing.json()) == 1

    get_one = client.get(f"/api/tasks/{task_id}")
    assert get_one.status_code == 200

    updated = client.put(
        f"/api/tasks/{task_id}",
        json={"title": "Write tests", "completed": True},
    )
    assert updated.status_code == 200
    assert updated.json()["completed"] is True

    active = client.get("/api/tasks", params={"filter": "active"})
    assert active.json() == []

    completed = client.get("/api/tasks", params={"filter": "completed"})
    assert len(completed.json()) == 1

    deleted = client.delete(f"/api/tasks/{task_id}")
    assert deleted.status_code == 200
    assert client.get(f"/api/tasks/{task_id}").status_code == 404


def test_create_task_validation(client: TestClient) -> None:
    response = client.post("/api/tasks", json={"title": "   "})
    assert response.status_code == 400


def test_unknown_task_returns_404(client: TestClient) -> None:
    assert client.get("/api/tasks/unknown-id").status_code == 404
