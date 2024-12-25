import  os

from datetime import datetime

from selenium.webdriver.common.by import By


class checkOut_page:
    backpack_xpath = (By.XPATH,"//div[normalize-space()='Sauce Labs Backpack']")
    backaddtocart_xpath = (By.XPATH,"//button[@id='add-to-cart']")
    gotocart_xpath = (By.XPATH,"//a[@class='shopping_cart_link']")
    continueshoping_xpath = (By.XPATH,"//button[@id='continue-shopping']")
    bikelight_xpath = (By.XPATH,"//div[normalize-space()='Sauce Labs Bike Light']")
    bikelightaddtocart_xpath = (By.XPATH,"//button[@id='add-to-cart']")
    backtoproduct_xpath = (By.XPATH,"//button[@id='back-to-products']")
    bolttshirtaddtocart_xpath = (By.XPATH,"//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    jacketaddtocart_xpath = (By.XPATH,"//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
    onesie_xpath = (By.XPATH,"//button[@id='add-to-cart-sauce-labs-onesie']")
    removeonesie_xpath = (By.XPATH,"//button[@id='remove-sauce-labs-onesie']")
    onesie_xpath1 = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
    RedTshirtaddtocart_xpath = (By.XPATH,"//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
    gotocart_xpath1 = (By.XPATH, "//a[@class='shopping_cart_link']")
    checkoutbtn_xpath = (By.XPATH,"//button[@id='checkout']")
    firstname_xpath = (By.XPATH,"//input[@id='first-name']")
    lastname_xpath = (By.XPATH,"//input[@id='last-name']")
    zipcode_xpath = (By.XPATH,"//input[@id='postal-code']")
    canclecheckout_xpath = (By.XPATH,"//button[@id='cancel']")
    checkoutbtn_xpath1 = (By.XPATH, "//button[@id='checkout']")
    continuebtn_xpath = (By.XPATH,"//input[@id='continue']")
    lastcheckoutbtncancle_xpath = (By.XPATH,"//button[@id='cancel']")
    gocart2_xpath = (By.XPATH, "//a[@class='shopping_cart_link']")
    checkout_xpath = (By.XPATH, '//*[@id="checkout"]')
    finish_xpath = (By.XPATH,'//*[@id="finish"]')
    back_xpath = (By.XPATH,"//button[@id='back-to-products']")

    def __init__(self,driver):
        self.driver = driver

    def click_backpack(self):
        self.driver.find_element(*checkOut_page.backpack_xpath).click()

    def click_backaddtocart(self):
        self.driver.find_element(*checkOut_page.backaddtocart_xpath).click()

    def click_gotocart(self):
        self.driver.find_element(*checkOut_page.gotocart_xpath).click()

    def click_continueshoping(self):
        self.driver.find_element(*checkOut_page.continueshoping_xpath).click()

    def click_bikelight(self):
        self.driver.find_element(*checkOut_page.bikelight_xpath).click()

    def click_bikelightaddtocart(self):
        self.driver.find_element(*checkOut_page.bikelightaddtocart_xpath).click()

    def click_backtoproduct(self):
        self.driver.find_element(*checkOut_page.backtoproduct_xpath).click()

    def click_bolttshirtaddtocart(self):
        self.driver.find_element(*checkOut_page.bolttshirtaddtocart_xpath).click()

    def click_jacketaddtocart(self):
        self.driver.find_element(*checkOut_page.jacketaddtocart_xpath).click()

    def click_onesie(self):
        self.driver.find_element(*checkOut_page.onesie_xpath).click()

    def click_removeonesie(self):
        self.driver.find_element(*checkOut_page.removeonesie_xpath).click()

    def click_onesie1(self):
        self.driver.find_element(*checkOut_page.onesie_xpath1).click()

    def click_RedTshirtaddtocart(self):
        self.driver.find_element(*checkOut_page.RedTshirtaddtocart_xpath).click()

    def click_gotocart1(self):
        self.driver.find_element(*checkOut_page.gotocart_xpath1).click()

    def click_checkoutbtn(self):
        self.driver.find_element(*checkOut_page.checkoutbtn_xpath).click()

    def enter_firstname(self,name):
        self.driver.find_element(*checkOut_page.firstname_xpath).send_keys(name)

    def enter_lastname(self,lastname):
        self.driver.find_element(*checkOut_page.lastname_xpath).send_keys(lastname)

    def enter_zipcode(self,zip):
        self.driver.find_element(*checkOut_page.zipcode_xpath).send_keys(zip)

    def click_canclecheck(self):
        self.driver.find_element(*checkOut_page.canclecheckout_xpath).click()

    def click_checkout(self):
        self.driver.find_element(*checkOut_page.checkoutbtn_xpath1).click()

    def click_continue(self):
        self.driver.find_element(*checkOut_page.continuebtn_xpath).click()

    def click_lastcheckoutbtncancle(self):
        self.driver.find_element(*checkOut_page.lastcheckoutbtncancle_xpath).click()

    def click_gocart2(self):
        self.driver.find_element(*checkOut_page.gocart2_xpath).click()

    def click_checkout1(self):
        self.driver.find_element(*checkOut_page.checkout_xpath).click()

    def click_finish(self):
        self.driver.find_element(*checkOut_page.finish_xpath).click()

    def click_back(self):
        self.driver.find_element(*checkOut_page.back_xpath).click()

        #screenshot

    def take_screenshot(self, test_name):
        screenshot = r"C:\Users\Admin\OneDrive\Desktop\Swag Labs\screenShots"
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(screenshot, f"{test_name}_{timestamp}.png")
        # save screenshot
        self.driver.save_screenshot(file_path)
        print(f"Screenshot saved at : {file_path}")