import pytest
from ..pages.base_page import BasePage
from ..pages.order_page import OrderPage
from ..pages.signup_login_page import SignupLoginPage
from ..settings import sets
import random


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order_page
class TestOrderPage:

    def setup_method(self):
        hash_name = "%032x" % random.getrandbits(128)
        self.email_for_subscribe = f"{hash_name}@mail.com"

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_login_to_cabinet(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.click_button_signup_login()
        page.explicit_wait(2)
        page.input_email_password(sets.TEST_EMAIL, sets.PASSWORD)
        page.press_button_login()
        page.is_alert_success()
        page.is_button_logout_in_header()
        page = OrderPage(browser, self.link_to_cabinet)
        page.click_on_logo()
        page.explicit_wait(2)

    def test_add_products_to_cart(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        global price_1_product
        price_1_product = page.add_to_cart_first_product()
        page.explicit_wait(2)
        page.press_btn_continue_shop_popup()
        page.explicit_wait(2)
        global price_2_product
        price_2_product = page.add_to_cart_second_product()

    def test_check_total_price_qty(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        page.press_btn_checkout_popup()
        page.explicit_wait(2)
        page.check_total_price_qty(price_1_product, price_2_product, qty=3) # qty - Quantity - кількість

    def test_checkout(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        page.add_notice()
        page.press_green_btn_checkout()
        page.is_alert_success()
        page.explicit_wait(5)

















