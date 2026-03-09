import pytest
import allure
from pages.login_page import LoginPage
from pages.personal_account import PersonalAccountPage

from data import TEST_ACCOUNT, ACCOUNT_LINK_ACTIVE
from urls import URL_LOGIN


class TestPersonalAccount:
    @allure.title("Тест: Перех в личный кабинет")
    def test_click_through_to_account(self, create_user, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login_to_account()
        personal_account = PersonalAccountPage(driver)
        personal_account.click_personal_account()
        assert personal_account.get_name_attribute_value() == TEST_ACCOUNT["name"]

    @allure.title("Тест: Переход в историю заказов пользователя")
    def test_click_through_to_order_history(self, create_user, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login_to_account()
        personal_account = PersonalAccountPage(driver)
        personal_account.click_personal_account()
        class_attributes = personal_account.click_order_history()
        assert ACCOUNT_LINK_ACTIVE in class_attributes

    @allure.title("Тест: Выход из аккаунта")
    def test_logout_of_account(self, create_user, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login_to_account()
        personal_account = PersonalAccountPage(driver)
        personal_account.click_personal_account()
        personal_account.click_logout_button()
        login_page.wait_for_visibility_header()
        assert login_page.get_current_url() == URL_LOGIN


    