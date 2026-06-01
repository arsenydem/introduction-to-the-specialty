import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[2] / "data" / "app.db"


def get_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL
            )
            """
        )
        conn.commit()


def find_user_by_name(username: str) -> sqlite3.Row | None:
    """Параметризованный запрос — защита от SQL injection."""
    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT id, username FROM users WHERE username = ?",
            (username,),
        )
        return cursor.fetchone()


def create_user(username: str) -> int:
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO users (username) VALUES (?)",
            (username.strip(),),
        )
        conn.commit()
        return int(cursor.lastrowid)
