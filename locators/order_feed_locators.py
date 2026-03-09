from selenium.webdriver.common.by import By


class OrderFeedLocators:
    FIRST_ORDER = (By.XPATH, "(.//li[contains(@class, 'OrderHistory')])[1]")
    ORDER_MODAL_CLOSE = (By.XPATH, "(.//div[contains(@class, 'modal')]//button)[2]")
    TOTAL_ORDER_COUNTER = (By.XPATH, ".//p[text()= 'Выполнено за все время:']/following-sibling::p")
    TODAY_ORDER_COUNTER = (By.XPATH, ".//p[text()= 'Выполнено за сегодня:']/following-sibling::p")
    FIRST_ORDER_IN_PROGRESS = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListRead')]/li[1]")
    USER_ORDER_IN_FEED = (By.XPATH, ".//*[text()={order_number}]")

   
