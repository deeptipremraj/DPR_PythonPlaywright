import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/entry_ad")
    page.get_by_role("link", name="click here").click()
    page.get_by_text("Close", exact=True).click()
    expect(page.get_by_role("heading", name="Entry Ad")).to_be_visible()
