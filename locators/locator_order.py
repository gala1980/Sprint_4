from selenium.webdriver.common.by import By

class LocatorOrder:

    top_order_button = By.XPATH, ".//div[starts-with(@class,'Header')]/button[contains(text(),'Заказать')]"
    buttom_order_button = By.XPATH, ".//div[starts-with(@class,'Home')]/button[contains(text(),'Заказать')]"
    scooter_dr_text = By.XPATH, ".//div[contains(text(),'Для кого самокат')]"
    firstname = [By.XPATH, ".//input[@placeholder='* Имя']"]
    surname = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    addsress = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    list_railway_button = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    railway_station = [By.XPATH, ".//ul[@class='select-search__options']/li[5]"]
    phone_number = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    next_button = [By.XPATH, ".//button[contains(text(),'Далее')]"]
    date_delivery = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    period_rent = [By.XPATH, ".//div[@class='Dropdown-root']"]
    choose_period_rent = [By.XPATH, ".//div[@class='Dropdown-menu']/div[1]"]
    form_order_button = [By.XPATH, ".//div[starts-with(@class,'Order_Button')]/button[contains(text(),'Заказать')]"]
    confirm_order_text = [By.XPATH, ".//div[contains(text(),'Хотите оформить заказ?')]"]
    confirm_order_button = [By.XPATH, ".//button[contains(text(),'Да')]"]
    text_order_success = [By.XPATH, ".//div[contains(text(),'Заказ оформлен')]"]
    check_status_butt = [By.XPATH, ".//button[contains(text(),'Посмотреть статус')]"]
    cancel_order_butt = [By.XPATH, ".//button[contains(text(),'Отменить заказ')]"]
    view_order_butt = By.XPATH, ".//button[contains(text(),'Посмотреть')]"
