import os
from selenium.webdriver.common.by import By

# Base URL
BASE_URL = "https://www.demoblaze.com/"

# User Credentials (stored securely via environment variables, but with fallback)
USERNAME = os.getenv("TEST_USERNAME", "antogonist")
PASSWORD = os.getenv("TEST_PASSWORD", "adminadmin")

# Locators
LOCATORS = {
    "login": {
        "LOGIN_BUTTON_NAV": (By.ID, "login2"),
        "LOGIN_MODAL": (By.ID, "logInModal"),
        "USERNAME_INPUT": (By.ID, "loginusername"),
        "PASSWORD_INPUT": (By.ID, "loginpassword"),
        "LOGIN_SUBMIT_BUTTON": (By.XPATH, "//button[text()='Log in']"),
        "LOGOUT_BUTTON": (By.ID, "logout2"),
    },
    "cart": {
        "CART_LINK": (By.ID, "cartur"),
        "CART_ITEMS": (By.XPATH, "//tbody/tr"),
        "DELETE_BUTTON": (By.XPATH, "//a[text()='Delete']"),
        "EMPTY_CART_MESSAGE": (By.XPATH, "//h2[text()='Products']"),
    },
    "product": {
        "FIRST_PRODUCT": (By.XPATH, "//a[contains(text(),'Samsung galaxy s6')]"),
        "ADD_TO_CART_BUTTON": (By.XPATH, "//a[text()='Add to cart']"),
    },
}
