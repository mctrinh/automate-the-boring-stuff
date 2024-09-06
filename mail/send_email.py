#!/usr/bin/env python3

"""Send emails from the Command Line using Selenium."""

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_email(recipient, subject, message):
    # Set up the browser
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run headless if you don't need a GUI
    browser = webdriver.Chrome(options=options)
    browser.get('https://mail.google.com/')
    
    try:
        # Wait for the email field to be available and log in
        email_field = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.ID, 'identifierId'))
        )
        email_field.send_keys('email@gmail.com')
        browser.find_element(By.ID, 'identifierNext').click()
        
        # Wait for the password field and enter the password
        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_field = browser.find_element(By.NAME, 'password')
        password_field.send_keys('password')
        browser.find_element(By.ID, 'passwordNext').click()

        # Wait for Gmail to load and click the Compose button
        compose_button = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.T-I.T-I-KE.L3'))
        )
        compose_button.click()
        
        # Wait for the recipient field and enter the recipient
        to_field = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'to'))
        )
        to_field.send_keys(recipient)
        
        # Enter the subject
        subject_field = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.NAME, 'subjectbox'))
        )
        subject_field.send_keys(subject)
        
        # Enter the message
        message_field = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.Am.Al.editable.LW-avf.tS-tW'))
        )
        message_field.send_keys(message)
        
        # Click the Send button
        send_button = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.T-I.T-I-J3'))
        )
        send_button.click()
        
        print('Email sent successfully.')

    except Exception as e:
        print(f'An error occurred: {e}')

    finally:
        # Clean up
        time.sleep(5)  # Allow some time for the email to be sent
        browser.quit()

def main():
    if len(sys.argv) != 4:
        print('Usage: python send_email.py [recipient] [subject] [message]')
        sys.exit(1)
    
    recipient, subject, message = sys.argv[1], sys.argv[2], sys.argv[3]
    send_email(recipient, subject, message)

if __name__ == '__main__':
    main()
