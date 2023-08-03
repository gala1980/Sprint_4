from pages.base_page import BasePage
from selenium import webdriver

class FaqPage(BasePage):
    def check_answers_to_faq_true(self, num, quest_loc, answer_loc, text_answer):
        quest_num = self.list_question_locators(num, quest_loc)
        answer_num = self.list_answer_locators(num, answer_loc)
        quest_exec = self.find_element_loc(quest_num)
        self.execute_scroll_script(quest_exec)
        self.execute_click_script(quest_exec)
        answer = self.get_inner_text_from_element(answer_num)
        print(answer)
        print(text_answer)
        return answer == text_answer
