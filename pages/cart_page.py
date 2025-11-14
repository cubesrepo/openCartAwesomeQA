import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities import test_data


class CartPage(BasePage):
    def click_home_icon(self):
        self.wait_clickable(test_data.homepage.HOME_ICON).click()
    def click_phone_and_pda(self):
        self.wait_clickable(test_data.homepage.PHONE_AND_PDA).click()
    def get_success_add_to_cart_message(self):
        return self.get_text(test_data.homepage.SUCCESS_YOU_HAVE_ADDED)
    def get_cart_total(self):
        return self.get_text(test_data.homepage.CART_TOTAL_BTN).strip()
    def click_cart_total_btn(self):
        self.wait_clickable(test_data.homepage.CART_TOTAL_BTN).click()
    def get_subtotal(self, sub_total_price):
        SUB_TOTAL = By.XPATH, f"//td[normalize-space()='{sub_total_price}']"
        text = self.get_text(SUB_TOTAL)
        return text
    def get_total(self, total_price):
        TOTAL = By.XPATH, f"//td[normalize-space()='{total_price}']"
        text = self.get_text(TOTAL)
        return text
    def click_add_to_cart_phone(self):
        success_message = []
        for i in range(1, 4):
            locator = By.XPATH, f"(//span[contains(text(),'Add to Cart')])[{i}]"
            self.scroll_to_element(locator)
            self.wait_clickable(locator).click()
            time.sleep(1)
            text = self.get_success_add_to_cart_message()
            success_message.append(text)
    def click_remove_item(self):
        for i in range(1,4):
            time.sleep(0.5)
            REMOVE_ITEM = By.XPATH, f"(//button[@title='Remove'])[1]"
            self.wait_clickable(REMOVE_ITEM).click()
            self.click_cart_total_btn()
    def click_wish_list(self):
        for i in range(2, 5):
            WISH_LIST = By.XPATH, f"(//i[@class='fa fa-heart'])[{i}]"
            self.scroll_to_element(WISH_LIST)
            self.wait_clickable(WISH_LIST).click()
    def click_wish_list_menu(self, total):
        wish_list = By.XPATH, f"//span[normalize-space()='Wish List ({total})']"
        self.wait_clickable(wish_list).click()
    def get_wish_list(self, total_wishlist):
        wish_list = By.XPATH, f"//span[normalize-space()='Wish List ({total_wishlist})']"
        text = self.get_text(wish_list)
        return text
    def get_success_modified_wishlist(self):
        return self.get_text(test_data.wishlist.SUCCESS_MODIFIED_WISHLIST)
    def get_wishlist_empty(self):
        return self.get_text(test_data.wishlist.WISH_LIST_EMPTY).strip()
    def click_remove_wish_list(self):
        expected_text = "Success: You have modified your wish list!"

        for i in range(1, 4):
            time.sleep(0.5)
            self.wait_clickable(test_data.wishlist.REMOVE_WISHLIST).click()
            current_text = self.get_success_modified_wishlist()
            cleaned_text = current_text.replace('×', '')
            if cleaned_text.strip() != expected_text.strip():
                raise ValueError(f"The current text: {cleaned_text} does not match with {expected_text}")

    def verify_total_added_to_cart_phone(self):
        self.click_home_icon()
        self.click_phone_and_pda()
        self.click_add_to_cart_phone()

        total = self.get_cart_total()
        subtotal_price = "$480.99"
        total_price = "$583.19"

        if total != "3 item(s) - $583.19":
            raise ValueError(f"Invalid total: {total}")

        self.click_cart_total_btn()

        current_result_subtotal, current_result_total = self.get_subtotal(subtotal_price), self.get_total(total_price)

        return str(current_result_subtotal).strip(), str(current_result_total).strip()

    def verify_cart_empty_after_removing_items(self):
        self.click_phone_and_pda()
        self.click_add_to_cart_phone()
        self.click_cart_total_btn()
        self.click_remove_item()
        self.click_cart_total_btn()
        current_result_cart_empty = self.get_text(test_data.cart.CART_EMPTY)

        return current_result_cart_empty.strip()


    def verify_add_to_wishlist(self):
        self.click_phone_and_pda()
        self.click_wish_list()
        current_result_wishlist_count = self.get_wish_list("3")

        return current_result_wishlist_count.strip()

    def verify_remove_wishlist(self):
        self.click_phone_and_pda()
        self.click_wish_list()
        self.click_wish_list_menu("3")
        self.click_remove_wish_list()

        current_result_wishlist_empty = self.get_wishlist_empty()

        return current_result_wishlist_empty




