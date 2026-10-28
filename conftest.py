"""
Pytest configuration and fixtures for DPR_PythonPlaywright
"""
import pyexpat
import sys
from pathlib import Path
from playwright.sync_api import Page
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from dotenv import load_dotenv
import os

load_dotenv()

SAUCE_USERNAME = os.getenv("SAUCE_USERNAME")
SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD")
BASE_URL = os.getenv("BASE_URL")

AUTH_STATE_PATH = "playwright/.auth/state.json"

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

import pytest

#auth fixtures
@pytest.fixture(scope="session")
def auth_state(browser):

    os.makedirs(os.path.dirname(AUTH_STATE_PATH),exist_ok=True)
    context=browser.new_context(base_url="https://www.saucedemo.com/")
    login_page = LoginPage(context.new_page())
    login_page.open()
    login_page.login_standard_user()
    context.storage_state(path="AUTH_STATE_PATH")
    yield context
    context.close() 

    return AUTH_STATE_PATH




@pytest.fixture
def login_page(new_context, auth_state: str) -> LoginPage:
    return new_context(storage_state=auth_state).new_page()





@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login_page = LoginPage(page)
    login_page.open()
    return login_page


@pytest.fixture
def inventory_page(login_page: LoginPage) -> InventoryPage:     
    return login_page.login_standard_user()

@pytest.fixture
def cart_page(inventory_page: InventoryPage) -> CartPage:
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    inventory_page.add_item_to_cart("sauce-labs-bike-light")
    return inventory_page.goto_cart()


@pytest.fixture
def start_checkout(cart_page: CartPage) -> CheckoutPage:
    """Open checkout from the cart (Checkout: Your Information)."""
    checkout_page = cart_page.go_to_checkout()
    checkout_page.first_name_input.wait_for()
    return checkout_page


@pytest.fixture
def complete_checkout(start_checkout: CheckoutPage) -> CheckoutPage:
    """Fill the form, continue, and finish (Checkout: Complete!)."""
    start_checkout.fill_out_checkout_form("John", "Doe", "1234567890")
    start_checkout.click_continue()
    start_checkout.finish_button.wait_for()
    start_checkout.click_finish()
    start_checkout.thank_you_message.wait_for()
    return start_checkout


#factory function for cart page
@pytest.fixture
def cart_with_items(inventory_page: InventoryPage):
    def _cart_with_items(*item_ids: str):
        for item_id in item_ids:
            inventory_page.add_item_to_cart(item_id)
        return inventory_page.goto_cart()
    return _cart_with_items