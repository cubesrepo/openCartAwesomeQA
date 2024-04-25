import pytest

from pages.register_page import RegisterPage
from tests.base_test import BaseTest

@pytest.mark.order(2)
class TestRegister(BaseTest):

    def test_register_without_inputting_all_fields(self, driver):
        registerpage = RegisterPage(driver)
        registerpage.verify_register_without_inputting_all_fields()

    def test_register_with_existing_accounts(self, driver):
        registerpage = RegisterPage(driver)
        registerpage.verify_register_with_existing_account()

    def test_verify_register_with_valid_values(self, driver):
        registerpage = RegisterPage(driver)
        registerpage.verify_valid_register()
