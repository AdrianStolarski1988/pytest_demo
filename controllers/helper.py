import logging
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Helper(object):

    

    def __init__(self, driver):
        self.driver = driver



    def verify_exist_element(self, element):
        try:
            return WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.XPATH, element)))
        except (TimeoutException, NoSuchElementException) as e:
            # self.driver.save_screenshot("screenshots/not_find_expected_element.png")
            return False
        finally:
            pass


    def check_element_is_displayed(self, element):
        try:
            self.driver.find_element_by_xpath(element)
        except NoSuchElementException as e:
            logging.error(e)
            logging.warning("not found element")
            return False
        return True

