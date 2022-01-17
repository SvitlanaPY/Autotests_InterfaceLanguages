import pytest
from selenium import webdriver
import time

# link = "http://selenium1py.pythonanywhere.com/"                                     # no button
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"  # button exists


def test_add_backet_button_exists(browser):
    browser.get(link)
    browser.implicitly_wait(5)

    time.sleep(30)

    add_basket_buttons = browser.find_elements_by_css_selector("#add_to_basket_form > button")

    if (not add_basket_buttons):
        print("\n Button not found !!! ", add_basket_buttons)
    else:
        print("\n Button(s) found : ", len(add_basket_buttons))

    assert add_basket_buttons, "no ADD BACKET button"
