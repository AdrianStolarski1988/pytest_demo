import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


browser = None


@pytest.fixture(scope='session')
def selenium_driver():
    global browser
    if browser is None:

        browser_options = Options()
        # chrome_options.add_argument('--headless')
        browser_options.add_argument('--no-sandbox')
        browser_options.add_argument('--disable-dev-shm-usage')

        browser = webdriver.Chrome(options=browser_options)
        browser.set_window_size(1920, 1080)
        browser.maximize_window()
        browser.implicitly_wait(5)

    yield browser
    browser.quit()
    return browser


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    timestamp = str(int(time.time()))
    print("raport")
    # if report.when == 'call':

        # TODO do zrobienia dodawanie screenow do raportow
        # if report.failed:
            # dodawanie url do raportow - lista screenow?
            # extra.append(pytest_html.extras.url('http://www.example.com/')

            # browser.save_screenshot("screenshots/" + timestamp + '.png')
            # extra.append(pytest_html.extras.image("screenshots/"+ timestamp + '.png'))
            # extra.append(pytest_html.extras.image("screenshots/error.png"))
    report.extra = extra
