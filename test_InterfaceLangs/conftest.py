from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver

# Можно задать значение параметра по умолчанию,
# чтобы в командной строке необязательно было указывать параметр --browser_name,
# например, так:
def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        # default=None,
        default="de",
        help="Choose language"
    )


@pytest.fixture(scope="function")
def browser(request):
    # Логика обработки командной строки.
    # Для запроса значения параметра с командной строки мы можем вызвать команду:
    user_language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
