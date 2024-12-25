import os
from datetime import datetime

# from faker.providers.date_time import datetime_to_timestamp
# from openpyxl.styles.builtins import title
# from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v129.page import Screenshot

class Login_page:
    username_xpath = (By.XPATH,"//input[@id='user-name']")
    password_xpath = (By.XPATH,"//input[@id='password']")
    login_xpath = (By.XPATH,"//input[@id='login-button']")

    def __init__(self,driver):

        self.driver = driver

    def enter_username(self,name):
        self.driver.find_element(*Login_page.username_xpath).send_keys(name)

    def enter_password(self,password):
        self.driver.find_element(*Login_page.password_xpath).send_keys(password)

    def click_loginbtn(self):
        self.driver.find_element(*Login_page.login_xpath).click()

    def take_screenshot(self,test_name):
        screenshot = r"C:\Users\Admin\OneDrive\Desktop\Swag Labs\screenShots"
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(screenshot,f"{test_name}_{timestamp}.png")
        #save screenshot
        self.driver.save_screenshot(file_path)
        print(f"Screenshot saved at : {file_path}")