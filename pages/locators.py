from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    # ВХОД
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")

    # РЕГИСТРАЦИЯ
    REG_EMAIL = (By.ID, "id_registration-email")
    REG_PASSWORD = (By.ID, "id_registration-password1")
    REG_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")

    REG_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1:nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[class='col-sm-6 product_main'] > p:nth-child(2)")
    ADD_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    IN_STOCK = (By.CSS_SELECTOR, ".instock.availability")
    IN_STOCK_MESSAGE = (By.CSS_SELECTOR, "[class='alert alert-safe alert-noicon alert-success  fade in']:nth-child(1)")
    TOTAL_PRICE_MESSAGE = (By.CSS_SELECTOR, "[class='alertinner '] >p > strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    CART_LINK = (By.CSS_SELECTOR, ".btn-group > a")

    USER_ICON = (By.CLASS_NAME, "icon-user")


class CartPageLocators():
    CART_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
