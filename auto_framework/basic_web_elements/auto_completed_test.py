from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_click_type():
    # Initialize Edge browser driver
    driver = webdriver.Edge()
    driver.maximize_window()  # Maximize the browser window

    # Open the target web page (Google)
    driver.get("https://www.google.com")
    sleep(2)  # Wait for the page to load

    # Locate the search box element
    search_box = driver.find_element(By.XPATH, '//textarea[@name="q"]')
    # Enter the search term "Selenium"
    search_box.send_keys("Selenium")
    sleep(2)  # Wait for autocomplete suggestions to appear

    # Navigate down the autocomplete suggestions
    search_box.send_keys(Keys.ARROW_DOWN)
    sleep(2)

    # Navigate down again in the suggestions
    search_box.send_keys(Keys.ARROW_DOWN)
    sleep(2)

    # Press Enter to select the suggestion
    search_box.send_keys(Keys.ENTER)
    sleep(2)  # Wait for the search results page to load

    # Close the browser
    driver.quit()