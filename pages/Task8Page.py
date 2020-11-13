from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging
from selenium.webdriver.support.select import Select
from controllers.helper import Helper
from pages.MainPage import Main

card_select= "//*[@id='task8_form_cardType']"
name_input= "//*[@id='task8_form_name']"
cardNumber_input= "//*[@id='task8_form_cardNumber']"
cardCvv_input = "//*[@id='task8_form_cardCvv']"
cardMonth_select = "//*[@id='task8_form_cardInfo_month']"
cardYear_select = "//*[@id='task8_form_cardInfo_year']"
submit_btn = "//*[@name='task8_form[save]']"


success_alert = "//*[@class='alert alert-success']"
danger_alert = "//*[@class='alert alert-danger']"

BASE_URL = "https://testingcup.pgs-soft.com/task_8"

def screenshot(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (TimeoutException, NoSuchElementException) as e:
            args[0].driver.save_screenshot("screenshots/error.png")
            logging.error(e)
            return False
    return wrapper


class Page8(Main):

    def visit(self):
        self.driver.get(BASE_URL)


    def select_visa_cart(self):
        Select(self.verify_exist_element(card_select)).select_by_value("vs")


    def select_month_cart_experience(self, month):
        Select(self.verify_exist_element(cardMonth_select)).select_by_value(month)


    def select_year_cart_experience(self, year):
        Select(self.driver.find_element_by_xpath(cardYear_select)).select_by_value(year)


    def fill_name(self, name):
        self.driver.find_element_by_xpath(name_input).send_keys(name)


    def fill_cart_cvv(self, cvv):
        self.driver.find_element_by_xpath(cardCvv_input).send_keys(cvv)


    def fill_cart_number(self, number):
        self.driver.find_element_by_xpath(cardNumber_input).send_keys(number)


    def confirm_form(self):
        self.driver.find_element_by_xpath(submit_btn).click()


    def alert_is_present(self):
        alert = self.check_element_is_displayed(success_alert)
        assert alert is True, "expected alert is not displayed"


    def an_invalid_card_message_is_displayed(self, msg):
        alert = self.get_text_from_element(danger_alert)
        assert alert == msg, "displayed alert {0} is not equal with expected {1}" .format(alert, msg)


