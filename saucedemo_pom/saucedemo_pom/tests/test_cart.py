import pytest
import time
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

class TestCart:

    def test_cart_page_title(self, logged_in_driver):
        products = ProductsPage(logged_in_driver)
        products.add_to_cart("Sauce Labs Backpack")
        time.sleep(2)
        products.click_cart()
        time.sleep(2)
        cart = CartPage(logged_in_driver)
        title = cart.get_title()
        print(f"\nCart Page Title: {title}")
        assert "Your Cart" in title
        print("Test 1 Passed - Cart page title verified!")

    def test_cart_item_count(self, logged_in_driver):
        products = ProductsPage(logged_in_driver)
        products.add_to_cart("Sauce Labs Backpack")
        time.sleep(2)
        products.add_to_cart("Sauce Labs Bike Light")
        time.sleep(2)
        products.click_cart()
        time.sleep(2)
        cart = CartPage(logged_in_driver)
        count = cart.get_item_count()
        print(f"\nItems in cart: {count}")
        assert count == 2
        print("Test 2 Passed - 2 items in cart!")

    def test_cart_item_names(self, logged_in_driver):
        products = ProductsPage(logged_in_driver)
        products.add_to_cart("Sauce Labs Backpack")
        time.sleep(2)
        products.click_cart()
        time.sleep(2)
        cart = CartPage(logged_in_driver)
        names = cart.get_item_names()
        print(f"\nItems in cart: {names}")
        assert "Sauce Labs Backpack" in names
        print("Test 3 Passed - Cart item names verified!")

    def test_continue_shopping(self, logged_in_driver):
        products = ProductsPage(logged_in_driver)
        products.add_to_cart("Sauce Labs Backpack")
        time.sleep(2)
        products.click_cart()
        time.sleep(2)
        cart = CartPage(logged_in_driver)
        cart.click_continue_shopping()
        time.sleep(2)
        print(f"\nURL after continue: {logged_in_driver.current_url}")
        assert "inventory" in logged_in_driver.current_url
        print("Test 4 Passed - Continue Shopping works!")

    def test_checkout_button(self, logged_in_driver):
        products = ProductsPage(logged_in_driver)
        products.add_to_cart("Sauce Labs Backpack")
        time.sleep(2)
        products.click_cart()
        time.sleep(2)
        cart = CartPage(logged_in_driver)
        cart.click_checkout()
        time.sleep(2)
        print(f"\nURL after checkout: {logged_in_driver.current_url}")
        assert "checkout-step-one" in logged_in_driver.current_url
        print("Test 5 Passed - Checkout button works!")

    def test_empty_cart(self, logged_in_driver):
        products = ProductsPage(logged_in_driver)
        products.click_cart()
        time.sleep(2)
        cart = CartPage(logged_in_driver)
        count = cart.get_item_count()
        print(f"\nItems in empty cart: {count}")
        assert count == 0
        print("Test 6 Passed - Cart is empty by default!")

    def test_cart_url(self, logged_in_driver):
        products = ProductsPage(logged_in_driver)
        products.click_cart()
        time.sleep(2)
        print(f"\nCart URL: {logged_in_driver.current_url}")
        assert "cart" in logged_in_driver.current_url
        print("Test 7 Passed - Cart URL verified!")