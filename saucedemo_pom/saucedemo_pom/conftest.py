import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():

    driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def logged_in_driver(driver):

    login = LoginPage(driver)

    login.open()

    login.login("standard_user", "secret_sauce")

    # wait until products visible
    WebDriverWait(driver,10).until(
        EC.visibility_of_element_located(
            (By.XPATH,"//div[@class='inventory_item']")
        )
    )

    return driver