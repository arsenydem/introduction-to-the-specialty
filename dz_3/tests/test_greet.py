import pytest

from dz3.greet import greet


def test_greet_returns_message() -> None:
    assert greet("World") == "Hello, World!"


def test_greet_strips_whitespace() -> None:
    assert greet("  Alice  ") == "Hello, Alice!"


def test_greet_rejects_empty_name() -> None:
    with pytest.raises(ValueError, match="non-empty"):
        greet("   ")
