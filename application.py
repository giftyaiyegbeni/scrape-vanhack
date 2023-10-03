from vanhack import driver_function
from login import log_in
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
import pickle


# Define a function to log in and apply for jobs
def login_and_apply(driver):
    url = 'https://vanhack.com'
    
    driver.get(url)

    # Perform login process
    log_in(driver, url)   

    time.sleep(1)
    
    # Perform search
    perform_search(driver)
    
    print(' ')
    
    item = 3

    while True:
        try:
            link = driver.find_element(By.XPATH, f'//*[@id="scrollable-job-board-div"]/div[{item}]/div[1]/div/div[1]')
            
            driver.execute_script("arguments[0].scrollIntoView(true);", link)
            a = link.find_element(By.TAG_NAME, 'a').get_attribute('href')
            time.sleep(3)
            driver.get(a)

            title = driver.find_element(By.XPATH, '//*[@id="vh-job-details-header-section"]/p').text
            
            go = driver.find_element(By.XPATH, '//*[@id="vh-job-details-apply-job-button-right"]/button')
            driver.execute_script("arguments[0].click();", go)
            time.sleep(2)
            
            print(f'Applied for: {title}')
            
            print(' ')

            driver.back()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'job-card')))

            item += 1
            time.sleep(5)
        
        except Exception:
            pass
            break
            
    item = 1        
    while True:
        try:
            link = driver.find_element(By.XPATH, f'//*[@id="scrollable-job-board-div"]/div[7]/div/div[{item}]')
            
            driver.execute_script("arguments[0].scrollIntoView(true);", link)
            a = link.find_element(By.TAG_NAME, 'a').get_attribute('href')
            time.sleep(3)
            driver.get(a)

            title = driver.find_element(By.XPATH, '//*[@id="vh-job-details-header-section"]/p').text
            
            go = driver.find_element(By.XPATH, '//*[@id="vh-job-details-apply-job-button-right"]/button')
            driver.execute_script("arguments[0].click();", go)
            time.sleep(2)
            
            print(f'Applied for: {title}')
            
            print(' ')

            driver.back()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'job-card')))

            item += 1
            time.sleep(5)
        except Exception:
            print('Application done!')
            break
