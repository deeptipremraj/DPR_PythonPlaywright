import pytest

from playwright.sync_api import Page
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage


def test_cart_page_loads(cart_page: CartPage):
    
    # Cart page should be visible
    assert cart_page.title.is_visible()
    assert cart_page.title.text_content() == "Your Cart"
    
    # Items should be visible since we added them
    assert cart_page.inventory_item_names.first.is_visible()
    assert cart_page.checkout_button.is_visible()
    
    # Assert the item count is 2
    assert len(cart_page.inventory_item_names.all()) == 2
    
    # Assert item prices are visible
    assert cart_page.inventory_item_prices.first.is_visible()
    assert len(cart_page.inventory_item_prices.all()) == 2
    
    # Assert item descriptions are visible
    assert cart_page.inventory_item_descriptions.first.is_visible()
    assert len(cart_page.inventory_item_descriptions.all()) == 2

    # Assert the item count is 2
    assert cart_page.get_inventory_item_count() == 2

    # Assert the item prices are correct
    prices = cart_page.get_inventory_item_prices()
    assert len(prices) == 2
    assert "$" in prices[0]  # Has price format
    assert "$" in prices[1]

    # Assert the item descriptions exist
    descriptions = cart_page.get_inventory_item_descriptions()
    assert len(descriptions) == 2
    assert descriptions[0]  # Non-empty description
    assert descriptions[1]  # Non-empty description


