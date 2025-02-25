from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log in']")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Log out")
    LOGIN_MODAL = (By.ID, "logInModal")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        """Logs in using the given username and password."""
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def is_login_modal_present(self):
        """Checks if the login modal is visible."""
        return self.is_element_present(self.LOGIN_MODAL)

    def is_logout_button_present(self):
        """Checks if the logout button is visible, indicating a successful login."""
        return self.is_element_present(self.LOGOUT_BUTTON)
