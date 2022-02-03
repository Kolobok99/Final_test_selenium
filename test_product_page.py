import time
import faker
import pytest

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage:
    """test: """

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        fake = faker.Faker()
        email = fake.email()
        password = fake.password()
        test_guest_can_go_to_login_page_from_product_page(browser)
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """тест: тестирование добавления товара в корзину"""
        # 1. переходим на страницу товара
        page = ProductPage(browser, LINK)
        page.open()
        # 2. Добавляем товар в корзину
        page.add_product_to_cart()
        # 3. Проверить сообщения о добавлении товара
        page.message_that_product_added_to_cart()

    def test_user_cant_see_success_message(self, browser):

        # 1. Открываем стр. товара
        page = ProductPage(browser, LINK)
        page.open()
        # 3. Проверяем, что нет сообщения
        page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    """тест: тестирование добавления товара в корзину"""
    # 0. Основные переменные

    # 1. переходим на страницу товара
    page = ProductPage(browser, LINK)
    page.open()
    # 2. Добавляем товар в корзину
    page.add_product_to_cart()
    # 3. Проверить сообщения о добавлении товара
    page.message_that_product_added_to_cart()

def test_guest_cant_see_success_message(browser):

    # 1. Открываем стр. товара
    page = ProductPage(browser, LINK)
    page.open()
    # 3. Проверяем, что нет сообщения
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):

    # 1. Открываем стр. товара
    page = ProductPage(browser, LINK)
    page.open()
    # 2. Добавляем товар
    page.should_guest_click_on_add_button()
    page.solve_quiz_and_get_code()
    # 3. Проверяем, что нет сообщения
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):

    # 1. Открываем стр. товара
    page = ProductPage(browser, LINK)
    page.open()
    # 2. Добавляем товар
    page.should_guest_click_on_add_button()
    page.solve_quiz_and_get_code()
    # 3. Проверяем, что нет сообщения
    page.should_dissapear_of_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, LINK)
    page.open()
    page.go_to_cart_page()

    page.there_is_text_with_cart_empty()
    page.no_products_in_items()



