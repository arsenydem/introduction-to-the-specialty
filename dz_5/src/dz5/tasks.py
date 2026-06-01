from __future__ import annotations

from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Task:
    id: str
    title: str
    completed: bool = False


class TaskStore:
    """In-memory хранилище задач (логика из dz_2, упрощённо)."""

    def __init__(self) -> None:
        self._tasks: dict[str, Task] = {}

    def list_all(self, *, completed: bool | None = None) -> list[Task]:
        tasks = list(self._tasks.values())
        if completed is None:
            return tasks
        return [t for t in tasks if t.completed is completed]

    def get(self, task_id: str) -> Task | None:
        return self._tasks.get(task_id)

    def create(self, title: str) -> Task:
        normalized = validate_title(title)
        task = Task(id=str(uuid4()), title=normalized, completed=False)
        self._tasks[task.id] = task
        return task

    def update(self, task_id: str, *, title: str, completed: bool) -> Task:
        task = self._tasks.get(task_id)
        if task is None:
            raise KeyError(task_id)
        task.title = validate_title(title)
        task.completed = completed
        return task

    def delete(self, task_id: str) -> None:
        if task_id not in self._tasks:
            raise KeyError(task_id)
        del self._tasks[task_id]


def validate_title(title: str) -> str:
    if not title or not title.strip():
        raise ValueError("title must be a non-empty string")
    return title.strip()
