from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class ProductsPage(BasePage):

    PAGE_TITLE = "//span[text()='Products']"

    PRODUCT_CARDS = "//div[@class='inventory_item']"

    PRODUCT_NAMES = "//div[@data-test='inventory-item-name']"

    ALL_PRICES = "//div[@class='inventory_item_price']"

    CART_BADGE = "//span[@class='shopping_cart_badge']"

    CART_ICON = "//a[@class='shopping_cart_link']"

    SORT_DROPDOWN = "//select[@class='product_sort_container']"

    BURGER_MENU = "//button[@id='react-burger-menu-btn']"

    LOGOUT_LINK = "//a[@id='logout_sidebar_link']"

    LOGIN_BUTTON = "//input[@id='login-button']"


    def get_title(self):

        return self.get_text(self.PAGE_TITLE)


    def get_product_count(self):

        return len(self.finds(self.PRODUCT_CARDS))


    def get_all_product_names(self):

        elements = self.finds(self.PRODUCT_NAMES)

        return [e.text for e in elements]


    def get_all_prices(self):

        elements = self.finds(self.ALL_PRICES)

        return [e.text for e in elements]


    def get_cart_badge(self):

        return self.get_text(self.CART_BADGE)


    def click_cart(self):

        self.click(self.CART_ICON)


    def sort_by(self, option_text):

        dropdown = Select(self.find(self.SORT_DROPDOWN))

        dropdown.select_by_visible_text(option_text)


    def add_to_cart(self, product_name):

        product_name_lower = product_name.lower().replace(" ", "-")

        xpath = f"//button[@data-test='add-to-cart-{product_name_lower}']"

        button = self.find(xpath)

        # scroll to button
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            button
        )

        # click using JS for reliability
        self.driver.execute_script(
            "arguments[0].click();",
            button
        )


    def logout(self):

        # open menu
        self.click(self.BURGER_MENU)

        # wait until logout visible
        self.wait_for(self.LOGOUT_LINK)

        logout_btn = self.find(self.LOGOUT_LINK)

        # click using JS
        self.driver.execute_script(
            "arguments[0].click();",
            logout_btn
        )