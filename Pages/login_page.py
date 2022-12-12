from Config.config import TestData
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Pages.home_page import HomePage
class LoginPage(BasePage):
    
    """Identifiers or web elements of login page"""
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[class*='login-button']")

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()
    
    """Page Actions"""
    def get_login_page_title(self, title):
        return self.get_login_page_title(title)

    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        # returns landing page instance
        return HomePage(self.driver)