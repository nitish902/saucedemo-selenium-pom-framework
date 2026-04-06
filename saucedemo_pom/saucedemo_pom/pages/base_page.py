from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    BASE_URL = "https://www.saucedemo.com/"

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)


    def open(self, url=""):

        self.driver.get(self.BASE_URL + url)


    def find(self, locator):

        return self.wait.until(

            EC.presence_of_element_located(locator)

        )


    def finds(self, locator):

        return self.wait.until(

            EC.presence_of_all_elements_located(locator)

        )


    def click(self, locator):

        self.wait.until(

            EC.element_to_be_clickable(locator)

        ).click()


    def type(self, locator, text):

        element = self.find(locator)

        element.clear()

        element.send_keys(text)


    def get_text(self, locator):

        return self.find(locator).text
