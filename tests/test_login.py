import pytest

from pages.login_page import LoginPage
from tests.base_test import BaseTest
@pytest.mark.skip
#@pytest.mark.order(1)
class TestLogin(BaseTest):

    def test_login_without_email_and_password(self, driver):
        loginpage = LoginPage(driver)
        loginpage.verify_login_without_email_and_password()

    def test_login_without_email(self, driver):
        loginpage = LoginPage(driver)
        loginpage.verify_login_without_email()

    def test_login_without_password(self, driver):
        loginpage = LoginPage(driver)
        loginpage.verify_login_without_password()

    def test_login_with_invalid_credentials(self, driver):
        loginpage = LoginPage(driver)
        loginpage.verify_login_with_invalid_credentials()

    def test_login_with_valid_credentials(self, driver):
        loginpage = LoginPage(driver)
        loginpage.verify_login_with_valid_credentials()