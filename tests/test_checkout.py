from tokenize import Expfloat

import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage


@pytest.mark.checkout
class TestCheckoutPage:
    @pytest.fixture
    def login_page(self, driver, delay):
        return LoginPage(driver, delay)

    @pytest.fixture
    def checkout_page(self, driver, delay):
        return CheckoutPage(driver, delay)

    @pytest.fixture
    def cart_page(self, driver, delay):
        return CartPage(driver, delay)
    @pytest.mark.skip
    def test_valid_checkout(self, login_page, checkout_page, cart_page):
        current_result_account_has_been_created, email, password = login_page.verify_valid_register()

        current_result_subtotal, current_result_total\
            = cart_page.verify_total_added_to_cart_phone()

        current_url, current_result_order_placed = checkout_page.verify_valid_checkout()
        expected_url = "https://awesomeqa.com/ui/index.php?route=checkout/success"
        expected_result_order_placed = "Your order has been placed!"

        assert current_url == expected_url, \
            f"Expected url to be {expected_url}, but got {current_url} instead."

        assert current_result_order_placed == expected_result_order_placed, \
            f"Expected url to be {expected_result_order_placed}, but got {current_result_order_placed} instead."

    def test_checkout_without_billing_details(self, login_page, checkout_page, cart_page):
        current_result_account_has_been_created, email, password = login_page.verify_valid_register()

        current_result_subtotal, current_result_total \
            = cart_page.verify_total_added_to_cart_phone()

        current_result_validation= checkout_page.verify_checkout_without_billing_details()
        expected_result_validation = "First Name must be between 1 and 32 characters!"

        assert current_result_validation == expected_result_validation, \
            f"Expected result to be {expected_result_validation}, but got {current_result_validation} instead."