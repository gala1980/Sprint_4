import pytest

from locators.locator_faq import LocatorsQuest
from locators.data import DataVar
from pages.faq_page import FaqPage

import allure

@allure.title('Проверка Вопросов о важном')
class TestFAQ:
    # Используем фикстуру browser, которая закрывает окно после прохождения всех тестов в классе,
    # а не после каждого теста

    @allure.description('Проверяем соответствие ожидаемого ответа вопросу')
    @pytest.mark.parametrize("number", [int(i) for i in range(8)])
    def test_check_faq_cost(self, browser, number):

            cost = FaqPage(browser).check_answers_to_faq_true(number, LocatorsQuest.locator_question_temp,
                                                         LocatorsQuest.locator_answer_temp,
                                                         DataVar.ANSWER_LIST[number])
            assert cost == True
