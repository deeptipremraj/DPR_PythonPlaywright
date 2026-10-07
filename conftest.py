"""
Pytest configuration and fixtures for DPR_PythonPlaywright
"""
import sys
from pathlib import Path
from playwright.sync_api import Page
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

import pytest

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login_page = LoginPage(page)
    login_page.open()
    return login_page


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    login_page = LoginPage(page)
    login_page.open()
    inventory_page = login_page.login_standard_user()
    return inventory_page

@pytest.fixture
def cart_page(inventory_page: InventoryPage) -> CartPage:
    # Add items to cart before navigating
    inventory_page.add_sauce_labs_backpack_to_cart()
    inventory_page.add_item_to_cart("sauce-labs-bike-light")
    return inventory_page.goto_cart()

@pytest.fixture
def checkout_page(cart_page: CartPage) -> CheckoutPage:
    return cart_page.go_to_checkout()