import allure
from locators.locator_order import LocatorOrder
from locators.data import DataVar
from pages.order_page import OrderPage
from pages.base_page import BasePage

# Проверяем Заказ по кнопке сверху.
# ОР - Заказ сформирован, если есть кнопки "Посмотреть" и "Отменить Заказ". Переход на страницу с данными Заказа
class TestTopOrder:

    @allure.title('Проверка создания заказа.')
    @allure.description('Проверяем возможность заказа по кнопке "Заказть" в верхней части экрана. '
                        'Тест позитивный, проверяется три раза')
    @allure.step ('Нажимаем на кнопку "Заказать, вводим данные клиента: Имя, Фамилия ,телефон, адрес доставки, метро ')
    @allure.step('Нажимаем на кнопку "Далее", вводим данные аренды: дата доставки, длительность, цвет самоката, комментарий')
    @allure.step('Нажимаем на кнопку "Заказать, проверяем ,что заказ сформирован, записываем номер заказа в файл,'
                 'для дальнейшего использования')
    def test_check_top_order(self, driver):
        for i in range(0,3):
            OrderPage(driver).order_part_button_order_click(LocatorOrder.top_order_button)
            OrderPage(driver)\
                .order_part_scooter_drv(LocatorOrder.scooter_dr_text,
                                        LocatorOrder.firstname, DataVar.list_firstname[i],
                                        LocatorOrder.surname, DataVar.list_surname[i],
                                        LocatorOrder.addsress, DataVar.list_address[i],
                                        LocatorOrder.phone_number, DataVar.list_phone[i],
                                        LocatorOrder.list_railway_button, LocatorOrder.railway_station,
                                        LocatorOrder.next_button)
            OrderPage(driver).order_part_rent(LocatorOrder.date_delivery, DataVar.list_delivery[i],
                                                 LocatorOrder.period_rent, LocatorOrder.choose_period_rent,
                                                 LocatorOrder.form_order_button, LocatorOrder.confirm_order_text,
                                                 LocatorOrder.confirm_order_button, LocatorOrder.text_order_success)
            check_order = OrderPage(driver).order_part_check_order(LocatorOrder.check_status_butt, LocatorOrder.cancel_order_butt,
                                                        LocatorOrder.view_order_butt)
            assert check_order == True

