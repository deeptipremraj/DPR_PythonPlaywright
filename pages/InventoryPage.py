from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        # Locators
        self.title = page.locator(".title")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.inventory_items = page.locator(".inventory_item")
        self.add_to_cart_backpack = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")

    # Methods
    def get_title(self):
        return self.title.text_content()

    def get_inventory_items(self):
        return self.inventory_items.all_text_contents()

    def sort_inventory_items(self, sort_option: str):
        self.sort_dropdown.select_option(sort_option)
        return self.inventory_items.all_text_contents()
    
    def get_sort_option_selected(self):
        """Get the currently selected sort option"""
        return self.sort_dropdown.input_value()
    
    def add_sauce_labs_backpack_to_cart(self):
        """Add Sauce Labs Backpack to cart"""
        self.add_to_cart_backpack.click()
