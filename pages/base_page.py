from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException, ElementClickInterceptedException
from settings import sets
import time

# Локаторы для разных страниц
from .locators import BasePageLocators, SignupLoginPageLocators  # Импорт класса с локаторами

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(sets.IMPLICITLY_WAIT)

    def open(self):
        self.browser.get(self.url)

    def explicit_wait(self, value):
        time.sleep(value)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def elements_are_present(self, how, what):
        try:
            self.browser.find_elements(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_appears_after_while(self, how, what, timeout):
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def hover_action(self, how, what):
        try:
            hover = self.browser.find_element(how, what)
            ActionChains(self.browser).move_to_element(hover).perform()
        except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
            return False
        return True

    def click_element(self, how, what):
        try:
            self.browser.find_element(how, what).click()
        except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException):
            return False
        return True

    def input_data(self, how, what, data):
        try:
            element = self.browser.find_element(how, what)
            element.clear()
            element.send_keys(data)
        except (NoSuchElementException, ElementNotInteractableException):
            return False
        return True

    def clear_field(self, how, what):
        try:
            self.browser.find_element(how, what).clear()
        except (NoSuchElementException, ElementNotInteractableException):
            return False
        return True

    def get_attribute(self, how, what, attribute):
        try:
            return self.browser.find_element(how, what).get_attribute(attribute)
        except NoSuchElementException:
            return None

    def get_text(self, how, what):
        try:
            return self.browser.find_element(how, what).text
        except NoSuchElementException:
            return None

    def refresh(self):
        self.browser.refresh()

    # Дополнительные методы для логина и логаута, которые могут быть переопределены или использованы напрямую, если подходят
    def login_to_cabinet(self, user_email, user_password):
        self.click_element(*BasePageLocators.LOGIN_SIGNUP)
        self.input_data(*SignupLoginPageLocators.INPUT_EMAIL, user_email)
        self.input_data(*SignupLoginPageLocators.INPUT_PASSWORD, user_password)
        self.click_element(*SignupLoginPageLocators.BUTTON_LOGIN)

    def logout_from_cabinet(self):
        self.click_element(*BasePageLocators.LOGOUT)


