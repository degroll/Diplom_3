from selenium.webdriver.common.by import By


class PesonalAccountLocators:
    NAME_FIELD = (By.XPATH, ".//input[@name= 'Name']")
    ORDER_HISTORY = (By.XPATH, ".//a[text()='История заказов']")
    LOGOUT = (By.XPATH, ".//button[text()='Выход']")
    