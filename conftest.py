import os

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

browser = None


def browser_config(browser_options):
    browser_options.add_argument('--headless')
    browser_options.add_argument('--no-sandbox')
    browser_options.add_argument('--disable-dev-shm-usage')
    return browser_options


@pytest.fixture(params=['chrome', 'firefox'], scope="class")
def selenium_driver(request):
    global browser

    if request.param == "chrome":
        browser_options = ChromeOptions()
        browser_config(browser_options)
        browser = webdriver.Chrome(options=browser_options)

    if request.param == "firefox":
        browser_options = FirefoxOptions()
        browser_config(browser_options)
        browser = webdriver.Firefox(options=browser_options)

    browser.maximize_window()
    browser.implicitly_wait(5)
    request.cls.browser = browser
    yield browser
    browser.quit()

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     timestamp = str(int(time.time()))
#
#     if report.when == 'call':
#
#     # TODO do zrobienia dodawanie screenow do raportow
#         if report.failed:
#             #dodawanie url do raportow - lista screenow?
#             # extra.append(pytest_html.extras.url('http://www.example.com/')
#             screenshot_name = "tests/screenshots/" + timestamp + ".png"
#             browser.save_screenshot(screenshot_name)
#             extra.append(pytest_html.extras.image(screenshot_name))
#     report.extra = extra
