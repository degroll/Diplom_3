from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    RECOVER_HEADER = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    EMAIL_FIELD = (By.NAME, "name")
    RECOVER_BUTTON = (By.XPATH, ".//button[text()= 'Восстановить']")
    PASSWORD_FIELD = (By.NAME, "Введите новый пароль")
    SHOW_HIDE_ICON = (By.XPATH, ".//div[contains(@class, 'input__icon')]")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/parent::div")

