from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test_click_type():
    # Initialize Edge browser driver
    driver = webdriver.Edge()
    driver.maximize_window()  # Maximize the browser window

    # Open the target web page
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    sleep(1)  # Wait for the page to load

    # Locate the username and password input fields
    username = driver.find_element(By.XPATH, '//input[@id="my-text-id"]')
    password = driver.find_element(By.XPATH, '//input[@name="my-password"]')

    # Enter text into the username and password fields
    username.send_keys("abc")
    password.send_keys("123")

    # Locate and click the submit button
    submit = driver.find_element(By.XPATH,"//button[@type='submit']")
    submit.click()

    sleep(3)  # Wait to observe the result

    # Close the browser
    driver.quit