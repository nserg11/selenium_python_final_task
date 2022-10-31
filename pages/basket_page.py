from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'basket' in self.browser.current_url, "This is not basket url"

    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET_TEXT), f"Products in basket detected"

    def check_msg_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MSG), "Basket is not empty"
