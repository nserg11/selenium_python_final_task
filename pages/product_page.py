from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_promo_url(self):
        assert '?promo' in self.browser.current_url, "This is not promo url"

    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Add-to-basket button not found"
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_button.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        # result = re.sub(r'[^\d.]', '', product_price.text)
        return product_price.text

    def check_msg_added_to_basket(self, product_name):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_SUCCESS_MSG), "No message for added product"
        msg = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_SUCCESS_MSG)
        assert product_name == msg.text, "Incorrect product name in message"

    def check_msg_price_in_basket(self, product_price):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MSG), "No message for basket total"
        msg = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MSG)
        assert product_price in msg.text, "Incorrect product price in message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_SUCCESS_MSG), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_SUCCESS_MSG), \
            "Success message is presented, but should have disappeared"
