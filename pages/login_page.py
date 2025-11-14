from zipfile import error

from faker import Faker
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities import test_data


class LoginPage(BasePage):
    def click_my_account_menu(self):
        self.wait_clickable(test_data.homepage.MY_ACCOUNT).click()
    def click_register_btn(self):
        self.wait_clickable(test_data.homepage.REGISTER).click()
    def click_login_btn_menu(self):
        self.wait_clickable(test_data.homepage.LOGIN).click()
    def click_continue_btn(self):
        self.wait_clickable(test_data.register.CONTINUE).click()
    def tick_privacy_policy(self):
        self.wait_clickable(test_data.register.PRIVACY_POLICY).click()
    def type_login_email_password(self, email, password):
        self.type(test_data.login.EMAIL, email)
        self.type(test_data.login.PASSWORD, password)
    def click_login_btn(self):
        self.wait_clickable(test_data.login.LOGIN).click()
    def type_personal_details(self, first_name, last_name, email, telephone,
                              password, confirm_password):
        personal_details = {
            test_data.register.FIRST_NAME: first_name,
            test_data.register.LAST_NAME: last_name,
            test_data.register.EMAIL: email,
            test_data.register.TELEPHONE: telephone,
            test_data.register.PASSWORD: password,
            test_data.register.CONFIRM_PASSWORD: confirm_password,
        }
        for locator, value in personal_details.items():
            self.type(locator, value)
    def get_account_created(self):
        return self.get_text(test_data.register.ACCOUNT_HAS_BEEN_CREATED_TEXT)
    def get_all_fields_validation_error(self):
        error_validation = []
        locators = [
            test_data.register.FIRST_NAME_VALIDATION,
            test_data.register.LAST_NAME_VALIDATION,
            test_data.register.EMAIL_VALIDATION,
            test_data.register.PHONE_VALIDATION,
            test_data.register.PASSWORD_VALIDATION
        ]
        for locator in locators:
            text = self.get_text(locator)
            error_validation.append(text)
        return error_validation
    def get_error_warning(self):
        return self.get_text(test_data.register.ERROR_MESSAGE)

    def verify_valid_register(self):
        self.click_my_account_menu()
        self.click_register_btn()
        fake = Faker()
        email = f"test1234{fake.email()}"
        telephone = "12332"
        password = "Password12345!"
        self.type_personal_details(fake.first_name(), fake.first_name(), email,
                                   telephone, password, password)
        self.tick_privacy_policy()
        self.click_continue_btn()

        current_result_account_has_been_created = self.get_account_created()

        return current_result_account_has_been_created, email, password

    def verify_register_with_empty_fields_and_privacy_policy(self):
        self.click_my_account_menu()
        self.click_register_btn()
        self.click_continue_btn()

        current_result_error_message = self.get_all_fields_validation_error()
        current_result_privacy_policy_message = self.get_error_warning()
        return current_result_error_message, current_result_privacy_policy_message.strip()

    def verify_register_with_empty_fields(self):
        self.click_my_account_menu()
        self.click_register_btn()
        self.tick_privacy_policy()
        self.click_continue_btn()

        current_result_error_message = self.get_all_fields_validation_error()
        return current_result_error_message

    def verify_valid_login(self, email, password, menu=True):
        if menu:
            self.click_my_account_menu()
            self.click_login_btn_menu()
        self.type_login_email_password(email, password)
        self.click_login_btn()

        current_result_homepage_url = self.get_url("https://awesomeqa.com/ui/index.php?route=account/account")

        return current_result_homepage_url

    def verify_login_without_email_password(self):
        self.click_my_account_menu()
        self.click_login_btn_menu()
        self.type_login_email_password("", "")
        self.click_login_btn()

        current_result_warning_message = self.get_error_warning()
        return current_result_warning_message.strip()