import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demoqa.com/elements/")
    page.get_by_role("link", name="Text Box").click()
    page.get_by_role("textbox", name="Full Name").click()
    page.get_by_role("textbox", name="name@example.com").click()
    page.get_by_role("textbox", name="Current Address").click()
    page.locator("#permanentAddress").click()
    page.get_by_role("button", name="Submit").click()
