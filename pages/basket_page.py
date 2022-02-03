from .locators import CartPageLocators
from .base_page import BasePage
from .login_page import LoginPage

class BasketPage(BasePage):
    """Test the Basket page"""

    def no_products_in_items(self):
        assert self.is_element_present(*CartPageLocators.CART_EMPTY), \
            "There is not emty_element!!!"

    def there_is_text_with_cart_empty(self):
        empty_text = self.browser.find_element(*CartPageLocators.CART_EMPTY).text
        assert "empty" in empty_text, \
            "There is not 'empty' in text!!!"



