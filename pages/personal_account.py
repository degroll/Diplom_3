import allure


from locators.base_page_locators import BasePageLocators
from locators.personal_account_locators import PesonalAccountLocators
from .base_page import BasePage


class PersonalAccountPage(BasePage):
    personal_room = BasePageLocators.PERSONAL_ROOM
    name_field = PesonalAccountLocators.NAME_FIELD
    order_history = PesonalAccountLocators.ORDER_HISTORY
    logout = PesonalAccountLocators.LOGOUT

    @allure.step("Инициализируем драйвер")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажимаем на личный кабинет")
    def click_personal_account(self):
        self.wait_for_clicable_element(self.personal_room)
        self.click_element(self.personal_room)
        return self
    
    @allure.step("Получаем name атрибута")
    def get_name_attribute_value(self):
        self.find_element(self.name_field)
        value = self.get_element_attribute(self.name_field, "value")
        return value
    
    @allure.step("Нажимаем на историю заказов")
    def click_order_history(self):
        self.wait_for_clicable_element(self.order_history)
        self.click_element(self.order_history)
        class_attributes = self.get_element_attribute(self.order_history, "class")
        return class_attributes
    
    @allure.step("Нажимаем на <<Выход>>")
    def click_logout_button(self):
        self.wait_for_clicable_element(self.logout)
        self.click_element(self.logout)
        return self

