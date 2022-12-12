from Tests.test_base import BaseTest
from Pages.login_page import LoginPage
from Config.config import TestData
class Test_Home(BaseTest):
    
    def test_logout(self):
        self.loginpage = LoginPage(self.driver)
        self.home_page_instance = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)      
        self.home_page_instance.logout()