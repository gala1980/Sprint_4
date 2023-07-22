from locators.locator_navigat import LocatorNavigation
from pages.navigation import NavigationPage
from pages.base_page import BasePage
import allure
# проверяем переход на страницу проверки заказа
# Ожидаемый результат - текущий url совпадает с ожидаемым
class TestNavigation:

    @allure.title('Проверка статуса заказа')
    @allure.description('Вводим номер заказа, проверяем, что '
                        'система перешла на страницу c соответствующим номером')
    def test_navigat_to_status_page(self, driver):
        expect_url = NavigationPage(driver).check_button_status_order(LocatorNavigation.status_button, LocatorNavigation.field_num_order,
                                                         LocatorNavigation.go_button, LocatorNavigation.cancel_order_butt)
        current_url = BasePage(driver).get_current_url()

        assert expect_url == current_url

    @allure.title('Проверка перехода на страницу Самоката')
    @allure.description('Нажимаем на кнопку "Самокат", проверяем, что '
                        'система перешла на страницу Самоката: https://qa-scooter.praktikum-services.ru/')
    def test_navigat_to_main_page_scooter(self, driver):
        NavigationPage(driver).check_button_status_order(LocatorNavigation.status_button,
                                                                      LocatorNavigation.field_num_order,
                                                                      LocatorNavigation.go_button,
                                                                      LocatorNavigation.cancel_order_butt)
        start_url = BasePage(driver).get_current_url()

        check_url = NavigationPage(driver).check_navigation(start_url, LocatorNavigation.link_scooter_button)

        assert check_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка перехода на страницу Яндекса')
    @allure.description('Нажимаем на кнопку "Яндекс", проверяем, что '
                        'система перешла на страницу Дзена: https://dzen.ru/?yredirect=true')
    def test_navigat_to_main_page_yandex(self, driver):
        NavigationPage(driver).check_button_status_order(LocatorNavigation.status_button,
                                                         LocatorNavigation.field_num_order,
                                                         LocatorNavigation.go_button,
                                                         LocatorNavigation.cancel_order_butt)
        start_url = BasePage(driver).get_current_url()

        check_url = NavigationPage(driver).navigation_between_window(start_url, LocatorNavigation.link_yandex_button,
                                                                     LocatorNavigation.check_that_yandex)

        assert check_url == 'https://dzen.ru/?yredirect=true'