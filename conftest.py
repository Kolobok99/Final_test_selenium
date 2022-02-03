import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption('--language')
    lang = browser_language

    options = Options()

    print(f"\n ---- START BROWSER with {lang=} ----")
    options.add_experimental_option('prefs',
                {'intl.accept_languages': lang})

    browser = webdriver.Chrome(options=options)
    #browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()