from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    username_input = (By.XPATH, "//input[@name='username']")
    password_input = (By.XPATH, "//input[@name='password']")
    login_button = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.sendkey(self.username_input, username)
    
    def enter_password(self, password):
        self.sendkey(self.password_input, password)

    def click_login(self):
        self.click(self.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()