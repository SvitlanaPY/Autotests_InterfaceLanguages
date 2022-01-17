# $ pytest -s -v --language=fr test_items.py


import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language_link(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket" and @type="submit"]')
    # button = browser.find_element(By.XPATH, '//button[@class="btnnnnn btn-lg btn-primary btn-add-to-basket"]')
    assert button is not None
