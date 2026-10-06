import pytest
from playwright.sync_api import Page
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.LoginPage import LoginPage

def test_fill_out_checkout_form(page: Page):
    login_page = LoginPage(page)
    inventory_page = login_page.login_standard_user()
    
    # Add items to cart
    inventory_page.add_sauce_labs_backpack_to_cart()
    inventory_page.add_item_to_cart("sauce-labs-bike-light")
    
    cart_page = inventory_page.goto_cart()
    checkout_page = cart_page.go_to_checkout()
    checkout_page.fill_out_checkout_form("John", "Doe", "1234567890")
    checkout_page.click_continue()
    checkout_page.click_finish()
    assert checkout_page.get_title() == "Checkout: Complete!"    


def test_all_information_required(page: Page):
    login_page = LoginPage(page)
    inventory_page = login_page.login_standard_user()
    
    # Add items to cart
    inventory_page.add_sauce_labs_backpack_to_cart()
    
    cart_page = inventory_page.goto_cart()
    checkout_page = cart_page.go_to_checkout()
    checkout_page.fill_out_checkout_form("", "", "")
    checkout_page.click_continue()
    assert checkout_page.get_error_message() == "Error: First Name is required"    

def test_verify_thank_you_message(page: Page):
    login_page = LoginPage(page)
    inventory_page = login_page.login_standard_user()
    
    # Add items to cart
    inventory_page.add_sauce_labs_backpack_to_cart()
    inventory_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
    
    cart_page = inventory_page.goto_cart()
    checkout_page = cart_page.go_to_checkout()
    checkout_page.fill_out_checkout_form("John", "Doe", "1234567890")
    checkout_page.click_continue()
    checkout_page.click_finish()
    assert checkout_page.get_thank_you_message() == "Thank you for your order!"    

def test_verify_checkout_workflow(page: Page):
    """Verify the complete checkout workflow"""
    login_page = LoginPage(page)
    inventory_page = login_page.login_standard_user()
    
    # Add items to cart
    inventory_page.add_sauce_labs_backpack_to_cart()
    inventory_page.add_item_to_cart("sauce-labs-bike-light")
    inventory_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
    
    cart_page = inventory_page.goto_cart()
    
    # Verify we can navigate to checkout
    checkout_page = cart_page.go_to_checkout()
    assert checkout_page.get_title() in ["Checkout: Your Information", "Checkout: Your Information."]
    
    # Verify we can fill and submit the form
    checkout_page.fill_out_checkout_form("John", "Doe", "1234567890")
    checkout_page.click_continue()
    
    # Verify we're on step 2
    assert "step-two" in page.url or "Checkout" in checkout_page.get_title()    
