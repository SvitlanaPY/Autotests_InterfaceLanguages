import time

from selenium.common.exceptions import NoSuchElementException
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def test_add_button_present(browser):
    browser.get(link)
    btn_add = ".btn-add-to-basket"
    def check_exists_by_css(css):
        try:
            browser.find_element_by_css_selector(css)
        except NoSuchElementException:
            return False
        return True
    assert check_exists_by_css(btn_add) == True, "Check 'Add button' present"
