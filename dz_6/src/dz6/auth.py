import os
from functools import lru_cache


@lru_cache
def get_api_key() -> str:
    """Ключ API только из окружения (не в исходниках)."""
    key = os.environ.get("API_KEY", "").strip()
    if not key:
        raise RuntimeError("API_KEY environment variable is required")
    return key


def verify_token(token: str | None) -> bool:
    if not token:
        return False
    expected = get_api_key()
    # Сравнение за константное время снижает риск timing-атаки.
    if len(token) != len(expected):
        return False
    result = 0
    for left, right in zip(token, expected, strict=True):
        result |= ord(left) ^ ord(right)
    return result == 0
