from playwright.sync_api import Page
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
import pytest

def test_login_credentials(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    
    assert "standard_user" in login_page.get_login_credentials()
    assert "secret_sauce" in login_page.get_login_password()

def test_login_successful(page: Page):
    #login Object has access to all the methods in the LoginPage class
    login_page = LoginPage(page)
    login_page.open()
   # login_page.login_standard_user()
    #inventory_page = InventoryPage(page)
    #inventory_page.get_title()
    #assert inventory_page.get_title().text_content() == "Products"

    #inv object has access to all the methods in the InventoryPage class
    inventory_page = login_page.login_standard_user()
    assert inventory_page.get_title() == "Products"


@pytest.mark.parametrize(
    "username",
    [
        ("standard_user"),
        ("problem_user"),
        ("performance_glitch_user"),
        ("visual_user")
    ],
)
def test_login_successful_with_all_users(page: Page, username):
    #login Object has access to all the methods in the LoginPage class
    login_page = LoginPage(page)
    login_page.open()
    login_page.login_user(username, "secret_sauce")
    #inv object has access to all the methods in the InventoryPage class
    inventory_page = InventoryPage(page)
    assert inventory_page.get_title() == "Products"


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
        ("standard_user", "wrong_password", "Username and password do not match any user in this service"),
    ],
)
def test_login_failed(page: Page, username: str, password: str, expected_error: str):
    """Negative test cases for login failures"""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login_user(username, password)
    actual_error_message = login_page.get_error_message()
    assert expected_error in actual_error_message