import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    """Setup and teardown for WebDriver."""
    driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login_valid_credentials(driver):
    """Test login with valid credentials."""
    login_page = LoginPage(driver)
    login_page.open_url("https://www.demoblaze.com/")

    assert login_page.is_login_modal_present(), "Login modal did not appear"

    login_page.login("testuser", "testpassword")

    assert login_page.is_logout_button_present(), "Login failed"