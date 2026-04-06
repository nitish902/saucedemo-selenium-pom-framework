import pytest
import time
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

class TestProducts:

    def test_products_page_title(self, logged_in_driver):
        products = ProductsPage(logged_in_driver)
        title = products.get_title()
        print(f"\nPage Title: {title}")
        assert "Products" in title
        print("Test 1 Passed - Products page title verified!")

    def test_total_products_count(self, logged_in_driver):
        products = ProductsPage(logged_in_driver)
        count = products.get_product_count()
        print(f"\nTotal Products: {count}")
        assert count == 6
        print("Test 2 Passed - 6 products found!")

    def test_all_product_names(self, logged_in_driver):
        products = ProductsPage(logged_in_driver)
        names = products.get_all_product_names()
        print("\n--- All Product Names ---")
        for name in names:
            print(name)
        assert len(names) == 6
        print("Test 3 Passed - All product names read!")

    def test_all_product_prices(self, logged_in_driver):
        products = ProductsPage(logged_in_driver)
        prices = products.get_all_prices()
        print("\n--- All Product Prices ---")
        for price in prices:
            print(price)
            assert "$" in price
        print("Test 4 Passed - All prices have $ sign!")

    def test_sort_z_to_a(self, logged_in_driver):
        products = ProductsPage(logged_in_driver)
        products.sort_by("Name (Z to A)")
        time.sleep(2)
        names = products.get_all_product_names()
        first_product = names[0]
        print(f"\nFirst product after Z to A: {first_product}")
        assert first_product == "Test.allTheThings() T-Shirt (Red)"
        print("Test 5 Passed - Sort Z to A works!")

    def test_sort_price_low_to_high(self, logged_in_driver):
        products = ProductsPage(logged_in_driver)
        products.sort_by("Price (low to high)")
        time.sleep(2)
        prices = products.get_all_prices()
        first_price = prices[0]
        print(f"\nFirst price after Low to High: {first_price}")
        assert first_price == "$7.99"
        print("Test 6 Passed - Sort Low to High works!")

    def test_add_backpack_to_cart(self, logged_in_driver):
        products = ProductsPage(logged_in_driver)
        products.add_to_cart("Sauce Labs Backpack")
        time.sleep(2)
        badge = products.get_cart_badge()
        print(f"\nCart Badge: {badge}")
        assert badge == "1"
        print("Test 7 Passed - Backpack added to cart!")

    def test_add_multiple_products(self, logged_in_driver):
        products = ProductsPage(logged_in_driver)
        products.add_to_cart("Sauce Labs Backpack")
        time.sleep(2)
        products.add_to_cart("Sauce Labs Bike Light")
        time.sleep(2)
        badge = products.get_cart_badge()
        print(f"\nCart Badge after 2 products: {badge}")
        assert badge == "2"
        print("Test 8 Passed - 2 products added to cart!")

    def test_cart_icon_visible(self, logged_in_driver):
        products = ProductsPage(logged_in_driver)
        cart = products.is_visible(products.CART_ICON)
        assert cart == True
        print("\nTest 9 Passed - Cart icon is visible!")

    def test_logout_works(self, logged_in_driver):
        products = ProductsPage(logged_in_driver)
        products.logout()
        time.sleep(3)
        current_url = logged_in_driver.current_url
        print(f"\nURL after logout: {current_url}")
        assert "index" in current_url or "saucedemo.com" in current_url
        assert "inventory" not in current_url
        print("Test 10 Passed - Logout works!")
