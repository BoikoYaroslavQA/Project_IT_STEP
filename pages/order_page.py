from pages import base_page, locators
import inspect
import re

class OrderPage(base_page.BasePage):
    def click_on_logo(self):
        # Клик по логотипу сайта
        assert self.click_element(*locators.BasePageLocators.LOGO), \
            "The logo element is not present or interactable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def add_to_cart_first_product(self):
        # Добавление первого продукта в корзину
        assert self.hover_action(*locators.OrderPageLocators.FIRST_PRODUCT), \
            "The first product element is not present"
        assert self.click_element(*locators.OrderPageLocators.BUTTON_ADD_FIRST_PRODUCT), \
            "The 'Add to Cart' button for the first product is not present or interactable"
        price = self.get_text(*locators.OrderPageLocators.PRICE_FIRST_PRODUCT)
        price = int(price.replace(' грн.', ''))
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
        return price

    def press_btn_continue_shop_popup(self):
        # Закрытие попапа продолжения покупок
        assert self.click_element(*locators.OrderPageLocators.BTN_CONTINUE_SHOP_POPUP), \
            "The 'Continue Shopping' popup button is not present or interactable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def add_to_cart_second_product(self):
        # Добавление второго продукта в корзину
        assert self.click_element(*locators.MainPageLocators.BUTTON_SHOW_HITS), \
            "The 'Show Hits' button is not present or interactable"
        self.explicit_wait(2)
        assert self.clear_field(*locators.OrderPageLocators.SECOND_PRODUCT_INPUT_NUMBER_QTY), \
            "The quantity input for the second product is not present"
        assert self.input_data(*locators.OrderPageLocators.SECOND_PRODUCT_INPUT_NUMBER_QTY, '2'), \
            "Failed to input quantity for the second product"
        price = self.get_text(*locators.OrderPageLocators.PRICE_SECOND_PRODUCT)
        price = int(price.replace(' грн.', '')) * 2
        assert self.click_element(*locators.OrderPageLocators.BUTTON_ADD_SECOND_PRODUCT), \
            "The 'Add to Cart' button for the second product is not present or interactable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
        return price

    def check_total_price_qty(self, price1, price2, qty):
        # Проверка общей стоимости и количества товаров в корзине
        total_price = self.get_text(*locators.OrderPageLocators.TOTAL_PRICE)
        self.explicit_wait(2)
        total_price = int(re.sub("[^0-9]", "", total_price))
        total_actual = price1 + price2
        assert total_actual == total_price, "Total price doesn't match the actual"
        qty_actual = int(self.get_text(*locators.OrderPageLocators.QTY))
        assert qty_actual == qty, "Quantity doesn't match the actual"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_btn_checkout_popup(self):
        # Клик по кнопке оформления заказа в попапе
        assert self.click_element(*locators.OrderPageLocators.CHECKOUT_BTN_POPUP), \
            "The checkout button in popup is not present or interactable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def add_notice(self):
        # Добавление примечания к заказу
        assert self.input_data(*locators.OrderPageLocators.INPUT_NOTE, "Test.."), \
            "The note input field is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_green_btn_checkout(self):
        assert self.click_element(*locators.OrderPageLocators.CHECKOUT_BUTTON), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

