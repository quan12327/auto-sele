from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test_radio_checkbox():
    # Initialize Edge browser driver
    driver = webdriver.Edge()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")  # Open the target web page
    driver.maximize_window()  # Maximize the browser window
    sleep(1)  # Wait for the page to load

    # Locate checkbox and radio button elements
    checkbox1 = driver.find_element(By.XPATH,"//input[@id='my-check-1']")
    checkbox2 = driver.find_element(By.XPATH,"//input[@id='my-check-2']")
    radio1 = driver.find_element(By.XPATH,"//input[@id='my-radio-1']")
    radio2 = driver.find_element(By.XPATH,"//input[@id='my-radio-2']")

    # Uncheck checkbox1 if it is checked
    if not checkbox1.is_selected():
        checkbox1.click()
    # Check checkbox2 if it is not checked
    if not checkbox2.is_selected():
        checkbox2.click()
    
    # Unselect radio1 if it is selected (though radios usually can't be unselected directly)
    if radio1.is_selected():
        radio1.click()
    # Select radio2 if it is not selected
    if not radio2.is_selected():
        radio2.click()

    sleep(3)  # Wait to observe the result
    driver.quit()  # Close the browser