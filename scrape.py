from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pickle
import time
import csv



def driver_function():
    options = Options()
    options.add_experimental_option("detach", True) 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Wait for the "Find a Job" link to be clickable
    return driver


def perform_search(driver):
    search_title = driver.find_element(By.ID, 'job-board-search-filter')
    search_title.send_keys('data')

    search_location = driver.find_element(By.XPATH, '//*[@id="react-select-5-input"]')
    search_location.send_keys("canada")
    time.sleep(2)
    search_location.send_keys(Keys.ENTER)
    time.sleep(2)

    # search_type = driver.find_element(By.XPATH, '//*[@id="react-select-6-input"]')
    # search_type.send_keys('relocate', Keys.ENTER)

    time.sleep(2)



def scrape_job_details(driver, item, scraped_data, section = "all"):
        if section == 'all':
            try:
                link = driver.find_element(By.XPATH, f'//*[@id="scrollable-job-board-div"]/div[2]/div/div[{item}]')
            except NoSuchElementException:
                try:
                    link = driver.find_element(By.XPATH, f'//*[@id="scrollable-job-board-div"]/div[3]/div/div[{item}]')
                except NoSuchElementException:
                        link = driver.find_element(By.XPATH, f'//*[@id="scrollable-job-board-div"]/div[{item}]')
        else:
            try:
                link = driver.find_element(By.XPATH, f'//*[@id="scrollable-job-board-div"]/div[6]/div/div[{item}]')
            except NoSuchElementException:
                link = driver.find_element(By.XPATH, f'//*[@id="scrollable-job-board-div"]/div[7]/div/div[{item}]')

                

        driver.execute_script("arguments[0].scrollIntoView(true);", link)
        a = link.find_element(By.TAG_NAME, 'a').get_attribute('href')
        time.sleep(5)
        driver.get(a)

        title = driver.find_element(By.XPATH, '//*[@id="vh-job-details-header-section"]/p').text
        location = driver.find_element(By.XPATH, '//*[@id="vh-job-details-header-section"]/div[4]/div[1]/p').text
        remote = driver.find_element(By.XPATH, '//*[@id="vh-job-details-header-section"]/div[4]/div[2]/span[1]').text
        salary = driver.find_element(By.XPATH, '//*[@id="vh-job-details-header-section"]/div[4]/div[3]/span/span').text
        description = driver.find_element(By.XPATH, '//*[@id="vh-job-details-job-about-section"]').text

        print(f'Job Title: {title}')
        print(f'Job Link: {a}')
        print(f'Location: {location}')
        print(f'Remote/On-site: {remote}')
        print(f'Salary: {salary}')
        print(f'Description: {description}')
        print(' ')

        driver.back()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'job-card')))

        time.sleep(5)

        job_data = {
            'Job Title': title,
            'Job Link': a,
            'Location': location,
            'Remote/On-site': remote,
            'Salary': salary,
            'Description': description
        }

        scraped_data.append(job_data)
        time.sleep(2)



def save_to_csv(data):
    with open('scraped_jobs.csv', 'w+', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Job Title', 'Job Link', 'Location', 'Remote/On-site', 'Salary', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for job in data:
            # Replace newline characters in the description with spaces to keep it in a single line
            job['Description'] = job['Description'].replace('\n', ' ')
            writer.writerow(job)


def scrape_all(driver):
    url = 'https://vanhack.com'

    driver.get(url)
    
    # Click on the "Find a Job" link using JavaScript
    find_job_link = driver.find_element(By.LINK_TEXT, 'Find a Job')
    driver.execute_script("arguments[0].click();", find_job_link)

    # Wait for the job posts to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "job-card")))
    
    time.sleep(2)
   
    print("\033[1m" + 'THE AVAILABLE JOBS ARE:'+ "\033[0m")
    item = 1
    scraped_data = []
    
    print(' ')

    while True:
        try:
            scrape_job_details(driver, item, scraped_data)
            item += 1
        except Exception:
            print(' ')
            print('No more jobs!')
            break
    
    # Save the scraped data to a CSV file
    save_to_csv(scraped_data)



def scrape_by_criteria(driver):
    url = 'https://vanhack.com'
    driver.get(url)
    
    # Click on the "Find a Job" link using JavaScript
    find_job_link = driver.find_element(By.LINK_TEXT, 'Find a Job')
    driver.execute_script("arguments[0].click();", find_job_link)

    # Wait for the job posts to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "job-card")))
    
    time.sleep(2)

        # Perform search
    perform_search(driver) 
        
    print("\033[1m" + 'YOUR SELECTED JOBS ARE:'+ "\033[0m")
    item = 1
    scraped_data = []
    
    print(' ')

    while True:
        try:
            scrape_job_details(driver, item, scraped_data)
            item += 1
        except Exception:
            print(' ')
            print('No more jobs!')
            break
    
    # Save the scraped data to a CSV file
    save_to_csv(scraped_data)

