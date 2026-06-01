import pytest

from dz5.greet import greet

pytestmark = pytest.mark.unit


def test_greet_success() -> None:
    assert greet("World") == "Hello, World!"


def test_greet_strips_whitespace() -> None:
    assert greet("  Alice  ") == "Hello, Alice!"


def test_greet_rejects_empty() -> None:
    with pytest.raises(ValueError, match="non-empty"):
        greet("")
