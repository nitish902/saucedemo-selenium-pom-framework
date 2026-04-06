from pages.base_page import BasePage

class CheckoutPage(BasePage):

    # ── Locators ──────────────────────────────────────────
    FIRST_NAME    = "//input[@id='first-name']"
    LAST_NAME     = "//input[@id='last-name']"
    ZIP_CODE      = "//input[@id='postal-code']"
    CONTINUE_BTN  = "//input[@id='continue']"
    FINISH_BTN    = "//button[@id='finish']"
    ERROR_MSG     = "//h3[@data-test='error']"
    ORDER_CONFIRM = "//h2[@class='complete-header']"
    TOTAL_LABEL   = "//div[@class='summary_total_label']"

    # ── Actions ───────────────────────────────────────────
    def fill_details(self, first, last, zipcode):
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.ZIP_CODE, zipcode)
        self.click(self.CONTINUE_BTN)

    def click_finish(self):
        self.click(self.FINISH_BTN)

    def get_error(self):
        return self.get_text(self.ERROR_MSG)

    def get_confirmation(self):
        return self.get_text(self.ORDER_CONFIRM)

    def get_total(self):
        return self.get_text(self.TOTAL_LABEL)