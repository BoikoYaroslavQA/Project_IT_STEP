from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
# from pages.locators import BasePageLocators
from ..settings import sets
import time


class BasePage:

    def __init__(self, browser, url):

        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(sets.IMPLICITLY_WAIT)

    def explicit_wait(self, value):
        time.sleep(value)

    def open(self):
        self.browser.get(self.url)

    def refresh(self):
        self.browser.refresh()

    def is_element_present(self, how, what):
        try: self.browser.find_element(how, what)
        except NoSuchElementException: return False
        return True

    def elements_are_present(self, how, what):
        try: self.browser.find_elements(how, what)
        except NoSuchElementException: return False
        return True

    def is_element_appears_after_while(self, how, what, timeout):
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def hover_action(self, how, what):
        try: hover = self.browser.find_element(how, what)
        except NoSuchElementException or ElementNotInteractableException or ElementClickInterceptedException: return False
        ActionChains(self.browser).move_to_element(hover) \
            .perform()
        return True

    def click_element(self, how, what):
        try: self.browser.find_element(how, what).click()
        except NoSuchElementException or ElementNotInteractableException or ElementClickInterceptedException: return False
        return True

    def input_data(self, how, what, data):
        try: self.browser.find_element(how, what).send_keys(data)
        except NoSuchElementException or ElementNotInteractableException: return False
        return True

    def clear_field(self, how, what):
        try: self.browser.find_element(how, what).clear()
        except NoSuchElementException or ElementNotInteractableException: return False
        return True

    def get_attribute(self, how, what, data):
        try: attribute = self.browser.find_element(how, what).get_attribute(data)
        except NoSuchElementException: return False
        return attribute

    def get_text(self, how, what):
        try: text = self.browser.find_element(how, what).text
        except NoSuchElementException: return None
        return text

    def login_to_cabinet(self, user_name, user_password):
        pass

    def logout_from_cabinet(self):
        pass

