from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_EMAIL), \
            "LOGIN_EMAIL is not presented"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_PASSWORD), \
            "LOGIN_PASSWORD is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REG_EMAIL), \
            "REG_EMAIL is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REG_PASSWORD), \
            "REG_PASSWORD is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REG_PASSWORD_CONFIRM), \
            "REG_PASSWORD_CONFIRM is not presented"