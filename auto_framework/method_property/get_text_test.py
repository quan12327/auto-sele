from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_get_text():
    # Initialize Edge browser driver
    driver = webdriver.Edge()
    driver.maximize_window()  # Maximize the browser window
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")  # Open the target web page
    sleep(2)  # Wait for the page to load

    # Locate the title element and get its text
    title = driver.find_element(By.XPATH, '//h1[@class="display-6"]')
    print(title.text)  # Print the text content of the title element

    # Close the browser
    driver.quit()