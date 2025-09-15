from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test_find_state():
    # Initialize Edge browser driver
    driver = webdriver.Edge()
    driver.maximize_window()  # Maximize the browser window

    # Navigate to the Selenium web form page
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    sleep(1)  # Wait for the page to load

    # Locate and click the submit button
    submit = driver.find_element(By.XPATH,"//button[@type='submit']")
    submit.click()
    sleep(1)  # Wait for the result after clicking submit

    # Try to find the message element by its id
    message = driver.find_elements(By.XPATH,"//p[@id='message']")
    if message:
        print("Element found")  # Print if the element is found
    else:
        print("Element not found")  # Print if the element is not found

    sleep(1)  # Wait before closing the browser
    driver.quit()  # Close the browser