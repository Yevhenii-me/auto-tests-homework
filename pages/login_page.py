from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Updated Locators
    LOGIN_BUTTON_NAV = (By.ID, "login2")  # Login button in navbar
    LOGIN_MODAL = (By.ID, "logInModal")  # Login modal
    USERNAME_INPUT = (By.ID, "loginusername")  # Username field
    PASSWORD_INPUT = (By.ID, "loginpassword")  # Password field
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Log in']")  # Login button inside modal
    LOGOUT_BUTTON = (By.ID, "logout2")  # Logout button (visible after login)

    def __init__(self, driver):
        super().__init__(driver)

    def open_login_modal(self):
        """Clicks the login button to open the modal."""
        self.click_element(self.LOGIN_BUTTON_NAV)  # Click login button
        self.wait.until(lambda d: d.find_element(*self.LOGIN_MODAL).is_displayed())  # Wait for modal to be visible

    def login(self, username, password):
        """Logs in using the given username and password."""
        self.open_login_modal()  # Open the modal first
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_SUBMIT_BUTTON)

    def is_login_modal_present(self):
        """Checks if the login modal is visible."""
        return self.is_element_present(self.LOGIN_MODAL)

    def is_logout_button_present(self):
        """Checks if the logout button is visible, meaning login was successful."""
        return self.is_element_present(self.LOGOUT_BUTTON)
