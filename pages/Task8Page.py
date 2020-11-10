from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import inspect
import logging
from selenium.webdriver.support.select import Select
from controllers.helper import Helper

card_select= "//*[@id='task8_form_cardType']"
name_input= "//*[@id='task8_form_name']"
cardNumber_input= "//*[@id='task8_form_cardNumber']"
cardCvv_input = "//*[@id='task8_form_cardCvv']"
cardMonth_select = "//*[@id='task8_form_cardInfo_month']"
cardYear_select = "//*[@id='task8_form_cardInfo_year']"
submit_btn = "//*[@name='task8_form[save]']"


success_alert = "//*[@class='alert alert-success1']"

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


class Page8(Helper):

    def visit(self):
        self.driver.get(BASE_URL)


    @screenshot
    def select_visa_cart(self):
        Select(self.verify_exist_element(card_select)).select_by_value("vs")


    def select_month_cart_experience(self, month):
        Select(self.driver.find_element_by_xpath(cardMonth_select)).select_by_value(month)


    def select_year_cart_experience(self, year):
        Select(self.driver.find_element_by_xpath(cardYear_select)).select_by_value(year)


    def fill_name(self, name):
        self.driver.find_element_by_xpath(name_input).send_keys(name)


    def fill_cart_cvv(self, cvv):
        self.driver.find_element_by_xpath(cardCvv_input).send_keys(cvv)


    @screenshot
    def fill_cart_number(self, number):
        self.driver.find_element_by_xpath(cardNumber_input).send_keys(number)


    def confirm_form(self):
        self.driver.find_element_by_xpath(submit_btn).click()


    def alert_is_present(self):
        aa =   self.verify_exist_element(success_alert)
        assert aa is True, "alert nie jest wyswietlony"



