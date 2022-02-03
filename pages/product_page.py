from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_cart(self):
        self.should_guest_click_on_add_button()
        self.solve_quiz_and_get_code()

    def message_that_product_added_to_cart(self):
        self.added_message()
        self.added_total_price()

    def should_guest_click_on_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), \
            "Пользователь не может нажать на кнопку 'Добавить товар'"
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def protudct_in_stock(self):
        assert self.is_element_present(*ProductPageLocators.IN_STOCK), \
            "Product isn't in stock"

    def added_message(self):
        product_name_text = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        expected_message = "×\n" + product_name_text + " has been added to your basket."

        message_text = self.browser.find_element(*ProductPageLocators.IN_STOCK_MESSAGE).text

        assert expected_message == message_text, \
            f"Message: {message_text=}"

    def added_total_price(self):
        expected_total_price_text = self.browser.find_element(
            *ProductPageLocators.TOTAL_PRICE_MESSAGE).text

        total_price_text = self.browser.find_element(
            *ProductPageLocators.TOTAL_PRICE_MESSAGE).text

        assert expected_total_price_text in total_price_text, \
            f"total_price: {total_price_text}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.IN_STOCK_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.IN_STOCK_MESSAGE), \
            "Success message is presented, but should not be"
