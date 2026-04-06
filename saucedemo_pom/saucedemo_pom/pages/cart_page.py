from pages.base_page import BasePage

class CartPage(BasePage):

    # ── Locators ──────────────────────────────────────────
    PAGE_TITLE        = "//span[@class='title']"
    CART_ITEMS        = "//div[@class='cart_item']"
    ITEM_NAMES        = "//div[@class='inventory_item_name']"
    CHECKOUT_BTN      = "//button[@id='checkout']"
    CONTINUE_SHOP_BTN = "//button[@id='continue-shopping']"

    # ── Actions ───────────────────────────────────────────
    def get_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_item_count(self):
        return len(self.finds(self.CART_ITEMS))

    def get_item_names(self):
        return [item.text for item in self.finds(self.ITEM_NAMES)]

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOP_BTN)