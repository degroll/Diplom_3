import allure

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    @allure.step("Инициализируем драйвер")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открываем страницу")
    def open(self, url):
        self.driver.get(url)
        return self
    
    @allure.step("Ищем элемент")
    def find_element(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator)) 
        
    
    @allure.step("Ожидаем, когда элемент станет видимым")
    def wait_for_visibility_element(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Ожидаем, когда на элемент можно нажать")
    def wait_for_clicable_element(self, locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator))
    
    @allure.step("Нажимаем на элемент")
    def click_element(self, locator):
        element = self.wait_for_clicable_element(locator)
        try:
            element.click()
        except:
            element.location_once_scrolled_into_view
            action = ActionChains(self.driver)
            action.move_to_element(element).click().perform()

    @allure.step("Заполняем данные в элемент")
    def send_keys(self, locator, data):
        element = self.wait_for_clicable_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        element.clear()
        element.send_keys(data)

    @allure.step("Получаем атрибут элемента")
    def get_element_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)
    
    @allure.step("Ожидаем нужный url")
    def wait_for_url_contains(self, text):
        self.wait.until(expected_conditions.url_contains(text))

    @allure.step("Ожидаем, когда элемент исчезнет")
    def wait_for_invisibility_element(self, element):
        return self.wait.until(expected_conditions.invisibility_of_element_located(element))

    @allure.step("Получаем url страницы")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Получаем текст элемента")
    def get_element_text(self, locator):
        element = self.wait_for_visibility_element(locator)
        return element.text 

