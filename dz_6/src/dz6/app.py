from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

from dz6.auth import verify_token
from dz6.database import create_user, find_user_by_name, init_db

app = FastAPI(title="dz6 Security Demo")


class UserCreate(BaseModel):
    username: str = Field(min_length=1, max_length=64)


def require_auth(authorization: str | None = Header(default=None)) -> None:
    token = None
    if authorization and authorization.lower().startswith("bearer "):
        token = authorization[7:].strip()
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="unauthorized")


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/users", dependencies=[Depends(require_auth)])
def register_user(body: UserCreate) -> dict[str, int | str]:
    if find_user_by_name(body.username):
        raise HTTPException(status_code=409, detail="user exists")
    user_id = create_user(body.username)
    return {"id": user_id, "username": body.username}


@app.get("/users/{username}", dependencies=[Depends(require_auth)])
def get_user(username: str) -> dict[str, int | str]:
    row = find_user_by_name(username)
    if row is None:
        raise HTTPException(status_code=404, detail="not found")
    return {"id": row["id"], "username": row["username"]}
