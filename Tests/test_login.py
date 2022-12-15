from Tests.test_base import BaseTest
from Pages.login_page import LoginPage
from Config.config import TestData
import pytest
import time
class Test_login(BaseTest):
    @pytest.mark.skip()
    def test_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
    
    def test_right_click(self, request):
        try:
            self.loginpage = LoginPage(self.driver)
            self.loginpage.right_click_forgot_password_link()
        except:
            self.loginpage.take_screenshot(request.node.name)