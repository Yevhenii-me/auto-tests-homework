from pages.base_page import BasePage
from utils.config import LOCATORS
from utils.logger import logger
import time


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        logger.info("ProductPage initialized.")

    def add_first_product_to_cart(self):
        """Clicks on the first product and adds it to the cart."""
        logger.info("🛒 Adding first product to cart...")

        self.click_element(LOCATORS["product"]["FIRST_PRODUCT"])  # Click on product
        logger.info("✅ Clicked on first product.")

        time.sleep(1)  # Wait for product page to load

        self.click_element(LOCATORS["product"]["ADD_TO_CART_BUTTON"])  # Click 'Add to cart'
        logger.info("✅ Clicked 'Add to cart' button.")

        time.sleep(1)  # Wait for confirmation alert

        # Accept the alert popup
        alert = self.driver.switch_to.alert
        alert.accept()
        logger.info("✅ Accepted confirmation alert.")

        time.sleep(1)  # Wait before proceeding
