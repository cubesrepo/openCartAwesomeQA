import pytest

from pages.checkout_page import CheckoutPage
from tests.base_test import BaseTest

@pytest.mark.order(4)
class Testcheckout(BaseTest):

    def test_checkout_with_valid_billing_details(self, driver):
        checkoutpage = CheckoutPage(driver)
        checkoutpage.verify_checkout_with_valid_billing_details()

    def test_checkout_with_valid_delivery_details(self, driver):
        checkoutpage = CheckoutPage(driver)
        checkoutpage.verify_checkout_with_valid_delivery_details()

    def test_checkout_with_valid_delivery_method(self, driver):
        checkoutpage = CheckoutPage(driver)
        checkoutpage.verify_checkout_with_valid_delivery_method()

    def test_checkout_with_valid_payment_method(self, driver):
        checkoutpage = CheckoutPage(driver)
        checkoutpage.verify_checkout_with_valid_payment_method()

    def test_checkout_confirm_order(self, driver):
        checkoutpage = CheckoutPage(driver)
        checkoutpage.verify_checkout_confirm_order()