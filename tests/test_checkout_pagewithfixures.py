"""Test checkout page using fixtures"""
import pytest
from pages.CheckoutPage import CheckoutPage


def test_fill_out_checkout_form(checkout_page: CheckoutPage):
    """Test filling out checkout form"""
    assert checkout_page.get_title() in ["Checkout: Your Information", "Checkout: Your Information."]
    checkout_page.fill_out_checkout_form("John", "Doe", "1234567890")
    checkout_page.click_continue()
    # After continue, should be on overview page
    assert "Checkout: Overview" in checkout_page.get_title()


def test_all_information_required(checkout_page: CheckoutPage):
    """Test that all fields are required"""
    checkout_page.fill_out_checkout_form("", "", "")
    checkout_page.click_continue()
    error_msg = checkout_page.get_error_message()
    assert "required" in error_msg.lower()


def test_verify_thank_you_message(checkout_page: CheckoutPage):
    """Test thank you message appears after checkout"""
    checkout_page.fill_out_checkout_form("John", "Doe", "1234567890")
    checkout_page.click_continue()
    checkout_page.click_finish()
    thank_you = checkout_page.get_thank_you_message()
    assert "thank" in thank_you.lower() or "complete" in thank_you.lower()


def test_complete_checkout_workflow(checkout_page: CheckoutPage):
    """Test complete checkout workflow from form to confirmation"""
    # Verify we're on checkout information page
    assert "Your Information" in checkout_page.get_title()
    
    # Fill and submit checkout form
    checkout_page.fill_out_checkout_form("Jane", "Smith", "9876543210")
    checkout_page.click_continue()
    
    # Verify we're on overview page
    assert "Overview" in checkout_page.get_title()
    
    # Complete purchase
    checkout_page.click_finish()
    
    # Verify completion
    assert "Complete" in checkout_page.get_title()
