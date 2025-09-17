from concurrent.futures import wait
from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RecuitPage(BasePage):
    vacancy = (By.XPATH, "//a[text() = 'Vacancies']")
    add_vacancy = (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
    vancancy_name = (By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[2]')
    job_title = (By.XPATH, '//div[@tabindex="0"]')
    description_field = (By.XPATH, '//textarea[@placeholder="Type description here"]')
    hiring_manager_field = (By.XPATH, '//input[@placeholder="Type for hints..."]')
    number_of_positions = (By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[3]')
    save_button = (By.XPATH, '//button[@type="submit"]')

    def __init__(self, driver):
        super().__init__(driver)
    def click_vacancy(self):
        self.click(self.vacancy)
    def click_add_vacancy(self):
        self.click(self.add_vacancy)

    def enter_vacancy_name(self, name):
        self.sendkey(self.vancancy_name, name)

    def select_job_title(self, title):
        self.click(self.job_title)
        job_title_option = (By.XPATH, f'//div[@role="option"]//span[text()="{title}"]')
        self.click(job_title_option)

    def type_description(self, description):
        self.sendkey(self.description_field, description)
        self.sendkey(self.description_field, description)
    
    def type_hiring_manager(self, manager_name):
        self.click(self.hiring_manager_field)
        self.sendkey(self.hiring_manager_field, manager_name)
        first_option = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='listbox']//span")))[0]
        first_option.click()

    def enter_number_of_positions(self, number):
        self.sendkey(self.number_of_positions, number)

    def click_save_button(self):
        self.click(self.save_button)