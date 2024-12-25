import os.path

import time

from pageObjects.Login_Page import Login_page

class TestLogin:

    def test_login_page(self,setup):
        self.driver = setup
        self.lp = Login_page(self.driver)
        self.lp.enter_username('standard_user')
        self.lp.enter_password('secret_sauce')
        self.lp.click_loginbtn()
        # time.sleep(5)
        self.lp.take_screenshot("login_page")