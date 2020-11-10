from controllers.helper import Helper


task_8 = "//*[contains(@href,'/task_8')]"

BASE_URL = "https://testingcup.pgs-soft.com/"



class Main(Helper):

    def visit(self):
        self.driver.get(BASE_URL)


    def choose_task8(self):
        self.verify_exist_element(task_8).click()


    def get_current_url(self):
        return self.driver.current_url