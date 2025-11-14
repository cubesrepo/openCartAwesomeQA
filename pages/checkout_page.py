import time

from faker.proxy import Faker
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities import test_data


class CheckoutPage(BasePage):
    def click_checkout(self):
        self.wait_clickable(test_data.cart.CHECKOUT).click()
    def check_dismissible(self):
        return self.get_text(test_data.cart.DISMISSIBLE).strip()
    def click_main_checkout(self):
        self.action_click(test_data.cart.MAIN_CHECKOUT)
    def click_billing_details_continue_btn(self):
        self.wait_clickable(test_data.checkout.BILLING_DETAILS_CONTINUE).click()
    def click_delivery_details_continue_btn(self):
        self.wait_clickable(test_data.checkout.DELIVERY_DETAILS_CONTINUE).click()
    def click_delivery_method_continue_btn(self):
        self.wait_clickable(test_data.checkout.DELIVERY_METHOD_CONTINUE).click()
    def click_payment_method_continue_btn(self):
        self.wait_clickable(test_data.checkout.PAYMENT_METHOD_CONTINUE).click()
    def add_comment_delivery_method(self, value):
        self.type(test_data.checkout.DELIVERY_METH0D_COMMENT, value)
    def click_terms_and_condition(self):
        self.wait_clickable(test_data.checkout.TERMS_CONDITION).click()
    def add_comment_payment_method(self, value):
        self.type(test_data.checkout.PAYMENT_METH0D_COMMENT, value)
    def click_confirm_order(self):
        self.wait_clickable(test_data.checkout.CONFIRM_ORDER).click()
    def get_order_has_been_placed(self):
        return self.get_text(test_data.checkout.ORDER_HAS_BEEN_PLACE_MESSAGE)
    def check_if_star(self):
        time.sleep(1)

        if "Products marked with ***" not in self.check_dismissible():
            return

        count = 11
        for i in range(31, 44, 6):
            locator = (By.XPATH, f"(//td)[{i}]//span[contains(normalize-space(.), '***')]")
            stars = self.driver.find_elements(*locator)

            if stars:
                remove_btn = (By.XPATH, f"(//button[@type='button'])[{count}]")
                self.wait_clickable(remove_btn).click()
            count += 1
    def get_validation_error(self):
        locator = By.XPATH, "//div[contains(text(),'First Name must be between 1 and 32 characters!')]"
        return self.get_text((locator))

    def input_billing_details(self, first_name, last_name, address1, city, post_code, country):
        billing_info = {
            test_data.checkout.FIRSTNAME: first_name,
            test_data.checkout.LASTNAME: last_name,
            test_data.checkout.ADDRESS_1: address1,
            test_data.checkout.CITY: city,
            test_data.checkout.POST_CODE: post_code,
            test_data.checkout.SELECT_COUNTRY: country
        }


        for locator, value in billing_info.items():
            self.action_type(locator, value)

    def verify_valid_checkout(self):
        self.click_checkout()
        self.check_if_star()
        self.click_main_checkout()
        fake = Faker()
        self.input_billing_details(fake.first_name(), fake.first_name(), "Addresss 123", "City",
                                   "512312", "Armenia", )
        self.select_dropdown_value(test_data.checkout.SELECT_REGION, "Rutland", "visible_text")
        self.click_billing_details_continue_btn()
        self.click_delivery_details_continue_btn()
        self.add_comment_delivery_method("Comment delivery method")
        self.click_delivery_method_continue_btn()
        self.add_comment_payment_method("Comment payment method")
        self.click_terms_and_condition()
        self.click_payment_method_continue_btn()
        self.click_confirm_order()

        current_url = self.get_url("https://awesomeqa.com/ui/index.php?route=checkout/success")
        current_result_order_placed = self.get_order_has_been_placed()

        return current_url, current_result_order_placed.strip()

    def verify_checkout_without_billing_details(self):
        self.click_checkout()
        self.check_if_star()
        self.click_main_checkout()
        self.click_billing_details_continue_btn()

        current_result_validation = self.get_validation_error()

        return current_result_validation.strip()



















