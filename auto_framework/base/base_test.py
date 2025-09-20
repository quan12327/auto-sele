import pytest
from selenium import webdriver
from util.config_reader import ConfigReader

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, request):
        # Initialize Edge browser driver
        option = webdriver.EdgeOptions()
        option.add_argument("--headless")
        option.add_argument("--no-sandbox")
        option.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Edge(options=option)
        self.driver.maximize_window()  # Maximize the browser window
        base_url = ConfigReader.get_base_url()
        if base_url:
            self.driver.get(base_url)
        request.cls.driver = self.driver  # Assign driver to the test class
        yield  # Test execution happens here
        self.driver.quit()  # Close the browser after tests are done