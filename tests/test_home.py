import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest

@pytest.mark.order(3)
class TestHome(BaseTest):

    def test_adding_and_removing_products_in_wishlist(self, driver):
        homepage = HomePage(driver)
        homepage.add_4_products_and_remove_in_wishlists()

    def test_add_to_cat_with_valid_values(self, driver):
        homepage = HomePage(driver)
        homepage.add_to_cart_product()