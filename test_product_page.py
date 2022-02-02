import time

import pytest

from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    """тест: тестирование добавления товара в корзину"""
    # 1. переходим на страницу товара
    #http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019
    link1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

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
    # 4. Проверить сообщение "Товар Х добавлен в корзину"
    #page.protudct_in_stock()
    expected_message = product_name
    page.added_message(expected_message)
    #time.sleep(10000000)

    # 4.1 Проверить сообщение со стоимостью корзины.
    expected_total_price = '9.99'
    page.added_total_price(expected_total_price)


