import allure

from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from urls import URL_FEED



class OrderFeedPage(BasePage):
    first_order = OrderFeedLocators.FIRST_ORDER
    order_modal_close = OrderFeedLocators.ORDER_MODAL_CLOSE
    today_orders_counter = OrderFeedLocators.TODAY_ORDER_COUNTER
    total_orders_counter = OrderFeedLocators.TOTAL_ORDER_COUNTER
    first_order_in_progress = OrderFeedLocators.FIRST_ORDER_IN_PROGRESS
    user_order_in_feed = OrderFeedLocators.USER_ORDER_IN_FEED

    @allure.step("Инициализируем драйвер")
    def __init__(self, driver):
        self.url = URL_FEED
        super().__init__(driver)

    @allure.step("Открываем страницу")
    def open_order_feed(self):
        self.open(self.url)
        return self

    @allure.step("Нажимаем на первый заказ в списке")
    def click_first_order(self):
        self.click_element(self.first_order)
        return self
    
    @allure.step("Проверяем открыто ли модальное окно")
    def is_order_modal_disaplayed(self):
        return self.wait_for_visibility_element(self.order_modal_close)
 
    @allure.step("Получаем число сегодняшних сделанных заказов")
    def get_today_orders_count(self):
        counter = self.wait_for_visibility_element(self.today_orders_counter)
        return int(counter.text)
    
    @allure.step("Получаем число за всё время сделанных заказов")
    def get_total_orders_count(self):
        counter = self.wait_for_visibility_element(self.total_orders_counter)
        return int(counter.text)
    
    @allure.step("Получаем первый заказ в списке <<В работе>>")
    def get_first_progress_order(self):
        order = self.wait_for_visibility_element(self.first_order_in_progress).text
        while not order.isdigit():
            order = self.wait_for_visibility_element(self.first_order_in_progress).text
        return order
        
    @allure.step("Проверяем есть ли номер заказа пользователя в ленте заказов")   
    def is_user_order_in_feed(self, order_number):
        by, xpath = self.user_order_in_feed
        formatted_xpath = xpath.format(order_number=order_number)
        locator = (by, formatted_xpath)
        order_element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return order_element.text
    


    