from locators.locator_faq import LocatorsQuest
from pages.faq_page import FaqPage
import allure

@allure.title('Проверка Вопросов о важном')
class TestFAQ:
    # Используем фикстуру browser, которая закрывает окно после прохождения всех тестов в классе,
    # а не после каждого теста
    @allure.title('Вопрос о стоимости и оплате')
    @allure.description('Проверяем соответствие ожидаемого ответа вопросу')
    def test_check_faq_cost(self, browser):
        assert FaqPage(browser).check_answers_to_faq_true(0, LocatorsQuest.locator_question_temp,
                                                         LocatorsQuest.locator_answer_temp,
                                                         LocatorsQuest.ANSWER_LIST[0]) == True

    @allure.title('Вопрос о количестве самокатов')
    @allure.description('Проверяем соответствие ожидаемого ответа вопросу')
    def test_check_faq_some_scooter(self, browser):
        assert FaqPage(browser).check_answers_to_faq_true(1, LocatorsQuest.locator_question_temp,
                                                         LocatorsQuest.locator_answer_temp,
                                                         LocatorsQuest.ANSWER_LIST[1]) == True
    @allure.title('Вопрос Как рассчитывается время аренды?')
    @allure.description('Проверяем соответствие ожидаемого ответа вопросу')
    def test_check_faq_time_rent(self, browser):
        assert FaqPage(browser).check_answers_to_faq_true(2, LocatorsQuest.locator_question_temp,
                                                         LocatorsQuest.locator_answer_temp,
                                                         LocatorsQuest.ANSWER_LIST[2]) == True
    @allure.title('Вопрос Можно ли заказать самокат прямо на сегодня?')
    @allure.description('Проверяем соответствие ожидаемого ответа вопросу')
    def test_check_faq_today_scooter(self, browser):
        assert FaqPage(browser).check_answers_to_faq_true(3, LocatorsQuest.locator_question_temp,
                                                         LocatorsQuest.locator_answer_temp,
                                                         LocatorsQuest.ANSWER_LIST[3]) == True

    @allure.title('Вопрос Можно ли продлить заказ или вернуть самокат раньше?')
    @allure.description('Проверяем соответствие ожидаемого ответа вопросу')
    def test_check_faq_extend_order(self, browser):
        assert FaqPage(browser).check_answers_to_faq_true(4, LocatorsQuest.locator_question_temp,
                                                         LocatorsQuest.locator_answer_temp,
                                                         LocatorsQuest.ANSWER_LIST[4]) == True

    @allure.title('Вопрос о зарядке')
    @allure.description('Проверяем соответствие ожидаемого ответа вопросу')
    def test_check_faq_charge_scooter(self, browser):
        assert FaqPage(browser).check_answers_to_faq_true(5, LocatorsQuest.locator_question_temp,
                                                         LocatorsQuest.locator_answer_temp,
                                                         LocatorsQuest.ANSWER_LIST[5]) == True
    @allure.title('Вопрос Можно ли отменить заказ?')
    @allure.description('Проверяем соответствие ожидаемого ответа вопросу')
    def test_check_faq_cancel_order(self, browser):
        assert FaqPage(browser).check_answers_to_faq_true(6, LocatorsQuest.locator_question_temp,
                                                         LocatorsQuest.locator_answer_temp,
                                                         LocatorsQuest.ANSWER_LIST[6]) == True
    @allure.title('Вопрос о доставке за МКАД')
    @allure.description('Проверяем соответствие ожидаемого ответа вопросу')
    def test_check_faq_over_MRR(self, browser):
        assert FaqPage(browser).check_answers_to_faq_true(7, LocatorsQuest.locator_question_temp,
                                                         LocatorsQuest.locator_answer_temp,
                                                         LocatorsQuest.ANSWER_LIST[7]) == True