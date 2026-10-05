from playwright.sync_api import Page

from pages.InventoryPage import InventoryPage


class LoginPage:
    def __init__(self, page: Page) -> None:
        #Locators
        self.page = page
        self.username_field = page.locator("[data-test=\"username\"]")
        self.password_field = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")
        self.error_message = page.locator("[data-test=\"error\"]")

        self.login_credentials = page.locator("[data-test=\"login-credentials\"]")
        self.login_password = page.locator("[data-test=\"login-password\"]")

    #Methods
    def open(self):
        self.page.goto("/")

    #Standard user login method
    def login_standard_user(self):
        self.username_field.fill("standard_user")
        self.password_field.fill("secret_sauce")
        self.login_button.click()
        return InventoryPage(self.page) #returns the InventoryPage object

    #Generic login method using parameters
    def login_user(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
        return InventoryPage(self.page) #returns the InventoryPage object

    #Getters
    def get_login_credentials(self):
        return self.login_credentials.text_content()

    def get_login_password(self):
        return self.login_password.text_content()

    def get_error_message(self):
        return self.error_message.text_content()

    def get_login_button(self):
        return self.login_button.text_content()
        