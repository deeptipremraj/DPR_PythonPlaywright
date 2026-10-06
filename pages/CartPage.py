from playwright.sync_api import Page
from pages.CheckoutPage import CheckoutPage

class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        # Locators
        self.title = page.locator(".title")
        self.inventory_item_names = page.locator(".inventory_item_name")
        self.inventory_item_prices = page.locator(".inventory_item_price")
        self.inventory_item_descriptions = page.locator(".inventory_item_desc")
        
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.sort_options = page.locator("option")
        
        self.cart_icon = page.locator("[class='shopping_cart_link']")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")
        self.remove_item_from_cart = page.locator("[data-test='remove-sauce-labs-backpack']")

    # Methods
    def go_to_checkout(self):
        self.checkout_button.click()
        return CheckoutPage(self.page)

    # Getters
    def get_title(self):
        return self.title.text_content()

    def get_inventory_item_names(self):
        return self.inventory_item_names.all_text_contents()

    def get_inventory_item_prices(self):
        return self.inventory_item_prices.all_text_contents()

    def get_inventory_item_descriptions(self):
        return self.inventory_item_descriptions.all_text_contents()

    def get_inventory_item_count(self):
        return self.inventory_item_names.count()

    def get_cart_icon(self):
        return self.cart_icon.text_content()
