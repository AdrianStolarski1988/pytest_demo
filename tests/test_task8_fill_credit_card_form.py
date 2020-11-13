import pytest
import time

from pages import MainPage
from pages import Task8Page

@pytest.mark.usefixtures("selenium_driver")
class BasicTest:
    pass


class TestTestingCupSite(BasicTest):

    def test_choose_all_tasks(self, selenium_driver):
        """
        scenario:
        1. entrence to site and counter numbers of tests
        2. in loop enterence to test and checking correction of url
        3. back to site with tasks and repeat step 2
        """
        errors = []

        # entrence to tasks site
        site = MainPage.Main(selenium_driver)
        site.visit()

        #counter of tasks box
        tasks = site.count_test_tasks()


        for i in range(1,tasks):

            # clicking on box with task
            site.choose_task_nb(i)

            # checking url
            strona = site.get_current_url()

            # checking correction of url
            if not "/task_{}".format(str(i)) in strona:
                errors.append("not correct url number %s" % str(i))
            site.back()


        #if array of errors is not empty test will be failed
        assert not errors, "errors occured:\n{}".format("\n".join(errors))


    def test_send_confirm_credit_card(self, selenium_driver):
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


