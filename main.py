from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# click submit
submit_button = driver.find_element(By.CSS_SELECTOR, value="button")
submit_button.click()

# back to web-form
driver.back