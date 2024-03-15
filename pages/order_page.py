from ..pages import base_page, locators
import inspect
import re


class OrderPage(base_page.BasePage):

    def click_on_logo(self):
        assert self.click_element(*locators.BasePageLocators.LOGO), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def add_to_cart_first_product(self):
        assert self.hover_action(*locators.OrderPageLocators.FIRST_PRODUCT), \
            "The element is not present"
        assert self.click_element(*locators.OrderPageLocators.BUTTON_ADD_FIRST_PRODUCT), \
            "The element is not present or intractable"
        price = self.get_text(*locators.OrderPageLocators.PRICE_FIRST_PRODUCT)
        price = int(price.replace(' грн.', '')) # 170
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
        if price:
            return price

    def press_btn_continue_shop_popup(self):
        assert self.click_element(*locators.OrderPageLocators.BTN_CONTINUE_SHOP_POPUP), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def add_to_cart_second_product(self):
        assert self.click_element(*locators.MainPageLocators.BUTTON_SHOW_HITS), \
            "The element currency is not present or intractable"
        self.explicit_wait(2)
        assert self.clear_field(*locators.OrderPageLocators.SECOND_PRODUCT_INPUT_NUMBER_QTY), \
            "The element currency is not present"
        assert self.input_data(*locators.OrderPageLocators.SECOND_PRODUCT_INPUT_NUMBER_QTY, 2), \
            "The element currency is not present"
        price = self.get_text(*locators.OrderPageLocators.PRICE_SECOND_PRODUCT)
        price = int(price.replace(' грн.', ''))*2
        assert self.click_element(*locators.OrderPageLocators.BUTTON_ADD_SECOND_PRODUCT), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
        if price:
            return price

    def check_total_price_qty(self, price1, price2, qty):
        total_price = self.get_text(*locators.OrderPageLocators.TOTAL_PRICE)
        self.explicit_wait(2)
        total_price = int(re.sub("[^0-9]", "", total_price))
        print(f"total_prise int: {total_price}")
        total_actual = price1+price2
        print(f"total_actual int: {total_actual}")
        assert total_actual == total_price, \
            "Total price doesn't match to actual"
        qty_actual = int(self.get_text(*locators.OrderPageLocators.QTY))
        assert qty_actual == qty, \
            "QTY doesn't match to actual"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_btn_checkout_popup(self):
        assert self.click_element(*locators.OrderPageLocators.CHECKOUT_BTN_POPUP), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def add_notice(self):
        assert self.input_data(*locators.OrderPageLocators.INPUT_NOTE, "Test.."), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_green_btn_checkout(self):
        assert self.click_element(*locators.OrderPageLocators.CHECKOUT_BUTTON), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_alert_success(self):
        assert self.is_element_appears_after_while(*locators.BasePageLocators.ALERT_SUCCESS, timeout=5), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
