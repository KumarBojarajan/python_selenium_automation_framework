from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
"""This class is the parent of all the pages"""
"""It contains all the generic methods and utilities for all the pages"""

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)
    
    def do_find_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element
    
    def do_click(self, locator):
        self.do_find_element(locator).click()
    
    def do_send_keys(self, locator, text):
        self.do_find_element(locator).send_keys(text)
    
    def get_element_text(self, locator):
        element = self.do_find_element(locator)
        return element.text
    
    def is_enabled(self, locator):
        element = self.do_find_element(locator)
        return bool(element)
    
    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return title
    
    def do_select(self, locator, value):
        select_class_obj = Select(self.do_find_element(locator))
        select_class_obj.select_by_value(value)
    
    def do_double_click(self, locator):
        element = self.do_find_element(locator)
        self.action.double_click(element)
    
    def do_right_click(self, locator):
        element = self.do_find_element(locator)
        self.action.context_click(element)
    
    def do_refresh(self):
        self.driver.refresh()
    
    def take_screenshot(self, test_name):
        self.driver.save_screenshot(test_name + '.png')