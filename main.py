import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.remote_connection import LOGGER
from crawlingFunction import *
from filteredTHTMLtag import *

# Disable logging output from device_event_log_impl module
LOGGER.setLevel(logging.WARNING)

import os 
from dotenv import load_dotenv

from crawlerBlockingEscape import *
from extractingURL import *
from userLogin import *

options = Options()
options.add_experimental_option("detach", True) # this will keep the browser open after the script is finished
options.add_argument('--headless') # this will hide the browser -> the browser will not be rendered so maybe it will be faster
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--disable-usb-keyboard-detect')
options.add_argument('--disable-usb-detection')

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)    

load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
EMAIL = os.getenv("EMAIL")

BASEUrl = "https://0x00sec.org" # without the last slash
startingURL = "https://0x00sec.org"

# dictionary that collects the results of the crawling
results = {}

if __name__ == "__main__":

    driver.get(startingURL)
    driver.maximize_window()
    
    escaping(driver)
    userCookies = login(EMAIL, PASSWORD, driver)
    escaping(driver)
    
    urlList = extractURLs(driver, BASEUrl)

    # here i add cookies to the driver
    for cookie in userCookies:
        driver.add_cookie(cookie)

    crawlingFunction(driver, BASEUrl, urlList, userCookies)

    driver.quit()

