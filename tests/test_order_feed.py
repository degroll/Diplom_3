import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage




class TestOrderFeed:
    @allure.title("Тест: Открытие модального окна заказа")
    def test_order_modal_opens(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open_order_feed()
        order_feed.click_first_order()
        assert order_feed.is_order_modal_disaplayed()

    @allure.title("Тест: Заказы пользователя появляются в списке заказов")
    def test_user_orders_appear_in_feed(self, create_user, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login_to_account()
        main_page = MainPage(driver)
        main_page.assemble_burger()
        main_page.place_order()
        order_number = main_page.get_order_number()
        main_page.close_modal()
        order_feed = OrderFeedPage(driver)
        order_feed.open_order_feed()
        result = order_feed.is_user_order_in_feed(order_number)
        assert result is not None
        assert order_number in result

    @allure.title("Тест: Увеличивается счётчик всех заказов")
    def test_total_order_counter_is_incremented(self, create_user, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open_order_feed()
        counter_before = order_feed.get_total_orders_count()
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login_to_account()
        main_page = MainPage(driver)
        main_page.assemble_burger()
        main_page.place_order()
        main_page.close_modal()
        order_feed.open_order_feed()
        counter_after = order_feed.get_total_orders_count()
        assert int(counter_after) > int(counter_before)

    @allure.title("Тест: Увеличивается счётчик сегодняшних заказов")
    def test_today_order_counter_is_incremented(self, create_user, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open_order_feed()
        counter_before = order_feed.get_today_orders_count()
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login_to_account()
        main_page = MainPage(driver)
        main_page.assemble_burger()
        main_page.place_order()
        main_page.close_modal()
        order_feed.open_order_feed()
        counter_after = order_feed.get_today_orders_count()
        assert int(counter_after) > int(counter_before)

    @allure.title("Тест: Номер заказа появляется в разделе <<В работе>>")
    def test_order_number_appear_in_progress_section(self, create_user, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login_to_account()
        main_page = MainPage(driver)
        main_page.assemble_burger()
        main_page.place_order()
        order_number = main_page.get_order_number()
        main_page.close_modal()
        order_feed = OrderFeedPage(driver)
        order_feed.open_order_feed()
        first_progress_order = order_feed.get_first_progress_order()
        assert order_number in first_progress_order

