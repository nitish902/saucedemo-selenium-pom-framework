from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")

    PASSWORD = (By.ID, "password")

    LOGIN_BTN = (By.ID, "login-button")


    def open(self):

        super().open()


    def login(self, username, password):

        self.type(self.USERNAME, username)

        self.type(self.PASSWORD, password)

        self.click(self.LOGIN_BTN)
