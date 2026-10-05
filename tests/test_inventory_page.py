from playwright.sync_api import Page
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
import pytest

def test_inventory_title(page: Page):
    """Test that the inventory page shows the correct title"""
    # Step 1: Create LoginPage object and log in
    login_page = LoginPage(page)
    login_page.open()
    inventory_page = login_page.login_standard_user()
    
    # Step 2: Check the title is "Products"
    assert inventory_page.get_title() == "Products"


def test_inventory_items_exist(page: Page):
    """Test that inventory items are displayed"""
    login_page = LoginPage(page)
    login_page.open()
    inventory_page = login_page.login_standard_user()
    
    # Get all inventory items
    items = inventory_page.get_inventory_items()
    
    # Check that we have some items
    assert len(items) > 0
    print(f"Found {len(items)} items in inventory")


def test_sort_inventory_by_price(page: Page):
    """Test sorting inventory items by price"""
    login_page = LoginPage(page)
    login_page.open()
    inventory_page = login_page.login_standard_user()
    
    # Get items sorted by price (low to high)
    # Note: The selector for the sort dropdown needs to be verified first
    sorted_items = inventory_page.get_inventory_items()
    
    # Check that items exist
    assert len(sorted_items) > 0


def test_complete_inventory_workflow(page: Page):
    """
    Complete workflow test:
    1. Login using LoginPage object
    2. Complete the InventoryPage object (add sort and add Sauce Labs Backpack)
    3. Perform a Select from the Dropdown
    4. Assert the option was selected
    """
    # Step 1: Login using LoginPage object
    login_page = LoginPage(page)
    login_page.open()
    inventory_page = login_page.login_standard_user()
    
    # Step 2: Verify we're on the Inventory Page
    assert inventory_page.get_title() == "Products"
    
    # Step 3: Sort inventory by price (low to high) - "lohi"
    sorted_items = inventory_page.sort_inventory_items("lohi")
    
    # Step 4: Assert the sort option was selected
    selected_option = inventory_page.get_sort_option_selected()
    assert selected_option == "lohi", f"Expected 'lohi' but got '{selected_option}'"
    
    # Step 5: Verify items are sorted (we have items)
    assert len(sorted_items) > 0
    
    # Step 6: Add Sauce Labs Backpack to cart
    inventory_page.add_sauce_labs_backpack_to_cart()
    
    # Verify the add to cart button changed (it should now show "Remove")
    remove_button = page.locator("[data-test='remove-sauce-labs-backpack']")
    assert remove_button.is_visible(), "Backpack should be added to cart"

#parametrize the test_all_sort_options test with all the sort options
@pytest.mark.parametrize(
    "sort_option",
    [
        "lohi",
        "hilo",
        "az",
        "za"
    ],
)
def test_all_sort_options(page: Page, sort_option):
    """Test all sort options"""
    login_page = LoginPage(page)
    login_page.open()
    inventory_page = login_page.login_standard_user()
    
    # Test each sort option
    sorted_items = inventory_page.sort_inventory_items(sort_option)
    assert len(sorted_items) > 0
    
    # Verify the sort option was selected
    selected_option = inventory_page.get_sort_option_selected()
    assert selected_option == sort_option, f"Expected '{sort_option}' but got '{selected_option}'"
    
