from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from utils.config import BASE_URL
from utils.logger import logger

class BasePage:
    DEFAULT_TIMEOUT = 10  # Default timeout for waiting operations

    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        """Initialize the base page with a driver and a default timeout."""
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout, ignored_exceptions=[
            NoSuchElementException, StaleElementReferenceException
        ])
        logger.info("BasePage initialized with timeout=%s", timeout)

    def open_url(self, url=BASE_URL):
        """Opens a specified URL."""
        logger.info("Opening URL: %s", url)
        self.driver.get(url)

    def wait_for_element(self, locator, condition=EC.visibility_of_element_located, timeout=DEFAULT_TIMEOUT):
        """Generalized method to wait for an element with a given condition."""
        try:
            logger.info("Waiting for element: %s", locator)
            return WebDriverWait(self.driver, timeout).until(condition(locator))
        except TimeoutException:
            logger.error("Timeout waiting for element: %s", locator)
            return None

    def find_element(self, locator):
        """Finds an element using a locator (By, value) with optimized wait."""
        logger.info("Finding element: %s", locator)
        return self.wait_for_element(locator, EC.presence_of_element_located)

    def click_element(self, locator):
        """Waits for an element to be clickable and clicks it."""
        logger.info("Clicking element: %s", locator)
        element = self.wait_for_element(locator, EC.element_to_be_clickable)
        if element:
            element.click()
            logger.info("Clicked element: %s", locator)
        else:
            logger.error("Element not clickable: %s", locator)
            raise TimeoutException(f"Element {locator} was not clickable.")

    def enter_text(self, locator, text):
        """Waits for an input field, clears it, and enters text."""
        logger.info("Entering text into: %s", locator)
        element = self.wait_for_element(locator, EC.visibility_of_element_located)
        if element:
            element.clear()
            element.send_keys(text)
            logger.info("Entered text into: %s", locator)
        else:
            logger.error("Input field not found: %s", locator)
            raise TimeoutException(f"Input field {locator} was not found.")

    def get_text(self, locator):
        """Gets the text of an element with optimized wait."""
        logger.info("Getting text from element: %s", locator)
        element = self.wait_for_element(locator, EC.visibility_of_element_located)
        if element:
            text = element.text
            logger.info("Text retrieved: %s", text)
            return text
        else:
            logger.error("Failed to get text from element: %s", locator)
            return None

    def is_element_present(self, locator):
        """Checks if an element is present and visible without throwing an exception."""
        logger.info("Checking if element is present: %s", locator)
        return bool(self.wait_for_element(locator, EC.presence_of_element_located, timeout=5))

    def wait_for_element_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        """Waits for an element to be visible on the page."""
        logger.info("Waiting for element to be visible: %s", locator)
        return self.wait_for_element(locator, EC.visibility_of_element_located, timeout)

    def wait_for_element_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        """Waits for an element to be clickable before interacting."""
        logger.info("Waiting for element to be clickable: %s", locator)
        return self.wait_for_element(locator, EC.element_to_be_clickable, timeout)
