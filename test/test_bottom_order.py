from locators.locator_order import LocatorOrder
from pages.order_page import OrderPage
from pages.base_page import BasePage
import allure
# Проверяем Заказ по кнопке снизу.
# ОР - Заказ сформирован, если есть кнопки "Посмотреть" и "Отменить Заказ". Переход на страницу с данными Заказа
class TestBottomOrder:

    @allure.title('Проверка создания заказа.')
    @allure.description('Проверяем возможность заказа по кнопке "Заказть" в нижней части экрана')
    @allure.step ('Нажимаем на кнопку "Заказать, вводим данные клиента: Имя, Фамилия ,телефон, адрес доставки, метро ')
    @allure.step('Нажимаем на кнопку "Далее", вводим данные аренды: дата доставки, длительность, цвет самоката, комментарий')
    @allure.step('Нажимаем на кнопку "Заказать, проверяем ,что заказ сформирован, записываем номер заказа в файл,'
                 'для дальнейшего использования')
    def test_check_bottom_order(self, driver):
        BasePage(driver).find_element_loc(LocatorOrder.top_order_button)
        OrderPage(driver).order_part_execute_order(LocatorOrder.buttom_order_button)
        BasePage(driver).wait_for_be_clickable(LocatorOrder.buttom_order_button)
        OrderPage(driver).order_part_button_order_click(LocatorOrder.buttom_order_button)
        OrderPage(driver) \
                .order_part_scooter_drv(LocatorOrder.scooter_dr_text,
                                        LocatorOrder.firstname, LocatorOrder.list_firstname[0],
                                        LocatorOrder.surname, LocatorOrder.list_surname[0],
                                        LocatorOrder.addsress, LocatorOrder.list_address[0],
                                        LocatorOrder.phone_number, LocatorOrder.list_phone[0],
                                        LocatorOrder.list_railway_button, LocatorOrder.railway_station,
                                        LocatorOrder.next_button)
        OrderPage(driver).order_part_rent(LocatorOrder.date_delivery, LocatorOrder.list_delivery[0],
                                              LocatorOrder.period_rent, LocatorOrder.choose_period_rent,
                                              LocatorOrder.form_order_button, LocatorOrder.confirm_order_text,
                                              LocatorOrder.confirm_order_button, LocatorOrder.text_order_success)
        check_order = OrderPage(driver).order_part_check_order(LocatorOrder.check_status_butt,
                                                                   LocatorOrder.cancel_order_butt,
                                                                   LocatorOrder.view_order_butt)
        assert check_order == True
