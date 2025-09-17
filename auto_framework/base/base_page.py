from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Default wait time of 10 seconds

    def find_element(self, xpath):
        return self.wait.until(EC.presence_of_element_located(xpath))

    def click(self, xpath):
        self.wait.until(EC.element_to_be_clickable(xpath)).click()

    def sendkey(self, xpath, text):
        self.wait.until(EC.visibility_of_element_located(xpath)).send_keys(text)