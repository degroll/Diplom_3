from selenium.webdriver.common.by import By


class MainPageLocators:
    MAKE_BURGER_TEXT = (By.XPATH, ".//h1[text()= 'Соберите бургер']")
    ORDER_FEED = (By.XPATH, ".//p[text()= 'Лента Заказов']")
    BUN_INGREDIENT = (By.XPATH, ".//a[contains(@href, '/ingredient/') and contains(., 'Флюоресцентная булка')]")
    SAUCE_INGREDIENT = (By.XPATH, ".//a[contains(@href, '/ingredient/') and contains(., 'Соус Spicy-X')]")
    FILLING_INGREDIENT = (By.XPATH, ".//a[contains(@href, '/ingredient/') and contains(., 'Мясо')]")
    ANY_INGREDIENT = (By.XPATH, "(.//a[contains(@href, '/ingredient/')])[1]")
    MODAL_WINDOW = (By.XPATH, ".//div[contains(@class, 'modal')]")
    MODAL_INGREDIENT_HEAD = (By.XPATH, ".// h2[text() = 'Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.XPATH, ".//div[contains(@class, 'modal')]//button[contains(@class, 'close')]")
    CONSTRUCTOR_BASKET = (By.XPATH, ".//ul[starts-with(@class, 'BurgerConstructor_basket')]")
    SAUCE_COUNTER = (By.XPATH, ".//a[contains(@href, '/ingredient/') and contains(., 'Соус')]//div[contains(@class, 'counter')]//p")
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    ORDER_NUMBER = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow')]")

    