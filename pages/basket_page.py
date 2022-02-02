from .locators import CartPageLocators
from .base_page import BasePage
from .login_page import LoginPage

class BasketPage(BasePage):
    """Тест стр. Корзина"""

    def no_products_in_items(self):
        assert self.is_element_present(*CartPageLocators.CART_EMPTY), \
            "Cart is not empty!"

    def there_is_text_with_cart_empty(self):
        empty_text = self.browser.find_element(*CartPageLocators.CART_EMPTY).text
        assert "empty" in empty_text, \
            "There isn't 'empty' in text!!!"



