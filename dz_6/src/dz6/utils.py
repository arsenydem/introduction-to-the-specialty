import json
from typing import Any


def parse_json_payload(raw: str) -> Any:
    """Безопасный разбор JSON вместо eval/exec."""
    return json.loads(raw)
