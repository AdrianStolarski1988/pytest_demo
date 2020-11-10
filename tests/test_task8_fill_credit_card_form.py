import pytest
from pages import MainPage
from pages import Task8Page

def test_choose_task(selenium_driver):
    """
    scenario:
    1. entrance to home site  https://testingcup.pgs-soft.com
    2. clicking on task8 button
    3. checking correction url

    """

    glowna = MainPage.Main(selenium_driver)
    glowna.visit()

    glowna.choose_task8()

    assert "/task_8" in glowna.get_current_url()

def test_send_confirm_credit_card(selenium_driver):
    """
    scenario
    1. entrance on the home site
    2. checking of display form
    3. filling the form
    4. checking the display of the alert

    """

    #entrance on the home site
    task= Task8Page.Page8(selenium_driver)
    task.visit()


    #filling the form
    task.select_visa_cart()
    task.fill_cart_number("4111111111111111")
    task.fill_name("Ad rian")
    task.fill_cart_cvv("123")
    task.select_month_cart_experience("12")
    task.select_year_cart_experience("2030")
    task.confirm_form()

    #checking the display of the alert
    task.alert_is_present()
