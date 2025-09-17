from base.base_page import BasePage
from selenium.webdriver.common.by import By

class DashBoardPage(BasePage):
    recuit = (By.XPATH, '//a[@href="/web/index.php/recruitment/viewRecruitmentModule"]')
    def __init__(self, driver):
        super().__init__(driver)

    def click_recruit(self):
        self.click(self.recuit)
