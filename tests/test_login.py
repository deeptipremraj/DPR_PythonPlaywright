import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    # NAVIGATE
    page.goto("https://www.saucedemo.com/")
    #    LOCATE                             . ACT/ACTIONS  
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    #    LOCATE                             . ACT/ACTIONS   . ASSERT ==expected result
    expect(page.locator("[data-test=\"secondary-header\"]")).to_be_visible()
    #expect is same as assert
