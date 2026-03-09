import allure

from selenium.webdriver.common.action_chains import ActionChains
from locators.main_page_locators import MainPageLocators
from .base_page import BasePage
from urls import URL


class MainPage(BasePage):
    make_burger_text = MainPageLocators.MAKE_BURGER_TEXT
    order_feed = MainPageLocators.ORDER_FEED
    any_ingredient = MainPageLocators.ANY_INGREDIENT
    modal_window = MainPageLocators.MODAL_WINDOW
    modal_close_button = MainPageLocators.MODAL_CLOSE_BUTTON
    constructor_basket = MainPageLocators.CONSTRUCTOR_BASKET
    sauce_counter = MainPageLocators.SAUCE_COUNTER
    sauce_ingredient = MainPageLocators.SAUCE_INGREDIENT
    modal_ingredient_head = MainPageLocators.MODAL_INGREDIENT_HEAD
    bun_ingredient = MainPageLocators.BUN_INGREDIENT
    filling_ingredient = MainPageLocators.FILLING_INGREDIENT
    place_order_button = MainPageLocators.PLACE_ORDER_BUTTON
    order_number = MainPageLocators.ORDER_NUMBER

    @allure.step("Инициализируем драйвер")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открываем страницу")
    def open_main_page(self):
        self.open(URL)
        return self
    
    @allure.step("Нажимаем на любой ингредиент")
    def click_any_ingredient(self):
        self.click_element(self.any_ingredient)
        return self

    @allure.step("Проверяем открыто ли модальное окно")
    def is_modal_displayed(self):
        return self.wait_for_visibility_element(self.modal_window).is_displayed()
    
    @allure.step("Закрываем модальное окно")
    def close_modal(self):
        self.click_element(self.modal_close_button)
        self.wait_for_invisibility_element(self.modal_ingredient_head)
        return self
    
    @allure.step("Проверяем закрыто ли модальное окно")
    def is_modal_closed(self):
        try: 
            self.wait_for_visibility_element(self.modal_ingredient_head)
            return False
        except:
            return True
        
    @allure.step("Добавляем ингредиенты")
    def add_ingredient(self, locator):
        ingredient = self.wait_for_visibility_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", ingredient)
        basket = self.wait_for_visibility_element(self.constructor_basket)
        action = ActionChains(self.driver)    
        action.click_and_hold(ingredient).move_to_element(basket).perform()
        action.release().perform()
               
    @allure.step("Добавляем соус")
    def add_sauce_to_order(self):
        self.add_ingredient(self.sauce_ingredient)
        return self
    
    @allure.step("Добавляем булку")
    def add_bun_to_order(self):
        self.add_ingredient(self.bun_ingredient)
        return self
    
    @allure.step("Добавляем соус")
    def add_filling_to_order(self):
        self.add_ingredient(self.filling_ingredient)
        return self
    
    @allure.step("Собираем бургер")
    def assemble_burger(self):
        self.add_bun_to_order()
        self.add_filling_to_order()
        self.add_sauce_to_order()
        return self
    
    @allure.step("Создаём заказ")
    def place_order(self):
        button = self.wait_for_clicable_element(self.place_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", button)
        button.click()
        return self
    
    @allure.step("Получаем номер заказа")
    def get_order_number(self):
        number_element = self.wait_for_visibility_element(self.order_number).text
        while number_element == '9999':
            number_element = self.wait_for_visibility_element(self.order_number).text
    
        return number_element
    
    @allure.step("Считаем соус")
    def get_sauce_ingredient_counter_value(self):
        try:
            counter_element = self.wait_for_visibility_element(self.sauce_counter)
            counter_text = counter_element.text
            return int(counter_text) if counter_text.isdigit() else 0
        except:
            return 0
        
    @allure.step("Получаем текст конструктора")
    def get_constructor_text(self):
        text = self.get_element_text(self.make_burger_text)
        return text
    
    @allure.step("Нажимаем на ленту заказов")
    def click_order_feed(self):
        self.click_element(self.order_feed)
        return self
    

    



