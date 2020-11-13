from controllers.helper import Helper


task_8 = "//*[contains(@href,'/task_8')]"
task_nb = "//a[contains(@href,'/task_*')]"

BASE_URL = "https://testingcup.pgs-soft.com/"



class Main(Helper):

    def visit(self):
        self.driver.get(BASE_URL)


    def choose_task8(self):
        self.verify_exist_element(task_8).click()


    def count_test_tasks(self):
        return len(self.driver.find_elements_by_xpath(task_nb.replace("*","")))

    def choose_task_nb(self, nb):
        zadanie = task_nb.replace("*", str(nb))
        self.driver.find_element_by_xpath(zadanie).click()

    def get_current_url(self):
        return self.driver.current_url


    def back(self):
        self.driver.back()


    def get_text_from_element(self, element):
        return self.driver.find_element_by_xpath(element).text