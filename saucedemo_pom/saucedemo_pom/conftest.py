import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():

    chrome_options = Options()

    chrome_options.add_argument("--headless")

    chrome_options.add_argument("--window-size=1920,1080")

    chrome_options.add_argument("--disable-gpu")

    chrome_options.add_argument("--no-sandbox")

    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.implicitly_wait(10)

    yield driver

    driver.quit()


@pytest.fixture
def logged_in_driver(driver):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login("standard_user", "secret_sauce")

    return driver
