import pytest
import requests
from base.base_api import TestSetup
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class TestApilocation(TestSetup):
    def setup_method(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(5) 
        try:
            self.driver.find_element(By.NAME, "username").send_keys("Admin")
            self.driver.find_element(By.NAME, "password").send_keys("admin123")
            self.driver.find_element("css selector", "button[type='submit']").click()
        except NoSuchElementException:
            raise Exception("Login failed, element not found.")
        
        
        self.driver.implicitly_wait(5)
        for cookie in self.driver.get_cookies():
            self.session.cookies.set(cookie['name'], cookie['value'])
    @pytest.mark.api
    @pytest.mark.parametrize("loc_id, loc_name",[(5,"Texas R&D"),],)
    def test_api_location(self, loc_id, loc_name):
        response = requests.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/dashboard/employees/locations"
            )
        self.driver.implicitly_wait(5)
        
        assert (
            response.status_code == 200 
        ), f"Expected status code 200 but got {response.status_code}"

        try:
            data = response.json()

            locations = data.get("data", {})

            location_dict = {locations["id"]: locations["name"] for locations in locations}

            assert location_dict.get(loc_id) == loc_name, "Location name does not match"
            self.driver.implicitly_wait(5)
        except ValueError:
            assert False, "Response is not in JSON format"