from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.NAME, "name")
    PASSWORD_FIELD = (By.NAME, "Пароль")
    RECOVER_LINK = (By.XPATH, ".//a[text()= 'Восстановить пароль']")
    LOGIN_HEADER = (By.XPATH, "//h2[contains(text(), 'Вход')]")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()=('Войти')]")

