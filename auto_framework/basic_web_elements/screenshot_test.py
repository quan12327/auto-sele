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

    # Take a screenshot of the username input element and save as 'username.png'
    driver.find_element(By.XPATH, '//input[@id="my-text-id"]').screenshot('username.png')
    sleep(3)  # Wait to observe the result

    # Close the browser
    driver.quit()  # Note: should be driver.quit() to properly close the browser