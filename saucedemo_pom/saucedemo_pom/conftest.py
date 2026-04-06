import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


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

    driver.implicitly_wait(5)

    yield driver

    driver.quit()
