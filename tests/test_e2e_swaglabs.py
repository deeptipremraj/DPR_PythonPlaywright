import re
from playwright.sync_api import Page
import pytest


@pytest.mark.parametrize(
    "username, password",
    [
        ("standard_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
        ("visual_user", "secret_sauce"),
    ],
)
def e2e_swaglabs_test(page: Page, username, password) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("tester")
    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"lastName\"]").fill("tester")
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("03885")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()
    assert page.locator("[data-test=\"complete-header\"]").is_visible()
    assert "Thank you for your order!" in page.locator("[data-test=\"complete-header\"]").text_content()
    page.locator("[data-test=\"back-to-products\"]").click()


@pytest.mark.parametrize(
    "username, password, error_message",
    [
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
        ("standard_user", "wrong_password", "Username and password do not match any user in this service"),
    ],
)
def test_invalid_login(page: Page, username, password, error_message) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()
    error = page.locator("[data-test=\"error\"]")
    assert error.is_visible()
    assert error_message in error.text_content()


def test_problem_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("problem_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"lastName\"]").fill("tester")
    assert page.locator("[data-test=\"lastName\"]").input_value() == ""
