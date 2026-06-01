"""
УЧЕБНЫЕ примеры небезопасного кода (НЕ используется в приложении).

Запуск Semgrep только на этой папке показывает типичные срабатывания:
  semgrep scan --config p/python --config p/secrets training/
"""

import os
import sqlite3

# rule: hardcoded-secret / generic.secrets
API_KEY = "super-secret-key-12345"

# rule: python.lang.security.audit.dangerous-eval
def run_user_code(expression: str) -> object:
    return eval(expression)  # noqa: S307


# rule: python.lang.security.audit.sql-injection
def find_user_unsafe(username: str) -> None:
    conn = sqlite3.connect("app.db")
    query = f"SELECT * FROM users WHERE username = '{username}'"
    conn.execute(query)


# rule: python.lang.security.audit.insecure-hash
import hashlib

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


# rule: python.lang.security.audit.subprocess-shell-true
import subprocess

def ping(host: str) -> None:
    subprocess.call(f"ping -c 1 {host}", shell=True)
