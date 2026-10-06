from playwright.sync_api import Page
from pages.CartPage import CartPage


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        # Locators
        self.title = page.locator(".title")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.inventory_items = page.locator(".inventory_item")
        self.inventory_item_names = page.locator(".inventory_item_name")
        self.inventory_item_prices = page.locator(".inventory_item_price")
        self.inventory_item_descriptions = page.locator(".inventory_item_desc")
        self.sort_options = page.locator("option")
        self.cart_icon = page.locator("[class='shopping_cart_link']")
        self.add_to_cart_backpack = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")

    # Methods
    def sort_inventory_items(self, sort_option: str):
        self.sort_dropdown.select_option(sort_option)
        return self.inventory_items.all_text_contents()

    def add_sauce_labs_backpack_to_cart(self):
        """Add Sauce Labs Backpack to cart"""
        self.add_to_cart_backpack.click()

    def goto_cart(self):
        self.cart_icon.click()
        return CartPage(self.page)

    def add_item_to_cart(self, item_name: str):
        self.page.locator(f"[data-test='add-to-cart-{item_name}']").click()
        return self

    # Getters
    def get_title(self):
        return self.title.text_content()

    def get_inventory_items(self):
        return self.inventory_items.all_text_contents()

    def get_inventory_item_names(self):
        return self.inventory_item_names.all_text_contents()

    def get_inventory_item_prices(self):
        return self.inventory_item_prices.all_text_contents()

    def get_sort_option_selected(self):
        """Get the currently selected sort option"""
        return self.sort_dropdown.input_value()
