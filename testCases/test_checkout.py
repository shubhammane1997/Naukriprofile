import  os.path

import time

from pageObjects.Checkout_Page import checkOut_page
from pageObjects.Login_Page import Login_page

class TestCheckout:

    def test_checkout_page(self,setup):
        self.driver = setup
        self.cp = checkOut_page(self.driver)
        #for log in

        self.lp = Login_page(self.driver)
        self.lp.enter_username('standard_user')
        self.lp.enter_password('secret_sauce')
        self.lp.click_loginbtn()


        # go for shopping


        self.cp.click_backpack()

        self.cp.click_backaddtocart()

        self.cp.click_gotocart()

        self.cp.click_continueshoping()

        self.cp.click_bikelight()

        self.cp.click_bikelightaddtocart()

        self.cp.click_backtoproduct()

        self.cp.click_bolttshirtaddtocart()

        self.cp.click_jacketaddtocart()

        self.cp.click_onesie()

        self.cp.click_removeonesie()

        self.cp.click_onesie1()

        self.cp.click_RedTshirtaddtocart()

        self.cp.click_gotocart1()

        self.cp.click_checkoutbtn()

        self.cp.enter_firstname('shubham')

        self.cp.enter_lastname('good')

        self.cp.enter_zipcode('455008')

        self.cp.click_canclecheck()

        self.cp.click_checkout()

        self.cp.enter_firstname('shubham')

        self.cp.enter_lastname('good')

        self.cp.enter_zipcode('455008')

        self.cp.click_continue()

        self.cp.click_lastcheckoutbtncancle()

        self.cp.click_gocart2()

        self.cp.click_checkout1()




        self.cp.enter_firstname('shubham')
        time.sleep(2)
        self.cp.enter_lastname('good')
        time.sleep(2)
        self.cp.enter_zipcode('455008')
        time.sleep(2)

        self.cp.click_continue()
        time.sleep(2)



        self.cp.click_finish()
        time.sleep(5)


        self.cp.take_screenshot("checkout_page")

        self.cp.click_back()