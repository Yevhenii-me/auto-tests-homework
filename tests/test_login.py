import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import BASE_URL, USERNAME, PASSWORD
from utils.logger import logger


@pytest.fixture
def driver():
    """Setup and teardown for WebDriver."""
    logger.info("🚀 Initializing WebDriver for login test...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    logger.info("🛑 Quitting WebDriver...")
    driver.quit()


def test_login_valid_credentials(driver):
    """Test login with valid credentials."""
    logger.info("🔐 Running test: Login with valid credentials")

    login_page = LoginPage(driver)

    # Open website
    logger.info("🌍 Opening website: %s", BASE_URL)
    login_page.open_url(BASE_URL)

    # Ensure modal opens first
    logger.info("📌 Opening login modal...")
    login_page.open_login_modal()
    assert login_page.is_login_modal_present(), "❌ Login modal did not appear"
    logger.info("✅ Login modal appeared.")

    # Attempt login using credentials from config.py
    logger.info("🔑 Attempting login with username: %s", USERNAME)
    login_page.login(USERNAME, PASSWORD)

    assert login_page.is_logout_button_present(), "❌ Login failed"
    logger.info("✅ Login successful.")
