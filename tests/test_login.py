import pytest

from pages.login_page import LoginPage
from utilities import test_data


@pytest.mark.login
class TestLogin:
    @pytest.fixture
    def login_page(self, driver, delay):
        return LoginPage(driver, delay)
    @pytest.mark.skip
    def test_valid_register(self, login_page):
        current_result_account_has_been_created, email, password = login_page.verify_valid_register()
        expected_result_account_has_been_created = "Your Account Has Been Created!"

        assert current_result_account_has_been_created == expected_result_account_has_been_created, \
            f"Expected result to be {expected_result_account_has_been_created}, but got {current_result_account_has_been_created} instead."
    @pytest.mark.skip
    def test_register_with_empty_fields_and_privacy_policy(self, login_page):
        current_result_error_message, current_result_privacy_policy_message = login_page.verify_register_with_empty_fields_and_privacy_policy()

        expected_result_error_validation = ["First Name must be between 1 and 32 characters!",
                            "Last Name must be between 1 and 32 characters!",
                            "E-Mail Address does not appear to be valid!",
                            "Telephone must be between 3 and 32 characters!",
                            "Password must be between 4 and 20 characters!"]

        expected_result_privacy_policy_message = "Warning: You must agree to the Privacy Policy!"

        assert current_result_error_message == expected_result_error_validation, \
            f"Expected result to be {expected_result_error_validation}, but got {current_result_error_message} instead."

        assert current_result_privacy_policy_message == expected_result_privacy_policy_message, \
            f"Expected result to be {expected_result_privacy_policy_message}, but got {current_result_privacy_policy_message} instead."
    @pytest.mark.skip
    def test_register_with_empty_fields(self, login_page):
        current_result_error_message= login_page.verify_register_with_empty_fields()

        expected_result_error_validation = ["First Name must be between 1 and 32 characters!",
                                            "Last Name must be between 1 and 32 characters!",
                                            "E-Mail Address does not appear to be valid!",
                                            "Telephone must be between 3 and 32 characters!",
                                            "Password must be between 4 and 20 characters!"]

        assert current_result_error_message == expected_result_error_validation, \
            f"Expected result to be {expected_result_error_validation}, but got {current_result_error_message} instead."

    @pytest.mark.skip
    def test_valid_login(self, login_page):
        current_result_homepage_url= login_page.verify_valid_login(test_data.EMAIL, test_data.PASSWORD)
        expected_result_homepage_url = "https://awesomeqa.com/ui/index.php?route=account/account"

        assert current_result_homepage_url == expected_result_homepage_url, \
            f"Expected URL to be {expected_result_homepage_url}, but got {current_result_homepage_url} instead."

    def test__login_without_email_password(self, login_page):
        current_result_warning_message = login_page.verify_login_without_email_password()
        expected_messages = [
            "Warning: No match for E-Mail Address and/or Password.",
            "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."
        ]
        assert current_result_warning_message in expected_messages, \
            f"Expected result to be {expected_messages}, but got {current_result_warning_message} instead."




