import pytest
from selenium import webdriver
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from utils.config import BASE_URL
from utils.logger import logger


@pytest.fixture
def driver():
    """Setup and teardown for WebDriver."""
    logger.info("🚀 Initializing WebDriver...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    logger.info("🛑 Quitting WebDriver...")
    driver.quit()


def test_add_and_remove_product_from_cart(driver):
    """Test adding a product to the cart and then removing it."""
    logger.info("🛒 Running test: Add and Remove Product from Cart")

    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    # Open DemoBlaze website
    logger.info("🌍 Opening website: %s", BASE_URL)
    product_page.open_url(BASE_URL)

    # Step 1: Add a product to the cart
    logger.info("📌 Adding product to the cart...")
    product_page.add_first_product_to_cart()

    # Step 2: Navigate to cart
    logger.info("🛒 Navigating to cart page...")
    cart_page.go_to_cart()

    # Step 3: Check if product was added successfully
    assert cart_page.is_product_in_cart(), "❌ No product was found in the cart after adding."
    logger.info("✅ Product successfully added to the cart.")

    # Step 4: Delete the product
    logger.info("🗑️ Deleting the product from the cart...")
    cart_page.delete_first_product()

    # Step 5: Verify cart is empty after deletion
    assert cart_page.is_cart_empty(), "❌ Cart is not empty after deleting the product."
    logger.info("✅ Cart is empty after product deletion.")
