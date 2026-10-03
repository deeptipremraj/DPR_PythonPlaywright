import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/context_menu")
    page.locator("#hot-spot").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.locator("#hot-spot").click(button="right")
