import pytest
import time
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestEndToEnd:

    def test_complete_purchase_flow(self, driver):
        print("\n" + "═" * 50)
        print("END TO END TEST — Complete Purchase Flow")
        print("═" * 50)

        # ── STEP 1 — Login ────────────────────────────
        print("\n▶ STEP 1: Login")
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")
        time.sleep(3)
        assert "inventory" in driver.current_url
        print("✅ Login successful!")

        # ── STEP 2 — Verify Products Page ─────────────
        print("\n▶ STEP 2: Verify Products Page")
        products = ProductsPage(driver)
        title = products.get_title()
        assert "Products" in title
        count = products.get_product_count()
        assert count == 6
        print(f"✅ Products page loaded — {count} products found!")

        # ── STEP 3 — Add Products to Cart ─────────────
        print("\n▶ STEP 3: Add Products to Cart")
        products.add_to_cart("Sauce Labs Backpack")
        time.sleep(2)
        products.add_to_cart("Sauce Labs Bike Light")
        time.sleep(2)
        badge = products.get_cart_badge()
        assert badge == "2"
        print(f"✅ 2 products added — Cart badge shows {badge}!")

        # ── STEP 4 — Go to Cart ───────────────────────
        print("\n▶ STEP 4: Go to Cart")
        products.click_cart()
        time.sleep(2)
        cart = CartPage(driver)
        cart_title = cart.get_title()
        assert "Your Cart" in cart_title
        item_count = cart.get_item_count()
        assert item_count == 2
        names = cart.get_item_names()
        print(f"✅ Cart page opened — {item_count} items in cart!")
        print(f"   Items: {names}")

        # ── STEP 5 — Checkout Step 1 ──────────────────
        print("\n▶ STEP 5: Checkout — Fill Details")
        cart.click_checkout()
        time.sleep(2)
        assert "checkout-step-one" in driver.current_url
        checkout = CheckoutPage(driver)
        checkout.fill_details("Rahul", "Sharma", "110001")
        time.sleep(2)
        assert "checkout-step-two" in driver.current_url
        print("✅ Checkout details filled!")

        # ── STEP 6 — Verify Order Summary ─────────────
        print("\n▶ STEP 6: Verify Order Summary")
        total = checkout.get_total()
        print(f"   Order Total: {total}")
        assert "Total:" in total
        print("✅ Order summary verified!")

        # ── STEP 7 — Place Order ──────────────────────
        print("\n▶ STEP 7: Place Order")
        checkout.click_finish()
        time.sleep(3)
        confirmation = checkout.get_confirmation()
        print(f"   Confirmation: {confirmation}")
        assert "Thank you" in confirmation
        print("✅ Order placed successfully!")

        print("\n" + "═" * 50)
        print("🎉 END TO END TEST PASSED!")
        print("═" * 50)

    def test_login_and_logout_flow(self, driver):
        print("\n" + "═" * 50)
        print("END TO END TEST — Login and Logout Flow")
        print("═" * 50)

        # Login
        print("\n▶ STEP 1: Login")
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")
        time.sleep(3)
        assert "inventory" in driver.current_url
        print("✅ Login successful!")

        # Verify products page
        print("\n▶ STEP 2: Verify on Products Page")
        products = ProductsPage(driver)
        assert "Products" in products.get_title()
        print("✅ Products page loaded!")

        # Logout
        print("\n▶ STEP 3: Logout")
        products.logout()
        time.sleep(3)
        assert "inventory" not in driver.current_url
        print("✅ Logout successful!")

        # Verify back on login page
        print("\n▶ STEP 4: Verify Back on Login Page")
        assert "saucedemo.com" in driver.current_url
        print("✅ Back on login page!")

        print("\n" + "═" * 50)
        print("🎉 LOGIN LOGOUT TEST PASSED!")
        print("═" * 50)

    def test_failed_login_then_success(self, driver):
        print("\n" + "═" * 50)
        print("END TO END TEST — Failed Login then Success")
        print("═" * 50)

        login = LoginPage(driver)
        login.open()

        # Try wrong credentials first
        print("\n▶ STEP 1: Try Wrong Credentials")
        login.login("wrong_user", "wrong_pass")
        time.sleep(2)
        error = login.get_error_message()
        assert "do not match" in error
        print(f"✅ Error shown: {error}")

        # Now login correctly
        print("\n▶ STEP 2: Login with Correct Credentials")
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()
        time.sleep(3)
        assert "inventory" in driver.current_url
        print("✅ Login successful after retry!")

        print("\n" + "═" * 50)
        print("🎉 FAILED THEN SUCCESS TEST PASSED!")
        print("═" * 50)