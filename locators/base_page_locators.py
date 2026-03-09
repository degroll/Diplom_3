from selenium.webdriver.common.by import By


class BasePageLocators:
    PERSONAL_ROOM = (By.XPATH, ".//p[text()='Личный Кабинет']")
    CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")