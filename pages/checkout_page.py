import time
import random

from faker import Faker

import test_data
from pages.base_page import BasePage


class CheckoutPage(BasePage):


    def verify_checkout_with_valid_billing_details(self):
        time.sleep(2)
        #check page url and title
        assert self.url_is("https://awesomeqa.com/ui/index.php?route=checkout/checkout")
        assert self.title_is("Checkout")

        self.scroll_by_amount(0, 200)

        fake = Faker()
        #Input first name
        time.sleep(0.5)
        firstnamevalue = fake.first_name()
        self.send_keys(test_data.checkout.FIRSTNAME, firstnamevalue)

        # Input last  name
        time.sleep(0.5)
        lastnamevalue = fake.last_name()
        self.send_keys(test_data.checkout.LASTNAME, lastnamevalue)

        # Input company
        time.sleep(0.5)
        companyvalue = "company"
        self.send_keys(test_data.checkout.COMPANY, companyvalue)

        #input address
        time.sleep(0.5)
        addressavalue = fake.address()
        self.send_keys(test_data.checkout.ADDRESS_1, addressavalue)

        #input city
        time.sleep(0.5)
        cityvalue = fake.city()
        self.send_keys(test_data.checkout.CITY, cityvalue)

        #input postcode
        time.sleep(0.5)
        postcodevalue = random.randint(1000, 2000)
        self.send_keys(test_data.checkout.POST_CODE, postcodevalue)

        #input country
        country = self.wait_clickable(test_data.checkout.SELECT_COUNTRY)
        country.click()
        self.action_click(self.select_by_visible_text(country, "Japan"))

        time.sleep(0.5)
        #input region
        region = self.wait_clickable(test_data.checkout.SELECT_REGION)
        region.click()
        self.action_click(self.select_by_visible_text(region, "Tokyo"))

        time.sleep(0.5)

        self.wait_clickable(test_data.checkout.CONTINUE_ONE).click()

    def verify_checkout_with_valid_delivery_details(self):
        time.sleep(2)
        #click continue
        continue_two = self.wait_clickable(test_data.checkout.CONTINUE_TWO)
        self.action_click(continue_two)

    def verify_checkout_with_valid_delivery_method(self):
        time.sleep(2)

        #Input comment
        comment = self.wait_visibility(test_data.checkout.DELIVARY_METH0D_COMMENT)
        self.action_clear_and_send_keys(comment, "COMMMMMMMMMMMMMMMMMMMMMENT")
        time.sleep(0.5)

        # click continue
        continue_btn = self.wait_clickable(test_data.checkout.CONTINUE_THREE)
        self.action_click(continue_btn)

    def verify_checkout_with_valid_payment_method(self):
        time.sleep(2)
        #click agree privacy policy
        try:
            agree = self.wait_clickable(test_data.checkout.PRIVACY_AGREE)
            self.action_click(agree)
        except:
            self.wait_clickable(test_data.checkout.PRIVACY_AGREE).click()


        time.sleep(0.5)
        #click continue
        continue_btn = self.wait_clickable(test_data.checkout.CONTINUE_FOUR)
        self.action_click(continue_btn)

    def verify_checkout_confirm_order(self):
        time.sleep(2)

        #click confirm order
        self.wait_clickable(test_data.checkout.CONFIRM_ORDER).click()

        time.sleep(0.5)
        #check success message
        assert self.wait_visibility(test_data.checkout.ORDER_HAS_BEEN_PLACE_MESSAGE)
        time.sleep(0.5)

        #click continue
        self.wait_clickable(test_data.checkout.CONTINUE_LAST).click()

