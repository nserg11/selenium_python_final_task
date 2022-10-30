from .pages.product_page import ProductPage
import pytest
import time

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.skip(reason="no need to be tested now")
# @pytest.mark.parametrize('link', LINK)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.should_be_promo_url()  # выполняем метод страницы — проверяем параметр промо в url страницы
    page.add_to_basket()  # добавляем товар в корзину
    page.solve_quiz_and_get_code()  # проверяем алерт, решаем задачу и вводим ответ
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.check_msg_added_to_basket(product_name)
    page.check_msg_price_in_basket(product_price)


@pytest.mark.xfail(reason="not supposed to pass")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link=LINK):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser, link=LINK):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="not supposed to pass")
def test_message_disappeared_after_adding_product_to_basket(browser, link=LINK):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()