def greet(name: str) -> str:
    """Возвращает приветствие для переданного имени."""
    if not name or not name.strip():
        raise ValueError("name must be a non-empty string")
    return f"Hello, {name.strip()}!"
