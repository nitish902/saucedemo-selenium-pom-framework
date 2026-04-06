from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestEndToEnd:


    def test_complete_purchase_flow(self, logged_in_driver):

        products = ProductsPage(logged_in_driver)

        products.add_to_cart("Sauce Labs Backpack")

        products.click_cart()

        cart = CartPage(logged_in_driver)

        cart.click_checkout()

        checkout = CheckoutPage(logged_in_driver)

        checkout.fill_information("Donald", "Trump", "224010")

        checkout.finish_checkout()

        assert "checkout-complete" in logged_in_driver.current_url
