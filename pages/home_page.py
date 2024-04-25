import time

from pynput.keyboard import Controller, Key
from selenium.webdriver.common.by import By

import test_data
from pages.base_page import BasePage


class HomePage(BasePage):

    def add_4_products_and_remove_in_wishlists(self):
        time.sleep(2)
        #scroll down
        self.scroll_by_amount(0, 500)

        time.sleep(0.5)

        #loop for adding 4 products in wishlists
        for products in range(2, 6):
            WISH_LIST_ICON = By.XPATH, f"(//i[@class='fa fa-heart'])[{products}]"
            wishlist_icon = self.wait_clickable(WISH_LIST_ICON)
            self.action_click(wishlist_icon)
            time.sleep(0.5)
            self.scroll_by_amount(0, 500)
            time.sleep(0.5)
        assert self.get_text(test_data.homepage.WISH_LIST_BADGE) in "Wish List (4)"

        #click wishlisht menu
        wishlist_badge = self.wait_clickable(test_data.homepage.WISH_LIST_BADGE)
        self.action_click(wishlist_badge)

        time.sleep(2)

        assert self.url_is("https://awesomeqa.com/ui/index.php?route=account/wishlist")
        assert self.title_is("My Wish List")
        #assert if all 4 products are dspaly
        assert self.wait_visibility(test_data.wishlisht.PRODUCT_NAME_MACBOOK)
        assert self.wait_visibility(test_data.wishlisht.PRODUCT_NAME_IPHONE)
        assert self.wait_visibility(test_data.wishlisht.PRODUCT_NAME_APPLE)
        assert self.wait_visibility(test_data.wishlisht.PRODUCT_NAME_CANON)

        #remove all products in wishlists
        for i in range(1, 5):
            x = By.XPATH, f"(//a[@data-original-title='Remove'])[{i}]"
            xclick = self.wait_clickable(x)
            self.action_click(xclick)
            time.sleep(0.1)

        self.driver.refresh()
        time.sleep(1)

        #assert displaying for empty wishlist message
        assert self.wait_visibility(test_data.wishlisht.EMPTY_WISHLIST)

        time.sleep(1)
        #click home
        home = self.wait_clickable(test_data.register.HOME)
        self.action_click(home)

    def add_to_cart_product(self):
        time.sleep(2)
        #scroll down
        self.scroll_by_amount(0, 500)

        #addtocart 3rd product
        add_to_cart_btn_3 = self.wait_clickable(test_data.homepage.ADD_TO_CART_BTN_3)
        self.action_click(add_to_cart_btn_3)

        time.sleep(0.5)
        #scroll down
        self.scroll_by_amount(0, 100)

        #click radio button medium
        medium = self.wait_clickable(test_data.homepage.MEDIUM)
        self.action_click(medium)

        time.sleep(0.5)
        #click all checkbox
        for i in range(8, 12):
            cb = By.XPATH, f"//input[@type='checkbox' and @value= '{i}']"
            checkbox = self.wait_clickable(cb)
            self.action_click(checkbox)

        time.sleep(0.5)
        #input text
        text = self.wait_visibility(test_data.homepage.TEXT)
        self.action_clear_and_send_keys(text, "text sample text sample text sample")
        self.scroll_by_amount(0, 100)
        time.sleep(0.5)

        #select color
        selectbtn = self.wait_clickable(test_data.homepage.SELECT)
        self.select_by_index(selectbtn, 2)

        #input textarae
        time.sleep(0.5)
        textarea = self.wait_visibility(test_data.homepage.TEXTAREA)
        self.action_clear_and_send_keys(textarea, "textarea testing textarea")

        time.sleep(0.5)
        self.scroll_by_amount(0, 100)

        #upload file
        keyboard = Controller()
        uploadfile = self.wait_clickable(test_data.homepage.UPLOAD_FILE)
        uploadfile.click()
        path = r"C:\Users\Leonard\Downloads\example image.png"
        time.sleep(1)
        keyboard.type(path)
        time.sleep(0.5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        #accept the alert
        self.switch_to_alert_and_accept()
        time.sleep(0.5)

        # input date time
        date_time = self.wait_clickable(test_data.homepage.DATE_AND_TIME)
        self.action_clear_and_send_keys(date_time, "2024-05-20 22:25")

        #scroll down
        time.sleep(0.5)
        self.scroll_by_amount(0, 70)

        #input quantity
        quantity = self.wait_visibility(test_data.homepage.QUANTITY)
        self.action_clear_and_send_keys(quantity, "2")
        time.sleep(0.5)

        #click add to cart
        add_to_cart_btn  = self.wait_clickable(test_data.homepage.ADDT_TO_CART_BTN)
        self.action_click(add_to_cart_btn)

        time.sleep(1)
        #assertion of success message
        assert "Success: You have added" in self.get_text(test_data.homepage.SUCCESS_YOU_HAVE_ADDED)
        assert self.get_text(test_data.homepage.PRODUCT_TITLE) in self.get_text(test_data.homepage.SUCCESS_PRODUCT)

        time.sleep(0.5)
        #click home
        home = self.wait_clickable(test_data.register.HOME)
        self.action_click(home)

        time.sleep(0.5)
        self.driver.refresh()
        time.sleep(0.5)

        self.check_add_to_cart_total_and_proceed_to_checkout()


    def check_add_to_cart_total_and_proceed_to_checkout(self):
        time.sleep(2)

        #assert if correct total addto cart
        assert "2 item(s) - $515.20" in self.get_text(test_data.homepage.CART_TOTAL)

        time.sleep(1)

        #click addtocart btn
        cart_total_bnt = self.wait_clickable(test_data.homepage.CART_TOTAL_BTN)
        self.action_click(cart_total_bnt)

        #click checkout btn
        time.sleep(0.5)
        checkout_btn = self.wait_clickable(test_data.homepage.CHECKOUT)
        self.action_click(checkout_btn)