from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        """Opens a specified URL."""
        self.driver.get(url)

    def find_element(self, locator):
        """Finds an element using a locator (By, value)."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        """Clicks on an element."""
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        """Enters text into an input field."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Gets the text of an element."""
        element = self.find_element(locator)
        return element.text

    def is_element_present(self, locator):
        """Checks if an element is present."""
        try:
            self.find_element(locator)
            return True
        except:
            return False
