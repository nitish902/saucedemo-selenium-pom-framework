from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 15)


    def open(self, url):

        self.driver.get(url)


    def find(self, locator):

        return self.wait.until(

            EC.visibility_of_element_located(locator)

        )


    def finds(self, locator):

        return self.wait.until(

            EC.visibility_of_all_elements_located(locator)

        )


    def click(self, locator):

        element = self.wait.until(

            EC.element_to_be_clickable(locator)

        )

        element.click()


    def type(self, locator, text):

        element = self.find(locator)

        element.clear()

        element.send_keys(text)


    def get_text(self, locator):

        return self.find(locator).text
