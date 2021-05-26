import pytest
import time

from pages import MainPage
from pages import Task8Page

@pytest.mark.usefixtures("selenium_driver")
class BasicTest:
    pass


class TestTestingCupSite(BasicTest):

    @pytest.fixture(name="site", scope="function")
    def visit_main_site(self, selenium_driver):
        """entrance to site before tests"""

        site = MainPage.Main(selenium_driver)
        site.visit()
        yield site

    @pytest.fixture(name="task8")
    def visit_site8(self, selenium_driver):
        """entrance to task8 site before tests"""

        task = Task8Page.Page8(selenium_driver)
        task.visit()
        yield task

    def test_choose_all_tasks_in_main_site(self, site):
        """
        scenario:
        1. entrance to site and counter numbers of tests
        2. in loop enterance to test and checking correction of url
        3. back to site with tasks and repeat step 2
        """
        errors = []

        # entrence to tasks site
        # site = MainPage.Main(selenium_driver)
        # site.visit()

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


    def test_task8_register_the_card_correctly(self, task8):
        """
        scenario
        1. entrance on the home site
        2. checking of display form
        3. filling the form
        4. checking the display of the alert

        """

        #entrance on the home site
        # task= Task8Page.Page8(selenium_driver)
        # task.visit()


        #filling the form
        task8.select_visa_cart()
        task8.fill_cart_number("4111111111111111")
        task8.fill_name("Ad rian")
        task8.fill_cart_cvv("123")
        task8.select_month_cart_experience("12")
        task8.select_year_cart_experience("2030")
        task8.confirm_form()

        #checking the display of the alert
        task8.alert_is_present()


    def test_task8_send_the_form_with_the_expiry_date_of_cart(self, task8):
        """
        scenario
        1. entrance on the home site
        2. checking of display form
        3. filling the form with incorrect month
        4. checking the display of the alert

        """

        #filling the form
        task8.select_visa_cart()
        task8.fill_cart_number("4111111111111111")
        task8.fill_name("Ad rian")
        task8.fill_cart_cvv("123")
        task8.select_month_cart_experience("01")
        task8.select_year_cart_experience("2021")
        task8.confirm_form()

        #checking the display of the alert
        task8.an_invalid_card_message_is_displayed("Upłynął termin ważności karty")
