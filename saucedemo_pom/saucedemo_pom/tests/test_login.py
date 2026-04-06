import pytest
from pages.login_page import LoginPage

class TestLogin:

    def test_page_title(self, driver):
        login = LoginPage(driver)
        login.open()
        assert "Swag Labs" in driver.title
        print("\nTest 1 Passed - Login page title verified!")

    def test_wrong_credentials(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("wrong_user", "wrong_pass")
        error = login.get_error_message()
        print(f"\nError: {error}")
        assert "do not match" in error
        print("Test 2 Passed - Wrong credentials error verified!")

    def test_empty_username(self, driver):
        login = LoginPage(driver)
        login.open()
        login.click_login()
        error = login.get_error_message()
        print(f"\nError: {error}")
        assert "Username is required" in error
        print("Test 3 Passed - Empty username error verified!")

    def test_empty_password(self, driver):
        login = LoginPage(driver)
        login.open()
        login.enter_username("standard_user")
        login.click_login()
        error = login.get_error_message()
        print(f"\nError: {error}")
        assert "Password is required" in error
        print("Test 4 Passed - Empty password error verified!")

    def test_successful_login(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")
        assert "inventory" in driver.current_url
        print("\nTest 5 Passed - Login successful!")