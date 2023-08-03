from selenium.webdriver.common.by import By

class LocatorNavigation:

    status_button = By.XPATH, ".//button[contains(text(),'Статус заказа')]"
    field_num_order = [By.XPATH, ".//input[@placeholder='Введите номер заказа']"]
    go_button = [By.XPATH, ".//button[contains(text(),'Go!')]"]
    cancel_order_butt = [By.XPATH, ".//button[contains(text(),'Отменить заказ')]"]
    link_scooter_button = By.XPATH, ".//a[starts-with(@class,'Header_LogoScooter')]"
    link_yandex_button = By.XPATH, ".//a[starts-with(@class,'Header_LogoYandex')]"
    check_that_yandex = By.XPATH, ".//button[contains(text(),'Найти')]"
