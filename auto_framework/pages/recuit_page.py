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
    active_button = (By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]')
    user_name = (By.XPATH, '//p[@class="oxd-userdropdown-name"]')
    verify_edit_vacancy = (By.XPATH, '//h6[@class="oxd-text oxd-text--h6 orangehrm-main-title"]')
    cancel_button = (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--ghost"]')
    verify_vacancy = (By.XPATH, '//h5[@class="oxd-text oxd-text--h5 oxd-table-filter-title"]')
    vacancy_job_title = (By.XPATH, '(//div[@class="oxd-select-text-input"])[1]')
    hiring_manager_select = (By.XPATH, '(//div[@class="oxd-select-text-input"])[3]')
    search_button = (By.XPATH, '//button[@type="submit"]')
    record_found = (By.XPATH, '(//div[@role="row"])[2]')
    match_vacancy_name = (By.XPATH, '(//div[@role="row"]//div[@role="cell"])[2]//div')
    match_job_title = (By.XPATH, '(//div[@role="row"]//div[@role="cell"])[3]//div')
    match_hiring_manager = (By.XPATH, '(//div[@role="row"]//div[@role="cell"])[4]//div')
    match_status = (By.XPATH, '(//div[@role="row"]//div[@role="cell"])[5]//div')
    log_out = (By.XPATH, '//a[@href="/web/index.php/auth/logout"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_vacancy(self):
        self.click(self.vacancy)
    def click_add_vacancy(self):
        self.click(self.add_vacancy)

    def enter_vacancy_name(self, name):
        self.sendkey(self.vancancy_name, name)
        return name

    def select_job_title(self, title):
        self.click(self.job_title)
        job_title_option = (By.XPATH, f'//div[@role="option"]//span[text()="{title}"]')
        self.click(job_title_option)

    def type_description(self, description):
        self.sendkey(self.description_field, description)
        self.sendkey(self.description_field, description)
    
    def get_hiring_manager_name(self):
        user_name = self.find_element(self.user_name)
        return user_name.text

    def type_hiring_manager(self):
        self.click(self.hiring_manager_field)
        self.sendkey(self.hiring_manager_field, self.get_hiring_manager_name())
        first_option = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='listbox']//span")))[0]
        first_option.click()

    def enter_number_of_positions(self, number):
        self.sendkey(self.number_of_positions, number)

    def click_save_button(self):
        self.click(self.save_button)
    
    def click_active_button(self):
        self.click(self.active_button)

    def verify_vacancy_added(self):
        verify_title = self.find_element(self.verify_edit_vacancy)
        assert verify_title.is_displayed(), "Vacancy not added successfully"

    def click_cancel_button(self):
        self.click(self.cancel_button)

    def verify_vacancy_page(self):
        verify_vacancy = self.find_element(self.verify_vacancy)
        assert verify_vacancy.is_displayed(), "Not navigated to vacancy page"

    def select_job_title_filter(self, title):
        self.click(self.vacancy_job_title)
        job_title_option = (By.XPATH, f'//div[@role="option"]//span[text()="{title}"]')
        self.click(job_title_option)
    
    def select_hiring_manager(self):
        self.click(self.hiring_manager_select)
        name = self.find_element(self.user_name).text
        hiring_manager_option = (By.XPATH, f'//div[@role="option"]//span[text()="{name}"]')
        self.click(hiring_manager_option)
    
    def click_search_button(self):
        self.click(self.search_button)
    
    def verify_record_found(self):
        record = self.find_element(self.record_found)
        assert record.is_displayed(), "No record found"

    def verify_vacancy_details(self, vacancy_name, job_title, status="Closed"):
        name = self.find_element(self.match_vacancy_name).text
        title = self.find_element(self.match_job_title).text
        manager = self.find_element(self.match_hiring_manager).text
        stat = self.find_element(self.match_status).text
        assert name == vacancy_name, "Vacancy name does not match"
        assert title == job_title, "Job title does not match"
        assert manager == self.get_hiring_manager_name(), "Hiring manager does not match"
        assert stat == status, "Status does not match"

    def verify_all_vacancies(self, expected_vacancy_name, expected_job_title, expected_manager, expected_status):

        rows = self.driver.find_elements(By.XPATH, '//div[@role="row"][position()>1]')
        for idx, row in enumerate(rows, start=1):
        # Adjust the cell indexes if your table structure is different
            name = row.find_element(By.XPATH, './/div[@role="cell"][2]//div').text.strip()
            job_title = row.find_element(By.XPATH, './/div[@role="cell"][3]//div').text.strip()
            manager = row.find_element(By.XPATH, './/div[@role="cell"][4]//div').text.strip()
            status = row.find_element(By.XPATH, './/div[@role="cell"][5]//div').text.strip()
            assert name == expected_vacancy_name, f"Row {idx}: Vacancy name does not match"
            assert job_title == expected_job_title, f"Row {idx}: Job title does not match"
            assert manager == expected_manager, f"Row {idx}: Hiring manager does not match"
            assert status == expected_status, f"Row {idx}: Status does not match"
    
    def log_out_user(self):
        self.click(self.user_name)
        self.click(self.log_out)

    def test_add_vacancy_flow(self):
        self.click_vacancy()
        sleep(1)
        self.click_add_vacancy()
        sleep(1)
        self.enter_vacancy_name(self.vacancy_name)
        sleep(1)
        self.type_description("Responsible for overseeing the IT department and ensuring the smooth operation of all technology systems.")
        sleep(1)
        self.type_hiring_manager()
        sleep(1)
        self.enter_number_of_positions("3")
        sleep(1)
        self.click_active_button()
        sleep(1)
        self.click_save_button()
        sleep(1)
        self.verify_vacancy_added()
        sleep(1)
        self.click_cancel_button()
        sleep(1)
        self.verify_vacancy_page()
        sleep(1)
        self.select_job_title_filter("Automaton Tester")
        sleep(2)
        self.select_hiring_manager()
        sleep(2)
        self.click_search_button()
        sleep(2)
        self.verify_record_found()
        sleep(2)
        self.verify_all_vacancies(expected_vacancy_name=self.vacancy_name,expected_job_title="Automaton Tester",expected_manager=recuit_page.get_hiring_manager_name(),expected_status="Active")
        sleep(2)
        self.log_out_user()
        sleep(2)