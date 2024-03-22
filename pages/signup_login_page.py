from pages import base_page, locators
import inspect

class SignupLoginPage(base_page.BasePage):

    def click_button_signup_login(self):
        # Клик по кнопке входа или регистрации
        assert self.click_element(*locators.BasePageLocators.LOGIN_SIGNUP), \
            "Login/Signup button is not present or interactable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_h1_vhod(self):
        # Проверка наличия заголовка "Вход"
        assert self.is_element_present(*locators.SignupLoginPageLocators.H1_VHOD), \
            "H1 element for login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_button_login(self):
        # Клик по кнопке "Войти"
        assert self.click_element(*locators.SignupLoginPageLocators.BUTTON_LOGIN), \
            "Login button is not present or interactable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def click_signup(self):
        # Клик по кнопке регистрации
        assert self.click_element(*locators.SignupLoginPageLocators.GO_TO_SIGNUP), \
            "Signup button is not present or interactable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_h1_signup(self):
        # Проверка наличия заголовка "Регистрация"
        assert self.is_element_present(*locators.SignupLoginPageLocators.H1_SIGNUP), \
            "H1 element for signup is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_email_password(self, email, password):
        # Ввод email и пароля
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_EMAIL, email), \
            "Email input field is not present"
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_PASSWORD, password), \
            "Password input field is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_button_signup(self):
        # Клик по кнопке "Зарегистрироваться"
        assert self.click_element(*locators.SignupLoginPageLocators.BUTTON_SIGNUP), \
            "Signup button is not present or interactable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_alert_success(self):
        # Проверка появления уведомления об успешной операции
        assert self.is_element_appears_after_while(*locators.BasePageLocators.ALERT_SUCCESS, timeout=5), \
            "Success alert is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_logout_in_header(self):
        # Проверка наличия кнопки выхода
        assert self.is_element_present(*locators.BasePageLocators.LOGOUT), \
            "Logout button is not present in the header"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_button_logout(self):
        # Клик по кнопке выхода
        assert self.click_element(*locators.BasePageLocators.LOGOUT), \
            "Logout button is not present or interactable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_alert_success_after_subscribe(self):
        # Проверка уведомления об успешной подписке
        assert self.is_element_appears_after_while(*locators.BasePageLocators.ALERT_SUCCESS, timeout=5), \
            "Success alert after subscription is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")





