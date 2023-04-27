import os 
from dotenv import load_dotenv
from crawlingFunction import *
from filteredHTMLtag import *
from seleniumCrawling import *
from crawlerBlockingEscape import *
from extractingURL import *
from userLogin import *

import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.remote_connection import LOGGER

# Disable logging output from device_event_log_impl module
LOGGER.setLevel(logging.WARNING)

options = Options()
options.add_experimental_option("detach", True) # this will keep the browser open after the script is finished
options.add_argument('--headless') # this will hide the browser -> the browser will not be rendered so maybe it will be faster
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--disable-usb-keyboard-detect')
options.add_argument('--disable-usb-detection')

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)    

def seleniumCrawling():
    
    load_dotenv()
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    EMAIL = os.getenv("EMAIL")

    BASEUrl = "https://0x00sec.org" # without the last slash
    startingURL = "https://0x00sec.org"

    driver.get(startingURL)
    driver.maximize_window()

    seleniumEscaping(driver)
    userCookies = login(EMAIL, PASSWORD, driver)
    if userCookies == None:
        print("Login failed")
        driver.quit()
        return
    
    else: # the login was successful
        print("Login successful")
        seleniumEscaping(driver)
            
        pageSource = driver.page_source

        urlList = extractURLs(pageSource, BASEUrl)

        # here i add cookies to the driver
        for cookie in userCookies:
            driver.add_cookie(cookie)

        seleniumCrawlingFunction(driver, BASEUrl, urlList, userCookies)
        
        driver.quit()