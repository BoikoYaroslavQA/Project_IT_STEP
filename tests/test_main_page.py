import pytest
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
from ..settings import sets
import random


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        hash_name = "%032x" % random.getrandbits(128)
        self.email_for_subscribe = f"{hash_name}@mail.com"

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_main_page_header(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_login()
        page.is_button_feedback()
        page.is_button_delivery()
        page.is_button_warranty()
        page.is_number_phone()
        page.is_element_currency()
        page.is_element_currency_uah()
        page.is_element_currency_usd()
        page.is_element_currency_eur()
        page.is_element_logo()
        page.is_search_input_field()
        page.is_search_button()
        page.is_wish_button()
        page.is_cart_button()
        page.is_hity_button()
        page.is_skidki_button()
        page.is_novinki_button()
        page.is_samsung_category()
        page.is_samsung_j701()

    def test_main_page_content(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_main_slider()
        page.is_left_category_zaryadki()
        page.is_left_subcategory_powerbank()
        page.is_info_block_refund()
        page.is_info_block_delivery()
        page.is_info_block_otsrochka()
        page.is_info_block_support()
        page.is_button_show_new_products()
        page.is_button_show_prev_new_products()
        page.is_button_show_next_new_products()
        page.is_section_new_products()
        page.is_new_product_8()
        page.is_button_show_hits()
        page.is_button_prev_hits()
        page.is_button_next_hits()
        page.is_section_hits()
        page.is_button_prev_trends()
        page.is_button_next_trends()

    def test_main_page_footer(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_subscribe()
        page.is_logo_footer()

    def test_main_page_subscribe_action(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.subscribe_action(self.email_for_subscribe)
        page.is_alert_success_after_subscribe()









