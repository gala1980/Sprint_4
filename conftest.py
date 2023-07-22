import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(1200, 1500)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def browser():
    firefox_options = webdriver.FirefoxOptions()
    browser = webdriver.Firefox(options=firefox_options)
    browser.set_window_size(1200, 1500)
    browser.get("https://qa-scooter.praktikum-services.ru/")
    yield browser
    browser.quit()