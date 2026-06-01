from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from dz5.greet import greet
from dz5.tasks import Task, TaskStore

STATIC_DIR = Path(__file__).resolve().parent.parent.parent / "static"


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)


class TaskUpdate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool


def create_app(store: TaskStore | None = None) -> FastAPI:
    app = FastAPI(title="dz5 Tasks API")
    task_store = store if store is not None else TaskStore()

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.get("/api/greet/{name}")
    def api_greet(name: str) -> dict[str, str]:
        try:
            message = greet(name)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return {"message": message}

    @app.get("/api/tasks")
    def list_tasks(
        filter: str | None = Query(default=None, alias="filter"),
    ) -> list[Task]:
        completed: bool | None = None
        if filter == "active":
            completed = False
        elif filter == "completed":
            completed = True
        elif filter not in (None, "all"):
            raise HTTPException(status_code=400, detail="invalid filter")
        return task_store.list_all(completed=completed)

    @app.post("/api/tasks", status_code=201)
    def create_task(body: TaskCreate) -> Task:
        try:
            return task_store.create(body.title)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc

    @app.get("/api/tasks/{task_id}")
    def get_task(task_id: str) -> Task:
        task = task_store.get(task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="task not found")
        return task

    @app.put("/api/tasks/{task_id}")
    def update_task(task_id: str, body: TaskUpdate) -> Task:
        try:
            return task_store.update(
                task_id, title=body.title, completed=body.completed
            )
        except KeyError as exc:
            raise HTTPException(status_code=404, detail="task not found") from exc
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc

    @app.delete("/api/tasks/{task_id}")
    def delete_task(task_id: str) -> dict[str, bool]:
        try:
            task_store.delete(task_id)
        except KeyError as exc:
            raise HTTPException(status_code=404, detail="task not found") from exc
        return {"success": True}

    @app.get("/")
    def index() -> FileResponse:
        return FileResponse(STATIC_DIR / "index.html")

    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
    return app


app = create_app()
