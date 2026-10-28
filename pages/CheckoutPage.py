from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.postal_code_input = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.back_home_button = page.locator("[data-test='back-to-products']")
        self.error_message = page.locator("[data-test='error']")
        self.title = page.locator(".title")
        self.thank_you_message = page.locator(".complete-header")

    # Methods
    def fill_out_checkout_form(self, first_name: str, last_name: str, postal_code: str):
        """Fill out the checkout form"""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def click_continue(self):
        """Click the continue button"""
        self.continue_button.click()

    def click_finish(self):
        """Click the finish button"""
        self.finish_button.click()

    def back_home(self):
        from pages.InventoryPage import InventoryPage
        self.back_home_button.click()
        return InventoryPage(self.page)

    # Getters
    def get_title(self):
        return self.title.text_content()

    def get_error_message(self):
        """Get the error message if form validation fails"""
        return self.error_message.text_content()

    def get_thank_you_message(self):
        """Get the thank you message after successful checkout"""
        return self.thank_you_message.text_content()

    def get_finish_button_is_disabled(self):
        """Check if the finish button is disabled"""
        return self.finish_button.is_disabled()

    def get_continue_button_is_enabled(self):
        """Check if the continue button is enabled"""
        return not self.continue_button.is_disabled()
