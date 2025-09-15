from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

def test_drop_down_list():
    # Initialize Edge browser driver
    driver = webdriver.Edge()
    driver.maximize_window()  # Maximize the browser window
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")  # Open the target web page
    sleep(2)  # Wait for the page to load

    # Locate the drop-down list element
    drop_down = Select(driver.find_element(By.XPATH, '//select[@name="my-select"]'))
    
    # Select option by visible text
    drop_down.select_by_visible_text("Open this select menu")
    sleep(1)  # Wait to observe the selection
    
    # Select option by value
    drop_down.select_by_value("1")
    sleep(1)  # Wait to observe the selection

    # Close the browser
    driver.quit()