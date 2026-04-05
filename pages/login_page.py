import allure

from locators.login_page_locators import LoginPageLocators
from locators.base_page_locators import BasePageLocators
from .base_page import BasePage
from urls import URL_LOGIN, URL
from data import TEST_ACCOUNT


class LoginPage(BasePage):
    recovery_link = LoginPageLocators.RECOVER_LINK
    login_header = LoginPageLocators.LOGIN_HEADER
    email_field = LoginPageLocators.EMAIL_FIELD
    password_field = LoginPageLocators.PASSWORD_FIELD
    login_button = LoginPageLocators.LOGIN_BUTTON
    constructor = BasePageLocators.CONSTRUCTOR


    @allure.step("Инициализируем драйвер")
    def __init__(self, driver):
        self.url = URL_LOGIN
        super().__init__(driver)

    @allure.step("Открываем страницу")
    def open_login_page(self):
        self.open(self.url)
        return self
    
    @allure.step("Ожидавем видимости заголовка логина")
    def wait_for_visibility_header(self):
        self.wait_for_visibility_element(self.login_header)
    
    @allure.step("Нажимаем на ссылку восстановления")
    def click_recovery_link(self):
        self.click_element(self.recovery_link)
        return self
    
    @allure.step("Нажимаем на конструктор")
    def click_constructor(self):
        self.click_element(self.constructor)
        return self

    @allure.step("Логинимся")
    def login_to_account(self):
        self.wait_for_visibility_element(self.email_field)
        self.send_keys(self.email_field, TEST_ACCOUNT["email"])
        self.wait_for_visibility_element(self.password_field)
        self.send_keys(self.password_field, TEST_ACCOUNT["password"])
        self.click_element(self.login_button)
        self.wait_for_url_contains(URL)
        return self



    
