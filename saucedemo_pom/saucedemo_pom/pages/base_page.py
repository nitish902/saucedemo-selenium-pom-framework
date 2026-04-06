from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def finds(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)

    def click(self, xpath):
        self.find(xpath).click()

    def type(self, xpath, text):
        self.find(xpath).clear()
        self.find(xpath).send_keys(text)

    def get_text(self, xpath):
        return self.find(xpath).text

    def is_visible(self, xpath):
        return self.find(xpath).is_displayed()

    def wait_for(self, xpath):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def get_url(self):
        return self.driver.current_url