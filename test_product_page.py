from .pages.product_page import ProductPage
import pytest
import time

"""@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"])"""

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
failed = [7]
link_lst = [f"{LINK}{i}" if i not in failed else pytest.param(f"{LINK}{i}", marks=pytest.mark.xfail) for i in range(10)]


@pytest.mark.parametrize('link', link_lst)
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()  # открываем страницу
    page.should_be_promo_url()  # выполняем метод страницы — проверяем параметр промо в url страницы
    page.add_to_basket()  # добавляем товар в корзину
    page.solve_quiz_and_get_code()  # проверяем алерт, решаем задачу и вводим ответ
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.check_msg_added_to_basket(product_name)
    page.check_msg_price_in_basket(product_price)
