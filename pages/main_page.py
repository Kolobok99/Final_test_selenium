from selenium.webdriver.common.by import By

from .locators import MainPageLocators
from .base_page import BasePage

class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.is_element_present(
            *MainPageLocators.LOGIN_LINK)
        assert login_link.click(), \
            "Не удается перейти на стр. Login"

    def should_be_login_link(self):
        assert self.is_element_present(
            *MainPageLocators.LOGIN_LINK), \
            "Login link is not presented"

