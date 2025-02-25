from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Correct Locators
    LOGIN_BUTTON_NAV = (By.ID, "login2")
    LOGIN_MODAL = (By.ID, "logInModal")
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Log in']")
    LOGOUT_BUTTON = (By.ID, "logout2")

    def __init__(self, driver):
        super().__init__(driver)

    def open_login_modal(self):
        """Make sure the login modal is open before proceeding."""
        try:
            modal = self.wait.until(EC.visibility_of_element_located(self.LOGIN_MODAL))
            if modal.is_displayed():
                print("Login modal is already open.")
                return
        except:
            print("Login modal is not open. Clicking login button.")
            self.click_element(self.LOGIN_BUTTON_NAV)

        self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))
        print("Login modal is now fully open.")

    def login(self, username, password):
        """Logs in using the given username and password."""
        self.open_login_modal()  # Ensure modal is open first
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_SUBMIT_BUTTON)

    def is_login_modal_present(self):
        """Checks if the login modal is visible."""
        return self.is_element_present(self.LOGIN_MODAL)

    def is_logout_button_present(self):
        """Checks if the logout button is visible, meaning login was successful."""
        return self.is_element_present(self.LOGOUT_BUTTON)
