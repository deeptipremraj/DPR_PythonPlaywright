"""Test login page using fixtures"""
import pytest
from pages.LoginPage import LoginPage


def test_login_credentials(login_page: LoginPage):
    """Test that login page displays credentials hints"""
    assert "standard_user" in login_page.get_login_credentials()
    assert "secret_sauce" in login_page.get_login_password()


def test_successful_login(login_page: LoginPage):
    """Test successful login with standard user"""
    login_page.login_standard_user()
    # After login, we're on inventory page, so we can't check login page elements
    # Instead, verify the login was successful by checking the page URL
    assert "inventory" in login_page.page.url


def test_login_with_custom_credentials(login_page: LoginPage):
    """Test login with custom username and password"""
    login_page.login_user("standard_user", "secret_sauce")
    # Verify login successful
    assert "inventory" in login_page.page.url


def test_error_message_visible_on_invalid_login(login_page: LoginPage):
    """Test that error message appears on invalid login"""
    login_page.login_user("invalid_user", "invalid_pass")
    error_msg = login_page.get_error_message()
    assert "do not match" in error_msg or "Username and password" in error_msg
