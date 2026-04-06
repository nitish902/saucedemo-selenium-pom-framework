from pages.products_page import ProductsPage


class TestProducts:


    def test_products_page_title(self, logged_in_driver):

        driver = logged_in_driver

        assert "inventory" in driver.current_url


    def test_total_products_count(self, logged_in_driver):

        products = ProductsPage(logged_in_driver)

        assert products.get_product_count() == 6


    def test_all_product_names(self, logged_in_driver):

        products = ProductsPage(logged_in_driver)

        names = products.get_all_product_names()

        assert len(names) > 0


    def test_all_product_prices(self, logged_in_driver):

        products = ProductsPage(logged_in_driver)

        prices = products.get_all_prices()

        assert len(prices) > 0


    def test_sort_z_to_a(self, logged_in_driver):

        products = ProductsPage(logged_in_driver)

        products.sort_by("Name (Z to A)")

        names = products.get_all_product_names()

        assert names == sorted(names, reverse=True)


    def test_sort_price_low_to_high(self, logged_in_driver):

        products = ProductsPage(logged_in_driver)

        products.sort_by("Price (low to high)")

        prices = products.get_all_prices()

        assert len(prices) > 0


    def test_add_backpack_to_cart(self, logged_in_driver):

        products = ProductsPage(logged_in_driver)

        products.add_to_cart("Sauce Labs Backpack")

        assert products.get_cart_badge() == "1"


    def test_add_multiple_products(self, logged_in_driver):

        products = ProductsPage(logged_in_driver)

        products.add_to_cart("Sauce Labs Backpack")

        products.add_to_cart("Sauce Labs Bike Light")

        assert products.get_cart_badge() == "2"


    def test_cart_icon_visible(self, logged_in_driver):

        products = ProductsPage(logged_in_driver)

        assert products.is_cart_icon_visible()


    def test_logout_works(self, logged_in_driver):

        products = ProductsPage(logged_in_driver)

        products.logout()

        assert "saucedemo" in logged_in_driver.current_url
