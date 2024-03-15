from ..pages import base_page, locators
import inspect


class SignupLoginPage(base_page.BasePage):

    def click_button_signup_login(self):
        assert self.click_element(*locators.BasePageLocators.LOGIN_SIGNUP), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_h1_vhod(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.H1_VHOD), \
            "Button login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_button_login(self):
        assert self.click_element(*locators.SignupLoginPageLocators.BUTTON_LOGIN), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def click_signup(self):
        assert self.click_element(*locators.SignupLoginPageLocators.GO_TO_SIGNUP), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_h1_signup(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.H1_SIGNUP), \
            "Button login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_email_password(self, email, password):
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_EMAIL, email), \
            "The element currency is not present"
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_PASSWORD, password), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_button_signup(self):
        assert self.click_element(*locators.SignupLoginPageLocators.BUTTON_SIGNUP), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_alert_success(self):
        assert self.is_element_appears_after_while(*locators.BasePageLocators.ALERT_SUCCESS, timeout=5), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_logout_in_header(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGOUT), \
            "Button login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_button_logout(self):
        assert self.click_element(*locators.BasePageLocators.LOGOUT), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
