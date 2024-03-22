import pytest
from pages.base_page import BasePage
from pages.order_page import OrderPage
from pages.signup_login_page import SignupLoginPage
from settings import sets
import random

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order_page
class TestOrderPage:

    def setup_method(self):
        # Генерация уникальных данных для каждого тестового запуска
        hash_name = "%032x" % random.getrandbits(128)
        self.email_for_signup = f"{hash_name}@mail.com"
        self.password_for_signup = "SecurePassword123"

    def test_get_main_page(self, browser):
        # Открытие главной страницы
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_signup_new_user(self, browser):
        # Регистрация нового пользователя
        self.link_to_cabinet = browser.current_url
        signup_page = SignupLoginPage(browser, self.link_to_cabinet)
        signup_page.click_button_signup_login()
        signup_page.explicit_wait(2)
        signup_page.click_signup()
        signup_page.explicit_wait(2)
        signup_page.input_email_password(self.email_for_signup, self.password_for_signup)
        signup_page.press_button_signup()
        signup_page.is_alert_success()

    def test_login_to_cabinet(self, browser):
        # Вход в систему зарегистрированным пользователем
        self.link_to_cabinet = browser.current_url
        login_page = SignupLoginPage(browser, self.link_to_cabinet)
        login_page.click_button_signup_login()
        login_page.explicit_wait(2)
        login_page.input_email_password(self.email_for_signup, self.password_for_signup)
        login_page.press_button_login()
        login_page.is_alert_success()
        login_page.is_button_logout_in_header()
        order_page = OrderPage(browser, self.link_to_cabinet)
        order_page.click_on_logo()
        order_page.explicit_wait(2)

    def test_add_products_to_cart(self, browser):
        # Добавление товаров в корзину и проверка их наличия
        self.link_to_cabinet = browser.current_url
        order_page = OrderPage(browser, self.link_to_cabinet)
        price_1_product = order_page.add_to_cart_first_product()
        order_page.explicit_wait(2)
        order_page.press_btn_continue_shop_popup()
        order_page.explicit_wait(2)
        price_2_product = order_page.add_to_cart_second_product()

    def test_check_total_price_qty(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        page.press_btn_checkout_popup()
        page.explicit_wait(2)
        page.check_total_price_qty(price_1_product, price_2_product, qty=3)  # qty - Quantity - кількість

    def test_checkout(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        page.add_notice()
        page.press_green_btn_checkout()
        page.is_alert_success()
        page.explicit_wait(5)


















