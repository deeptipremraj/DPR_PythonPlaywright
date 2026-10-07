import re
from playwright.sync_api import Page, expect
import pytest


@pytest.mark.external
def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/login", timeout=60000, wait_until="domcontentloaded")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("tomsmith")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()



