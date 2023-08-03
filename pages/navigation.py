from pages.base_page import BasePage
from selenium import webdriver
import json


class NavigationPage(BasePage):


    def check_button_status_order(self, status_button, field_num_order,
                                  go_button, cancel_order_butt_loc):
        self.click_button(status_button)
        with open("num_order.json", mode="r", encoding="utf-8") as f:
            num_ord = json.load(f)
        nos = num_ord['numb_order']
        self.set_field(field_num_order, nos)
        self.wait_for_be_clickable(go_button)
        self.click_button(go_button)
        self.wait_for_load_page(cancel_order_butt_loc)
        expect_url = "https://qa-scooter.praktikum-services.ru/track?t="+nos
        return expect_url


    def check_navigation(self, start_url, link_button):
        self.set_url(start_url)
        self.click_button(link_button)
        self.wait_for_time()
        curr_url = self.get_current_url()
        return curr_url


    def navigation_between_window(self, start_url, link_button, butt_check_that_yandex):
        self.set_url(start_url)
        win_before = self.find_windows(0)
        self.click_button(link_button)
        self.wait_for_time()
        win_after = self.find_windows(1)
        self.switch_windows(win_after)
        self.wait_for_be_clickable(butt_check_that_yandex)
        return self.get_current_url()