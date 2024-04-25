import time

import test_data
from pages.base_page import BasePage


class LoginPage(BasePage):
    def go_to_login_page(self):
        time.sleep(2)

        # click myaccount
        my_account = self.wait_clickable(test_data.homepage.MY_ACCOUNT)
        self.action_click(my_account)

        time.sleep(0.5)

        login = self.wait_clickable(test_data.homepage.LOGIN)
        self.action_click(login)

    def verify_login_without_email_and_password(self):
        time.sleep(2)
        self.go_to_login_page()

        assert self.url_is("https://awesomeqa.com/ui/index.php?route=account/login")
        assert self.title_is("Account Login")

        login_btn = self.wait_clickable(test_data.login.LOGIN)
        self.action_click(login_btn)

        assert self.get_text(test_data.login.ERROR_MESSAGE) in "Warning: No match for E-Mail Address and/or Password."

    def verify_login_without_email(self):
        time.sleep(2)

        #Input password
        self.send_keys(test_data.login.PASSWORD, test_data.PASSWORD)
        time.sleep(0.5)
        #click loginbtn
        login_btn = self.wait_clickable(test_data.login.LOGIN)
        self.action_click(login_btn)

        #check validation erroer message
        assert self.get_text(test_data.login.ERROR_MESSAGE) in "Warning: No match for E-Mail Address and/or Password."

    def verify_login_without_password(self):
        time.sleep(2)

        # Input email
        self.send_keys(test_data.login.EMAIL, test_data.EMAIL)
        time.sleep(0.5)
        # click loginbtn
        login_btn = self.wait_clickable(test_data.login.LOGIN)
        self.action_click(login_btn)

        # check validation error message
        assert self.get_text(test_data.login.ERROR_MESSAGE) in "Warning: No match for E-Mail Address and/or Password."

    def verify_login_with_invalid_credentials(self):
        time.sleep(2)
        # Input email
        self.send_keys(test_data.login.EMAIL, test_data.WRONGEMAIL)

        time.sleep(0.5)
        # Input password
        self.send_keys(test_data.login.PASSWORD, test_data.WRONGPASSWORD)

        time.sleep(0.5)

        # click loginbtn
        login_btn = self.wait_clickable(test_data.login.LOGIN)
        self.action_click(login_btn)

        # check validation error message
        assert self.get_text(test_data.login.ERROR_MESSAGE) in "Warning: No match for E-Mail Address and/or Password."

    def verify_login_with_valid_credentials(self):
        time.sleep(2)
        # Input email
        self.send_keys(test_data.login.EMAIL, test_data.EMAIL)

        time.sleep(0.5)
        # Input password
        self.send_keys(test_data.login.PASSWORD, test_data.PASSWORD)

        time.sleep(0.5)
        # click loginbtn
        login_btn = self.wait_clickable(test_data.login.LOGIN)
        self.action_click(login_btn)

        # check validation error message
        assert self.get_text(test_data.login.ERROR_MESSAGE) in "Warning: No match for E-Mail Address and/or Password."


