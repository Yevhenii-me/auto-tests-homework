from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.config import LOCATORS, USERNAME, PASSWORD
from utils.logger import logger

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        logger.info("LoginPage initialized.")

    def open_login_modal(self):
        """Ensure the login modal is open before proceeding."""
        try:
            logger.info("Checking if login modal is open...")
            modal = self.wait_for_element_visible(LOCATORS["login"]["LOGIN_MODAL"])
            if modal.is_displayed():
                logger.info("✅ Login modal is already open.")
                return
        except:
            logger.warning("⚠️ Login modal is not open. Clicking login button.")
            self.click_element(LOCATORS["login"]["LOGIN_BUTTON_NAV"])

        self.wait_for_element_visible(LOCATORS["login"]["USERNAME_INPUT"])
        logger.info("✅ Login modal is now fully open.")

    def login(self, username=USERNAME, password=PASSWORD):
        """Logs in using the given username and password (defaults from config)."""
        logger.info("🔐 Attempting login with username: %s", username)
        self.open_login_modal()  # Ensure modal is open first
        self.enter_text(LOCATORS["login"]["USERNAME_INPUT"], username)
        self.enter_text(LOCATORS["login"]["PASSWORD_INPUT"], password)
        self.click_element(LOCATORS["login"]["LOGIN_SUBMIT_BUTTON"])
        logger.info("📩 Submitted login form.")

    def is_login_modal_present(self):
        """Checks if the login modal is visible."""
        modal_present = self.is_element_present(LOCATORS["login"]["LOGIN_MODAL"])
        logger.info("Login modal present: %s", modal_present)
        return modal_present

    def is_logout_button_present(self):
        """Checks if the logout button is visible, meaning login was successful."""
        logout_present = self.is_element_present(LOCATORS["login"]["LOGOUT_BUTTON"])
        logger.info("Logout button present (login success): %s", logout_present)
        return logout_present
