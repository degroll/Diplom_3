import allure

from locators.recovery_page_locators import RecoveryPageLocators
from .base_page import BasePage



class RecoveryPage(BasePage):
    email_field = RecoveryPageLocators.EMAIL_FIELD
    recover_button = RecoveryPageLocators.RECOVER_BUTTON
    password_field = RecoveryPageLocators.PASSWORD_FIELD
    show_hide_icon = RecoveryPageLocators.SHOW_HIDE_ICON
    password_input = RecoveryPageLocators.PASSWORD_INPUT
    recovery_header = RecoveryPageLocators.RECOVER_HEADER

    @allure.step("Инициализируем драйвер")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Пишем эл. почту")
    def send_keys_into_email_field(self, email):
        self.wait_for_visibility_element(self.email_field)
        self.send_keys(self.email_field, email)

    @allure.step("Нажимаем на сбросить аккаунт")
    def recover_password_with_email(self, email):
        self.send_keys_into_email_field(email)
        self.click_element(self.recover_button)
        return self
    
    @allure.step("Показать/скрыть поле пароля")
    def complete_recovery_flow(self, email, new_password):
        self.recover_password_with_email(email)
        self.find_element(self.password_field)
        self.send_keys(self.password_field, new_password)
        self.click_element(self.show_hide_icon)
        return self
    
    @allure.step("Ждём, когда появится поля пароля")
    def wait_for_password_field_appear(self):
        self.wait_for_visibility_element(self.password_field)
        return self
    
    @allure.step("Проверяем активно ли поле пароля")
    def is_password_input_active(self):
        show_hide = self.find_element(self.password_input)
        class_attribute = show_hide.get_attribute("class")
        active_classes = ['input_status_active', 'focused', 'active', 'input__field_focused']
        for active_class in active_classes:
            if active_class in class_attribute:
                return True
        return False
    
    @allure.step("Нажимаем на сброс пароля и ждём появления поля пароля")
    def request_password_recovery(self, email):
        self.recover_password_with_email(email)
        self.wait_for_visibility_element(self.password_field)
        return self  
    
    @allure.step("Нажимаем на иконку видимости/невидимости пароля")
    def toggle_password_visibility(self):
        self.click_element(self.show_hide_icon)
        return self


