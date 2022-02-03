import time
import faker
import pytest

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage

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
        time.sleep(3)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        """тест: тестирование добавления товара в корзину"""
        # 0. Основные переменные
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

        # 1. переходим на страницу товара
        page = ProductPage(browser, link)
        page.open()

        # 1.1 Проверяем, что мы на нужно странице
        product_url_name = link.split('/')[5]
        page.should_be_desired_page(product_url_name=product_url_name)

        # 2. Нажимаем кнопку "Добавить товар"
        page.should_guest_click_on_add_button()

        # 3. Подсчитываем мат. выражение . . .
        page.solve_quiz_and_get_code()

        # 4. Проверить сообщение "X has been added to your basket."
        product_name = browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        expected_message = "×\n" + product_name + " has been added to your basket."
        page.added_message(expected_message)

        # 4.1 Проверить сообщение со стоимостью корзины.
        expected_total_price = browser.find_element(*ProductPageLocators.TOTAL_PRICE_MESSAGE)
        expected_total_price_text = expected_total_price.text
        page.added_total_price(expected_total_price_text)

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self,browser):
        """тест: тестирование добавления товара в корзину"""
        # 0. Основные переменные
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

        # 1. переходим на страницу товара
        page = ProductPage(browser, link)
        page.open()

        # 1.1 Проверяем, что мы на нужно странице
        product_url_name = link.split('/')[5]
        page.should_be_desired_page(product_url_name=product_url_name)

        # 2. Нажимаем кнопку "Добавить товар"
        page.should_guest_click_on_add_button()

        # 3. Подсчитываем мат. выражение . . .
        page.solve_quiz_and_get_code()

        # 4. Проверить сообщение "X has been added to your basket."
        product_name = browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        expected_message = "×\n" + product_name + " has been added to your basket."
        page.added_message(expected_message)

        # 4.1 Проверить сообщение со стоимостью корзины.
        expected_total_price = browser.find_element(*ProductPageLocators.TOTAL_PRICE_MESSAGE)
        expected_total_price_text = expected_total_price.text
        page.added_total_price(expected_total_price_text)

    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

        # 1. Открываем стр. товара
        page = ProductPage(browser, link)
        page.open()

        # 3. Проверяем, что нет сообщения
        page.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    # 1. Открываем стр. товара
    page = ProductPage(browser, link)
    page.open()

    # 2. Добавляем товар
    page.should_guest_click_on_add_button()
    page.solve_quiz_and_get_code()

    # 3. Проверяем, что нет сообщения
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    # 1. Открываем стр. товара
    page = ProductPage(browser, link)
    page.open()

    # 2. Добавляем товар
    page.should_guest_click_on_add_button()
    page.solve_quiz_and_get_code()

    # 3. Проверяем, что нет сообщения
    page.should_dissapear_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

    assert 'login' in browser.current_url, \
        f"{browser.current_url=}"

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_cart_page()

    page.there_is_text_with_cart_empty()
    page.no_products_in_items()



