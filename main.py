from vanhack import driver_function
from vanhack import scrape_all
from vanhack import scrape_by_criteria
from login import log_in
from login import login_and_scrape_all
from login import login_and_scrape_by_criteria
from application import login_and_apply

def main():
    url = 'https://vanhack.com'

    driver = driver_function()
    
    # scrape_all(driver)

    # scrape_by_criteria(driver)

    #log_in(driver, url)

    # login_and_apply(driver)

    #login_and_scrape_all(driver)

    login_and_scrape_by_criteria(driver)
   
main()
