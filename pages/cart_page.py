from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.config import LOCATORS
from utils.logger import logger

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)
        logger.info("CartPage initialized.")

    def go_to_cart(self):
        """Navigates to the cart page and waits for the cart to load."""
        logger.info("Navigating to cart page...")
        self.click_element(LOCATORS["cart"]["CART_LINK"])
        self.wait.until(EC.presence_of_element_located(LOCATORS["cart"]["CART_ITEMS"]))
        logger.info("Cart page loaded successfully.")

    def is_product_in_cart(self):
        """Checks if any product is in the cart."""
        logger.info("Checking if product is in cart...")
        is_present = self.is_element_present(LOCATORS["cart"]["CART_ITEMS"])
        logger.info("Product found in cart: %s", is_present)
        return is_present

    def delete_first_product(self):
        """Deletes the first product from the cart and waits for the update."""
        logger.info("Attempting to delete first product from cart...")
        if self.is_product_in_cart():
            self.click_element(LOCATORS["cart"]["DELETE_BUTTON"])
            self.wait.until_not(EC.presence_of_element_located(LOCATORS["cart"]["CART_ITEMS"]))  # Wait until product disappears
            logger.info("Product successfully removed from cart.")
        else:
            logger.warning("No product found in cart to delete.")

    def is_cart_empty(self):
        """Checks if the cart is empty after waiting for the update."""
        is_empty = not self.is_element_present(LOCATORS["cart"]["CART_ITEMS"])
        logger.info("Cart empty: %s", is_empty)
        return is_empty
