from selenium.webdriver.common.by import By

BASE_URL = "https://awesomeqa.com/ui/"

EMAIL = "automation@gmail.com"
PASSWORD = "Password123"

WRONGEMAIL = "wrong@gmail.com"
WRONGPASSWORD = "wrongpassword"


class cart:
    CHECKOUT = By.XPATH, "//strong[normalize-space()='Checkout']"
    MAIN_CHECKOUT = By.XPATH, "//a[@class='btn btn-primary']"
    CART_EMPTY = By.XPATH, "//p[@class='text-center']"
    DISMISSIBLE = By.XPATH, "//div[@class='alert alert-danger alert-dismissible']"
class wishlist:
    SUCCESS_MODIFIED_WISHLIST = By.XPATH, "//div[@class='alert alert-success alert-dismissible']"
    WISH_LIST_EMPTY =By.XPATH, "//p[normalize-space()='Your wish list is empty.']"
    REMOVE_WISHLIST = By.XPATH, "(//a[@class='btn btn-danger'])[1]"
class homepage:
    PHONE_AND_PDA = By.XPATH, "//a[normalize-space()='Phones & PDAs']"

    MY_ACCOUNT = By.XPATH, "//a[@title='My Account']"
    REGISTER = By.XPATH, "//a[text() = 'Register']"
    LOGIN = By.XPATH, "//a[text() = 'Login']"
    HOME_ICON = By.XPATH, "//i[@class='fa fa-home']"
    ADD_TO_CART_BTN_3 = By.XPATH, "(//span[contains(text(),'Add to Cart')])[3]"
    WISH_LIST_BADGE = By.XPATH, "//a[@id='wishlist-total']"
    SHOPPING_CART_BADGE = By.XPATH,"//a[@title='Shopping Cart']"
    CHECKOUT_BADGE = By.XPATH,"//a[@title='Checkout']"
    CART_TOTAL = By.XPATH, "//span[@id='cart-total']"
    CHECKOUT = By.XPATH, "//strong[normalize-space()='Checkout']"
    CART_TOTAL_BTN = By.XPATH, "(//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle'])[1]"
    MEDIUM = By.XPATH, "//input[@type='radio' and @value= '6']"
    UPLOAD_FILE = By.XPATH, "//button[@id='button-upload222']"
    TEXT = By.XPATH, "//input[@id='input-option208']"
    SELECT = By.XPATH, "//select[@id='input-option217']"
    TEXTAREA = By.XPATH, "//textarea[@id='input-option209']"
    DATE_AND_TIME = By.XPATH, "//input[@data-date-format='YYYY-MM-DD HH:mm']"
    QUANTITY = By.XPATH, "//input[@name='quantity']"
    ADDT_TO_CART_BTN = By.XPATH, "//button[@id='button-cart']"
    SUCCESS_YOU_HAVE_ADDED = By.XPATH, "//div[@class='alert alert-success alert-dismissible']"
    SUCCESS_PRODUCT = By.XPATH, "(//div[@class='alert alert-success alert-dismissible'])[1]/a[1]"
    PRODUCT_TITLE = By.XPATH, "(//div[@class='col-sm-4'])[2]/h1"
class wishlisht:
    PRODUCT_NAME_MACBOOK = By.XPATH, "//a[text()='MacBook']"
    PRODUCT_NAME_IPHONE = By.XPATH, "//a[text()='iPhone']"
    PRODUCT_NAME_APPLE = By.XPATH, "//a[text()='Apple Cinema 30\"']"
    PRODUCT_NAME_CANON = By.XPATH, "//a[text()='Canon EOS 5D']"

    EMPTY_WISHLIST = By.XPATH, "//p[text()='Your wish list is empty.']"
class register:
    FIRST_NAME = By.XPATH, "//input[@name='firstname']"
    LAST_NAME = By.XPATH, "//input[@name='lastname']"
    EMAIL = By.XPATH, "//input[@name='email']"
    TELEPHONE = By.XPATH, "//input[@name='telephone']"

    PASSWORD = By.XPATH, "//input[@name='password']"
    CONFIRM_PASSWORD = By.XPATH, "//input[@name='confirm']"

    PRIVACY_POLICY = By.XPATH, "//input[@type='checkbox' and @name='agree']"
    CONTINUE = By.XPATH, "//input[@value= 'Continue']"

    ERROR_MESSAGE = By.XPATH, "//div[@class='alert alert-danger alert-dismissible']"

    FIRST_NAME_VALIDATION = By.XPATH, "//div[text()='First Name must be between 1 and 32 characters!']"
    LAST_NAME_VALIDATION = By.XPATH, "//div[text()='Last Name must be between 1 and 32 characters!']"
    EMAIL_VALIDATION = By.XPATH, "//div[text()='E-Mail Address does not appear to be valid!']"
    PHONE_VALIDATION = By.XPATH, "//div[text()='Telephone must be between 3 and 32 characters!']"
    PASSWORD_VALIDATION = By.XPATH, "//div[text()='Password must be between 4 and 20 characters!']"

    ACCOUNT_HAS_BEEN_CREATED_TEXT = By.XPATH, "//h1[text()='Your Account Has Been Created!']"
    CONTINUE_CREATED_BTN = By.XPATH, "//a[@class='btn btn-primary']"

    HOME = By.XPATH, "//i[@class='fa fa-home']"
class login:
    EMAIL = By.XPATH, "//input[@name='email']"
    PASSWORD = By.XPATH,  "//input[@name='password']"
    LOGIN = By.XPATH, "//input[@value='Login']"
    ERROR_MESSAGE = By.XPATH, "//div[@class='alert alert-danger alert-dismissible']"


class checkout:

    FIRSTNAME = By.XPATH ,"//input[@id='input-payment-firstname']"
    LASTNAME = By.XPATH, "//input[@id='input-payment-lastname']"
    COMPANY = By.XPATH, "//input[@id='input-payment-company']"
    ADDRESS_1 = By.XPATH, "(//input[@id='input-payment-address-1'])[1]"
    CITY = By.XPATH, "//input[@id='input-payment-city']"
    POST_CODE = By.XPATH, "//input[@id='input-payment-postcode']"
    SELECT_COUNTRY = By.XPATH, "//select[@id='input-payment-country']"
    SELECT_REGION = By.XPATH, "//select[@id='input-payment-zone']"

    BILLING_DETAILS_CONTINUE = By.XPATH, "//input[@id='button-payment-address']"
    DELIVERY_DETAILS_CONTINUE = By.XPATH, "//input[@id='button-shipping-address']"
    DELIVERY_METHOD_CONTINUE = By.XPATH, "//input[@id='button-shipping-method']"
    PAYMENT_METHOD_CONTINUE = By.XPATH, "//input[@id = 'button-payment-method']"

    DELIVERY_METH0D_COMMENT = By.XPATH, "//textarea[@name='comment']"
    PAYMENT_METH0D_COMMENT = By.XPATH, "//textarea[@name='comment']"
    PRIVACY_AGREE = By.XPATH, "//input[@type='checkbox' and @name='agree']"
    CONFIRM_ORDER = By.XPATH, "//input[@value = 'Confirm Order']"

    ORDER_HAS_BEEN_PLACE_MESSAGE = By.XPATH, "//h1[normalize-space()='Your order has been placed!']"
    CONTINUE_LAST = By.XPATH, "//a[@href='https://awesomeqa.com/ui/index.php?route=common/home']"

    TERMS_CONDITION = By.XPATH, "//input[@name='agree']"
    USE_EXISTING_ADDRESS_DELIVERY_DETAILS = By.XPATH, "(//input[@name='shipping_address'])[1]"