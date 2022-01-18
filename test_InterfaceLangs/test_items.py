# $ pytest -s -v --language=fr test_items.py


import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_basket_button_exists(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket" and @type="submit"]')
    # button = browser.find_element(By.XPATH, '//button[@class="btnnnnn btn-lg btn-primary btn-add-to-basket"]')
    assert button is not None

# Можно было все запихнуть в один assert, без дополнительных переменных, с проверкой видимости, но так тоже можно.
# Пример:
# assert expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'button.btn-add-to-basket')), 'Cannot locate button on page' expected_conditions
# вернет True, если кнопка есть и видима, и False, если кнопки нет - assert встретив False выбросит исключение.
