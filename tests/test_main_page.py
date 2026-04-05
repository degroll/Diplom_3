import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage

from data import CONSTRUCTOR_TEXT
from urls import URL_FEED


class TestMainPage:
    @allure.title("Тест: Переход в конструктор заказа")
    def test_click_through_to_constructor(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_constructor()
        main_page = MainPage(driver)
        assert main_page.get_constructor_text() == CONSTRUCTOR_TEXT

    @allure.title("Тест: Переход в ленту заказов")
    def test_click_through_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_feed()
        assert main_page.get_current_url() == URL_FEED

    @allure.title("Тест: Появление подробной информации об ингредиенте")
    def test_ingredient_modal_appears(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_any_ingredient()
        assert main_page.is_modal_displayed()

    @allure.title("Тест: Закрытие модального окна с информацией")
    def test_ingredient_modal_closes(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_any_ingredient()
        main_page.close_modal()
        assert main_page.is_modal_closed()

    @allure.title("Тест: Работает ли счётчик соуса")
    def test_sauce_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        initial_counter = main_page.get_sauce_ingredient_counter_value()
        main_page.add_sauce_to_order()
        new_counter = main_page.get_sauce_ingredient_counter_value()
        assert new_counter == initial_counter + 1

    @allure.title("Тест: Авторизованный пользователь может сделать заказ")
    def test_authorized_user_can_place_order(self, create_user, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login_to_account()
        main_page = MainPage(driver)
        main_page.assemble_burger()
        main_page.place_order()
        order_number = main_page.get_order_number()
        assert order_number is not None
        assert order_number.isdigit()
