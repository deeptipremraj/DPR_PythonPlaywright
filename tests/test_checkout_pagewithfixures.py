"""Test checkout page using fixtures"""
from pages.CheckoutPage import CheckoutPage
import pytest


def test_fill_out_checkout_form(start_checkout: CheckoutPage):
    """Test filling out checkout form from the start of checkout"""
    assert start_checkout.get_title() in ["Checkout: Your Information", "Checkout: Your Information."]
    start_checkout.fill_out_checkout_form("John", "Doe", "1234567890")
    start_checkout.click_continue()
    # After continue, should be on overview page
    start_checkout.finish_button.wait_for()
    assert "Checkout: Overview" in start_checkout.get_title()


def test_all_information_required(start_checkout: CheckoutPage):
    """Test that all fields are required"""
    start_checkout.fill_out_checkout_form("", "", "")
    start_checkout.click_continue()
    error_msg = start_checkout.get_error_message()
    assert "required" in error_msg.lower()


def test_verify_thank_you_message(complete_checkout: CheckoutPage):
    """Test thank you message appears after checkout is complete"""
    thank_you = complete_checkout.get_thank_you_message()
    assert "thank" in thank_you.lower() or "complete" in thank_you.lower()


def test_complete_checkout_workflow(complete_checkout: CheckoutPage):
    """Test the completed checkout lands on the confirmation page"""
    assert "Complete" in complete_checkout.get_title()
    assert complete_checkout.get_thank_you_message() == "Thank you for your order!"

@pytest.mark.parametrize(
    "first_name, last_name, postal_code", 
    [
    ("John", "Doe", "1234567890"), 
    ("Jane", "Doe", "0987654321")
    ]
)
def test_checkout_with_different_customers(start_checkout: CheckoutPage, first_name: str, last_name: str, postal_code: str):
    """Test checkout with different customers"""
    start_checkout.fill_out_checkout_form(first_name, last_name, postal_code)
    start_checkout.click_continue()
    start_checkout.finish_button.wait_for()
    start_checkout.click_finish()
    start_checkout.thank_you_message.wait_for()
    assert "Checkout: Complete!" in start_checkout.get_title()
    assert start_checkout.get_thank_you_message() == "Thank you for your order!"


def test_back_home_after_checkout(complete_checkout: CheckoutPage):
    """Test back home after checkout"""
    inventory_page = complete_checkout.back_home()
    inventory_page.title.wait_for()
    assert "Products" in inventory_page.get_title()

