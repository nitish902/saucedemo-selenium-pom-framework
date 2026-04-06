from pages.products_page import ProductsPage
from pages.cart_page import CartPage


class TestCart:


    def test_cart_page_title(self, logged_in_driver):

        products = ProductsPage(logged_in_driver)

        products.click_cart()

        assert "cart" in logged_in_driver.current_url


    def test_cart_item_count(self, logged_in_driver):

        products = ProductsPage(logged_in_driver)

        products.add_to_cart("Sauce Labs Backpack")

        products.click_cart()

        cart = CartPage(logged_in_driver)

        assert cart.get_cart_item_count() == 1


    def test_cart_item_names(self, logged_in_driver):

        products = ProductsPage(logged_in_driver)

        products.add_to_cart("Sauce Labs Backpack")

        products.click_cart()

        cart = CartPage(logged_in_driver)

        names = cart.get_cart_items()

        assert "Sauce Labs Backpack" in names


    def test_continue_shopping(self, logged_in_driver):

        products = ProductsPage(logged_in_driver)

        products.click_cart()

        cart = CartPage(logged_in_driver)

        cart.click_continue_shopping()

        assert "inventory" in logged_in_driver.current_url


    def test_checkout_button(self, logged_in_driver):

        products = ProductsPage(logged_in_driver)

        products.add_to_cart("Sauce Labs Backpack")

        products.click_cart()

        cart = CartPage(logged_in_driver)

        cart.click_checkout()

        assert "checkout" in logged_in_driver.current_url


    def test_empty_cart(self, logged_in_driver):

        products = ProductsPage(logged_in_driver)

        products.click_cart()

        cart = CartPage(logged_in_driver)

        assert cart.get_cart_item_count() == 0


    def test_cart_url(self, logged_in_driver):

        products = ProductsPage(logged_in_driver)

        products.click_cart()

        assert "cart" in logged_in_driver.current_url
