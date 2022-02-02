import time
from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    """Класс страницы товара"""

    def should_be_shell_coders_page(self, product_url_name):
        assert product_url_name in self.browser.current_url, \
        f"Это не страницы 'The shellcoder's handbook'\n Это {self.browser.current_url}"

    def should_guest_click_on_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), \
            "Пользователь не может нажать на кнопку 'Добавить товар'"
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def protudct_in_stock(self):
        assert self.is_element_present(*ProductPageLocators.IN_STOCK), \
            "Product isn't in stock"

    # has been added to your basket.
    # Your basket total is now £19.99
    def added_message(self, expected_message):
        message = self.browser.find_element(*ProductPageLocators.IN_STOCK_MESSAGE)
        message_text = message.text
        assert expected_message in message_text, f"Message: {message_text=}"

    def added_total_price(self, expected_total_price):
        total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_MESSAGE)
        total_price_text = "Your basket total is now £" + total_price.text
        assert expected_total_price in total_price_text,\
            f"total_price: {total_price_text}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.IN_STOCK_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.IN_STOCK_MESSAGE), \
            "Success message is presented, but should not be"