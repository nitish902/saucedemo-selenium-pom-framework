from pages.base_page import BasePage

class LoginPage(BasePage):

    # ── Locators ──────────────────────────────────────────
    USERNAME  = "//input[@id='user-name']"
    PASSWORD  = "//input[@id='password']"
    LOGIN_BTN = "//input[@id='login-button']"
    ERROR_MSG = "//h3[@data-test='error']"

    # ── Actions ───────────────────────────────────────────
    def open(self):
        self.driver.get("https://www.saucedemo.com")

    def enter_username(self, username):
        self.type(self.USERNAME, username)

    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BTN)

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()