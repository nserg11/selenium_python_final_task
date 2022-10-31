from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest
import time

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


# @pytest.mark.skip(reason="no need to be tested now")

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/accounts/login"
        self.email = str(time.time()) + "@fakemail.org"
        self.password = "1qazQAZ12345678"
        page = LoginPage(browser, self.link)
        page.open()
        page.register_new_user(self.email, self.password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, link=LINK):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link=LINK):
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        page.open()  # открываем страницу
        # page.should_be_promo_url()  # выполняем метод страницы — проверяем параметр промо в url страницы
        page.add_to_basket()  # добавляем товар в корзину
        # page.solve_quiz_and_get_code()  # проверяем алерт, решаем задачу и вводим ответ
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        page.check_msg_added_to_basket(product_name)
        page.check_msg_price_in_basket(product_price)


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link=LINK):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    # page.should_be_promo_url()  # выполняем метод страницы — проверяем параметр промо в url страницы
    page.add_to_basket()  # добавляем товар в корзину
    # page.solve_quiz_and_get_code()  # проверяем алерт, решаем задачу и вводим ответ
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.check_msg_added_to_basket(product_name)
    page.check_msg_price_in_basket(product_price)


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser, link=LINK):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link=LINK):
    page = ProductPage(browser, link)
    page.open()  # Гость открывает главную страницу
    page.go_to_basket_page()  # Переходит в корзину по кнопке в шапке сайта
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()  # Проверяем, что это страница корзины
    basket_page.should_be_no_products_in_basket()  # Проверяем, что в корзине нет продуктов
    basket_page.check_msg_empty_basket()  # Проверяем, что есть сообщение о пустой корзине


def test_guest_cant_see_success_message(browser, link=LINK):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="not supposed to pass")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link=LINK):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.add_to_basket()
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
