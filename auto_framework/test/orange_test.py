from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dash_board_page import DashBoardPage
from pages.recuit_page import RecuitPage
from time import sleep
from datetime import datetime

def random_name(prefix="Test"):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # YYYYMMDDHHMMSS
    return f"{prefix}_{timestamp}"

class TestOrangeHRM(BaseTest):

    vacancy_name = random_name("Vacancy")

    def test_login(self):
        username = "Admin"
        password = "admin123"
        
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        sleep(2)

    def click_recruit(self):
        dash_board_page = DashBoardPage(self.driver)
        dash_board_page.click_recruit()
        sleep(1)
    
    def test_add_vacancy(self):
        self.click_recruit()
        recuit_page = RecuitPage(self.driver)
        recuit_page.click_vacancy()
        sleep(1)
        recuit_page.click_add_vacancy()
        sleep(1)
        recuit_page.enter_vacancy_name(self.vacancy_name)
        sleep(1)
        recuit_page.select_job_title("Automaton Tester")
        sleep(1)
        recuit_page.type_description("Responsible for overseeing the IT department and ensuring the smooth operation of all technology systems.")
        sleep(1)
        recuit_page.type_hiring_manager()
        sleep(1)
        recuit_page.enter_number_of_positions("3")
        sleep(1)
        recuit_page.click_active_button()
        sleep(1)
        recuit_page.click_save_button()
        sleep(1)
        recuit_page.verify_vacancy_added()
        sleep(1)
        recuit_page.click_cancel_button()
        sleep(1)
        recuit_page.verify_vacancy_page()
        sleep(1)
        recuit_page.select_job_title_filter("Automaton Tester")
        sleep(2)
        recuit_page.select_hiring_manager()
        sleep(2)
        recuit_page.click_search_button()
        sleep(2)
        recuit_page.verify_record_found()
        sleep(2)
        recuit_page.verify_all_vacancies(expected_vacancy_name=self.vacancy_name,expected_job_title="Automaton Tester",expected_manager=recuit_page.get_hiring_manager_name(),expected_status="Active")
        sleep(2)
        recuit_page.log_out_user()
        sleep(2)
        # You can add a timestamp to make the vacancy name unique if needed
        # timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        # Add more steps as needed, like saving the vacancy
        # For example:
        # recuit_page.click_save_button()
        # sleep(2)