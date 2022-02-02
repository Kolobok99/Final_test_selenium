import time

import pytest

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

@pytest.mark.xfail
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    """тест: тестирование добавления товара в корзину"""
    # 1. переходим на страницу товара
    #http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019
    link1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    page = ProductPage(browser, link)
    page.open()
    product_url_name = link.split('/')[5]
    product_name = browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    page.should_be_shell_coders_page(product_url_name=product_url_name)

    # 2. Нажимаем кнопку "Добавить товар"
    page.should_guest_click_on_add_button()

    # 3. Подсчитываем мат. выражение . . .
    page.solve_quiz_and_get_code()
    #time.sleep(30)
    # 4. Проверить сообщение "X has been added to your basket."
    #page.protudct_in_stock()
    expected_message = "×\n" + product_name + " has been added to your basket."
    print(f"{expected_message=}")
    page.added_message(expected_message)
    #time.sleep(10000000)

    # 4.1 Проверить сообщение со стоимостью корзины.
    expected_total_price = browser.find_element(*ProductPageLocators.TOTAL_PRICE_MESSAGE)
    expected_total_price_text = expected_total_price.text
    page.added_total_price(expected_total_price_text)
    #time.sleep(100)

@pytest.mark.xfail
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    # 1. Открываем стр. товара
    page = ProductPage(browser, link)
    page.open()

    # 2. Нажимаем кнопку
    page.should_guest_click_on_add_button()
    page.solve_quiz_and_get_code()

    # 3. Проверяем, что нет сообщения
    page.should_not_be_success_message()
@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    # 1. Открываем стр. товара
    page = ProductPage(browser, link)
    page.open()

    # 3. Проверяем, что нет сообщения
    page.should_not_be_success_message()

@pytest.mark.xfail
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    # 1. Открываем стр. товара
    page = ProductPage(browser, link)
    page.open()

    # 2. Нажимаем кнопку
    page.should_guest_click_on_add_button()
    page.solve_quiz_and_get_code()
    # 3. Проверяем, что нет сообщения
    page.should_dissapear_of_success_message()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

    assert 'login' in browser.current_url, \
        f"{browser.current_url=}"

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_cart_page()

    page.there_is_text_with_cart_empty()
    page.no_products_in_items()



