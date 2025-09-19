import pytest
from selenium import webdriver
import requests

class TestSetup:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        # Create a requests session for API testing
        session = requests.Session()
        request.cls.session = session

        # Set up Selenium Edge WebDriver for UI testing
        option = webdriver.EdgeOptions()
        option.add_argument("--headless")
        option.add_argument("--no-sandbox")
        option.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Edge(options=option)
        driver.maximize_window()
        request.cls.driver = driver

        yield  # Run the tests

        # Teardown: close browser and session
        driver.quit()
        session.close()