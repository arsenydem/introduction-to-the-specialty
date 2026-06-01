import pytest

from dz5.tasks import TaskStore, validate_title

pytestmark = pytest.mark.unit


def test_validate_title_strips() -> None:
    assert validate_title("  task  ") == "task"


def test_validate_title_rejects_empty() -> None:
    with pytest.raises(ValueError):
        validate_title("   ")


def test_store_crud_and_filters() -> None:
    store = TaskStore()
    a = store.create("First")
    b = store.create("Second")
    store.update(b.id, title="Second", completed=True)

    assert len(store.list_all()) == 2
    assert len(store.list_all(completed=False)) == 1
    assert len(store.list_all(completed=True)) == 1

    store.delete(a.id)
    assert store.get(a.id) is None
    assert store.get(b.id) is not None


def test_store_update_missing_raises() -> None:
    store = TaskStore()
    with pytest.raises(KeyError):
        store.update("missing", title="x", completed=False)
