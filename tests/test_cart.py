import pytest

from pages.cart_page import CartPage
from pages.login_page import LoginPage


@pytest.mark.cart
class TestCart:
    @pytest.fixture
    def cart_page(self, driver, delay):
        return CartPage(driver, delay)

    @pytest.fixture
    def login_page(self, driver, delay):
        return LoginPage(driver, delay)
    @pytest.mark.skip
    def test_total_added_to_cart_phone(self, cart_page,login_page):
        current_result_account_has_been_created, email, password = login_page.verify_valid_register()

        current_result_subtotal, current_result_total\
            = cart_page.verify_total_added_to_cart_phone()

        expected_result_subtotal = "$480.99"
        expected_result_total = "$583.19"

        assert current_result_subtotal == expected_result_subtotal, \
            f"Expected result to be {expected_result_subtotal}, but got {current_result_subtotal} instead."

        assert current_result_total == expected_result_total, \
            f"Expected result to be {expected_result_total}, but got {current_result_total} instead."
    @pytest.mark.skip
    def test_cart_empty_after_removing_items(self, cart_page,login_page):
        current_result_account_has_been_created, email, password = login_page.verify_valid_register()
        current_result_cart_empty = cart_page.verify_cart_empty_after_removing_items()

        expected_result_cart_empty = "Your shopping cart is empty!"

        assert current_result_cart_empty == expected_result_cart_empty, \
            f"Expected result to be {expected_result_cart_empty}, but got {current_result_cart_empty} instead."
    @pytest.mark.skip
    def test_add_to_wishlist(self, cart_page,login_page):
        current_result_account_has_been_created, email, password = login_page.verify_valid_register()
        current_result_wishlist_count = cart_page.verify_add_to_wishlist()

        expected_result_wishlist_count = "Wish List (3)"

        assert current_result_wishlist_count == expected_result_wishlist_count, \
            f"Expected result to be {expected_result_wishlist_count}, but got {current_result_wishlist_count} instead."

    def test_remove_wishlist(self, cart_page, login_page):
        current_result_account_has_been_created, email, password = login_page.verify_valid_register()
        current_result_wishlist_empty = cart_page.verify_remove_wishlist()

        expected_result_wishlist_empty  = "Your wish list is empty."

        assert current_result_wishlist_empty == expected_result_wishlist_empty, \
            f"Expected result to be {expected_result_wishlist_empty}, but got {current_result_wishlist_empty} instead."












