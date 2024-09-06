from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# Initialize the Chrome browser
browser = webdriver.Chrome()

try:
    # Navigate to the Project Gutenberg website
    browser.get('https://www.gutenberg.org')

    # Attempt to find the element with the specified class name
    elem = browser.find_element(By.CLASS_NAME, 'bookcover')  # Example class name; adjust as needed
    print(f'Found <{elem.tag_name}> element with that class name!')
except NoSuchElementException:
    # Handle the case where the element is not found
    print('Was not able to find an element with that class name.')
finally:
    # Ensure the browser is closed
    browser.quit()
