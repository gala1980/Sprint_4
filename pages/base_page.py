
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_loc(self, locator):
        return self.driver.find_element(*locator)  # Поиск локатора

    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text  # атрибут текст

    def get_inner_text_from_element(self, locator):
        return self.driver.find_element(*locator).get_attribute('innerText')  # атрибут текст

    def click_button(self, locator):
        return self.driver.find_element(*locator).click()  # нажатие на кнопку

    def set_field(self, locator, field):
        return self.driver.find_element(*locator).send_keys(field)  # ввод данных

    def set_enter(self, locator):
        return self.driver.find_element(*locator).send_keys(Keys.ENTER)  # ввод данных

    def execute_scroll_script(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def execute_click_script(self, element):
        return self.driver.execute_script("arguments[0].click();", element)

    def list_question_locators(self, number, locator): # Локаторы с вопросами из списка, number - номер вопроса
        metod, locator_link = locator
        locator_link = locator_link.format(number)
        display_question = ['id', locator_link]
        return display_question

    def list_answer_locators(self, number, locator): # Локаторы с ответами из списка, number - номер ответа
        metod, locator_link = locator
        locator_link = locator_link.format(number)
        display_answer = ['id', locator_link]
        return display_answer

    def wait_for_load_page(self, locator):
        return WebDriverWait(self.driver, 45)\
            .until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_be_clickable(self, locator):
        return WebDriverWait(self.driver, 45)\
            .until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_time(self):
        return WebDriverWait(self.driver, 450)

    def element_is_displayed(self, locator):
         return self.driver.find_element(*locator).is_displayed()

    def get_current_url(self):
        return self.driver.current_url

    def set_url(self, url):
        return self.driver.get(url)

    def find_windows(self, num):
        return self.driver.window_handles[num]

    def switch_windows(self, required_window):
        self.driver.switch_to.window(required_window)
        return
