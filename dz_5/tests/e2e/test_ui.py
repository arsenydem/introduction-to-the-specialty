import pytest
from playwright.sync_api import Page, expect

pytestmark = pytest.mark.e2e


def test_homepage_add_task(page: Page, live_server: str) -> None:
    page.goto(f"{live_server}/")
    expect(page.get_by_role("heading", name="Задачи (dz_5)")).to_be_visible()

    page.get_by_placeholder("Название").fill("E2E task")
    page.get_by_role("button", name="Добавить").click()

    expect(page.get_by_text("E2E task")).to_be_visible()


def test_api_greet_via_browser_fetch(page: Page, live_server: str) -> None:
    page.goto(f"{live_server}/")
    message = page.evaluate(
        """async () => {
            const res = await fetch('/api/greet/Browser');
            const data = await res.json();
            return data.message;
        }"""
    )
    assert message == "Hello, Browser!"
