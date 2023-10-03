from vanhack import driver_function
from vanhack import perform_search
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from vanhack import save_to_csv
from vanhack import scrape_job_details
import pickle
import csv


def log_in(driver, url):
    
    driver.get(url)
    
    # Wait for the "Log In" link to be clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Log In')))

    # Click on the "Log In" link using JavaScript
    log_in_link = driver.find_element(By.LINK_TEXT, 'Log In')
    driver.execute_script("arguments[0].click();", log_in_link)

    email = 'aiyegbenigifty@gmail.com'
    password = 'aHz6sr8ijF@t2xs'
    
    time.sleep(3)

    driver.find_element(By.NAME, 'email').send_keys(email)
    driver.find_element(By.NAME, 'password').send_keys(password)


    # Click on the "Continue with email" button using JavaScript
    go = driver.find_element(By.TAG_NAME, 'button')
    driver.execute_script("arguments[0].click();", go)
    
    time.sleep(1)
     



def login_and_scrape_all(driver):
    url = 'https://vanhack.com'
    
    log_in(driver, url)
    time.sleep(2)
   
    print("\033[1m" + 'YOUR RECOMMENDED JOBS ARE:'+ "\033[0m")
    item = 2
    scraped_data = []
    
    print(' ')

    while True:
        try:
            scrape_job_details(driver, item, scraped_data)
            item += 1
        except Exception:
            print(' ')
            print("\033[1m" + 'SEE THE NEWEST JOBS BELOW'+ "\033[0m")
            print(' ')
            break

    item = 1

    while True:
        try:
            scrape_job_details(driver, item, scraped_data, section = 'new')
            item += 1
        except Exception:
            print(' ')
            print('No more jobs!')
            break
    
    # Save the scraped data to a CSV file
    save_to_csv(scraped_data)


def login_and_scrape_by_criteria(driver):
    url = 'https://vanhack.com'
    
    log_in(driver, url)
    time.sleep(2)

        # Perform search
    perform_search(driver) 
        
    print("\033[1m" + 'YOUR RECOMMENDED JOBS ARE:'+ "\033[0m")
    item = 3
    scraped_data = []
    
    print(' ')

    while True:
        try:
            scrape_job_details(driver, item, scraped_data)
            item += 1
        except Exception:
            print(' ')
            print("\033[1m" + 'SEE THE NEWEST JOBS BELOW'+ "\033[0m")
  
            print(' ')
            break

    item = 1

    while True:
        try:
            scrape_job_details(driver, item, scraped_data, section = 'new')
            item += 1
        except Exception:
            print(' ')
            print('No more jobs!')
            break
    
    # Save the scraped data to a CSV file
    save_to_csv(scraped_data)

