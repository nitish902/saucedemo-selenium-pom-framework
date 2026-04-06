import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():

    chrome_options = Options()

    chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--window-size=1920,1080")

    chrome_options.add_argument("--disable-gpu")

    chrome_options.add_argument("--no-sandbox")

    chrome_options.add_argument("--disable-dev-shm-usage")


    driver = webdriver.Chrome(

        service=Service(ChromeDriverManager().install()),

        options=chrome_options

    )

    driver.implicitly_wait(10)


    # always open website
    driver.get("https://www.saucedemo.com")

    # always login before every test
    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")

    login_page.enter_password("secret_sauce")

    login_page.click_login()


    yield driver

    driver.quit()
