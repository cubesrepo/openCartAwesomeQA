import time

from faker import Faker

import test_data
from pages.base_page import BasePage


class RegisterPage(BasePage):

    def go_to_register_page(self):
        time.sleep(2)

        #check page title
        assert self.title_is("Your Store")

        #click myaccount
        my_account = self.wait_clickable(test_data.homepage.MY_ACCOUNT)
        self.action_click(my_account)

        time.sleep(0.5)

        register = self.wait_clickable(test_data.homepage.REGISTER)
        self.action_click(register)

    def verify_register_without_inputting_all_fields(self):

        #call the go_to_register_page
        self.go_to_register_page()

        time.sleep(2)

        assert self.url_is("https://awesomeqa.com/ui/index.php?route=account/register")
        assert self.title_is("Register Account")

        #scroll down
        self.scroll_by_amount(0, 100)

        time.sleep(0.5)

        continue_btn = self.wait_clickable(test_data.register.CONTINUE)
        continue_btn.click()
        time.sleep(1)


        assert  self.get_text(test_data.register.ERROR_MESSAGE) in "Warning: You must agree to the Privacy Policy!"
        assert self.wait_visibility(test_data.register.FIRST_NAME_VALIDATION)
        assert self.wait_visibility(test_data.register.LAST_NAME_VALIDATION)
        assert self.wait_visibility(test_data.register.EMAIL_VALIDATION)
        assert self.wait_visibility(test_data.register.PHONE_VALIDATION)
        assert self.wait_visibility(test_data.register.PASSWORD_VALIDATION)

    def verify_register_with_existing_account(self):
        time.sleep(2)

        fake = Faker()

        # input firstname
        firstnamevalue = fake.first_name()
        self.send_keys(test_data.register.FIRST_NAME, firstnamevalue)
        time.sleep(0.5)

        # input lastname
        lastnamevalue = fake.last_name()
        self.send_keys(test_data.register.LAST_NAME, lastnamevalue)
        time.sleep(0.5)

        # input email
        self.send_keys(test_data.register.EMAIL, test_data.EMAIL)
        time.sleep(0.5)

        # input telephone number
        telephonevalue = fake.numerify("##########")
        self.send_keys(test_data.register.TELEPHONE, telephonevalue)
        time.sleep(0.5)

        # input password
        self.send_keys(test_data.register.PASSWORD, test_data.PASSWORD)
        time.sleep(0.5)

        # confirm password
        self.send_keys(test_data.register.CONFIRM_PASSWORD, test_data.PASSWORD)
        time.sleep(0.5)

        # click agree privacy
        privacy_policy = self.wait_clickable(test_data.register.PRIVACY_POLICY)
        privacy_policy.click()

        # click continue
        continue_btn = self.wait_clickable(test_data.register.CONTINUE)
        continue_btn.click()

        time.sleep(1)

        assert self.get_text(test_data.register.ERROR_MESSAGE) in "Warning: E-Mail Address is already registered!"

    def verify_valid_register(self):
        time.sleep(2)

        fake = Faker()

        #input firstname
        firstnamevalue = fake.first_name()
        firstname = self.wait_visibility(test_data.register.FIRST_NAME)
        self.action_clear_and_send_keys(firstname, firstnamevalue)
        time.sleep(0.5)

        # input lastname
        lastnamevalue = fake.last_name()
        lastname = self.wait_visibility(test_data.register.LAST_NAME)
        self.action_clear_and_send_keys(lastname, lastnamevalue)
        time.sleep(0.5)

        # input email
        emailvalue = fake.email()
        email = self.wait_visibility(test_data.register.EMAIL)
        self.action_clear_and_send_keys(email, emailvalue)
        time.sleep(0.5)

        #input telephone number
        telephonevalue = fake.numerify("##########")
        telephone = self.wait_visibility(test_data.register.TELEPHONE)
        self.action_clear_and_send_keys(telephone, telephonevalue)
        time.sleep(0.5)

        # input password
        password = self.wait_visibility(test_data.register.PASSWORD)
        self.action_clear_and_send_keys(password, test_data.PASSWORD)
        time.sleep(0.5)

        # confirm password
        confirm_password = self.wait_visibility(test_data.register.CONFIRM_PASSWORD)
        self.action_clear_and_send_keys(confirm_password, test_data.PASSWORD)
        time.sleep(0.5)

        # click continue
        continue_btn = self.wait_clickable(test_data.register.CONTINUE)
        time.sleep(0.5)
        continue_btn.click()

        time.sleep(1)
        try:
            assert self.title_is("Your Account Has Been Created!")
            assert self.url_is("https://awesomeqa.com/ui/index.php?route=account/success")

            continue_created_btn = self.wait_clickable(test_data.register.CONTINUE_CREATED_BTN)
            self.action_click(continue_created_btn)

            time.sleep(1)

            assert self.url_is("https://awesomeqa.com/ui/index.php?route=account/account")
            assert self.title_is("My Account")

            home = self.wait_clickable(test_data.register.HOME)
            self.action_click(home)
        except:
            if "Warning: You must agree to the Privacy Policy!" in self.get_text(test_data.register.ERROR_MESSAGE):
                self.scroll_by_amount(0, 300)
                time.sleep(0.5)

                self.wait_clickable(test_data.register.PRIVACY_POLICY).click()

                time.sleep(0.5)

                # click continue
                continue_btn = self.wait_clickable(test_data.register.CONTINUE)
                continue_btn.click()

                time.sleep(1)

                assert self.title_is("Your Account Has Been Created!")
                assert self.url_is("https://awesomeqa.com/ui/index.php?route=account/success")

                continue_created_btn = self.wait_clickable(test_data.register.CONTINUE_CREATED_BTN)
                self.action_click(continue_created_btn)

                time.sleep(1)

                assert self.url_is("https://awesomeqa.com/ui/index.php?route=account/account")
                assert self.title_is("My Account")

                home = self.wait_clickable(test_data.register.HOME)
                self.action_click(home)






