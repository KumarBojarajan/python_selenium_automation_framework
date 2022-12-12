from Tests.test_base import BaseTest
from Pages.login_page import LoginPage
from Config.config import TestData
class Test_login(BaseTest):
    def test_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)