from pages.base_page import BasePage
import json


class OrderPage(BasePage):

    def order_part_button_order_click(self, order_butt):
        self.click_button(order_butt)

    def order_part_execute_order(self, butt_order):
        quest_exec = self.find_element_loc(butt_order)
        self.execute_scroll_script(quest_exec)
        self.wait_for_load_page(butt_order)

    def order_part_scooter_drv(self, scoot_drv_text, firstname_loc, firstname,
                  surname_loc, surname, addres_loc, address, phone_loc, phone, railway_list,
                  railway_station, next_button):
        self.wait_for_load_page(scoot_drv_text)
        self.set_field(firstname_loc, firstname)
        self.set_field(surname_loc, surname)
        self.set_field(addres_loc, address)
        self.set_field(phone_loc, phone)
        self.click_button(railway_list)
        self.click_button(railway_station)
        self.click_button(next_button)

    def order_part_rent(self, date_delivery_loc, date_delivery, period_rent_loc,
                            choose_period_rent_loc, form_order_button_loc, confirm_order_text_loc,
                            confirm_order_button_loc, text_order_success_loc):
        self.set_field(date_delivery_loc, date_delivery)
        self.set_enter(date_delivery_loc)
        self.click_button(period_rent_loc)
        self.click_button(choose_period_rent_loc)
        self.click_button(form_order_button_loc)
        self.wait_for_load_page(confirm_order_text_loc)
        self.click_button(confirm_order_button_loc)
        self.wait_for_load_page(text_order_success_loc)
        text_order = self.get_inner_text_from_element(text_order_success_loc)
        num_order = "".join(text_order.split()).split(".")[0][25:]
        numbDict = {
            "numb_order": num_order}
        with open("num_order.json", mode="w+", encoding="utf-8") as f:
            json.dump(numbDict, f, indent=4, ensure_ascii=False) # Записываем в файл данные Заказа
        print(num_order)
        self.wait_for_time()
        return num_order


    def order_part_check_order(self, check_status_butt_loc, cancel_order_butt_loc, view_order_butt):
        self.click_button(check_status_butt_loc)
        self.wait_for_load_page(cancel_order_butt_loc)
        but_cancel = self.element_is_displayed(cancel_order_butt_loc)
        but_view_order = self.element_is_displayed(view_order_butt)
        return but_view_order & but_cancel #Возвращаем результат видимости кнопок посмотреть и Отменить Заказ






