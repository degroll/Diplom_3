import pytest
import allure
from pages.login_page import LoginPage
from pages.recovery_page import RecoveryPage
from data import TEST_EMAIL


class TestPasswordRecovery:
    @allure.title("Тест: Переход на страницу восстановления пароля")
    def test_go_to_password_recovery_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_element(login_page.recovery_link)
        recovery_page = RecoveryPage(driver)
        assert recovery_page.wait_for_visibility_element(recovery_page.recovery_header)

    @allure.title("Тест: Восстановление пароля с помощью эл. посты")
    def test_recover_password_with_email(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_recovery_link()
        recovery_page = RecoveryPage(driver)
        test_email = TEST_EMAIL
        recovery_page.recover_password_with_email(test_email)
        assert recovery_page.wait_for_visibility_element(recovery_page.password_field)

    @allure.title("Тест: Подсвечивание поля пароля при нажатии на глаз")
    def test_show_hide_password_highlight_field(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_recovery_link()
        recovery_page = RecoveryPage(driver)
        recovery_page.request_password_recovery(TEST_EMAIL)
        recovery_page.toggle_password_visibility()
        assert recovery_page.is_password_input_active() == True
