from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
class HomePage(BasePage):

    """Identifiers or Web elements of home page"""
    DROP_DOWN_MENU = (By.CSS_SELECTOR, "[class*='dropdown-tab']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "[href*='logout']")
    
    """Constructor of home page"""
    def __init__(self, driver):
        super().__init__(driver)
    
    """Homepage Actions"""
    def logout(self):
        self.do_click(self.DROP_DOWN_MENU)
        self.do_click(self.LOGOUT_BUTTON)