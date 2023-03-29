import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.remote_connection import LOGGER
import sys

from seleniumCrawling import seleniumCrawling
from requestsCrawling import requestsCrawling

# Disable logging output from device_event_log_impl module
LOGGER.setLevel(logging.WARNING)

options = Options()
options.add_experimental_option("detach", True) # this will keep the browser open after the script is finished
options.add_argument('--headless') # this will hide the browser -> the browser will not be rendered so maybe it will be faster
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--disable-usb-keyboard-detect')
options.add_argument('--disable-usb-detection')


if __name__ == "__main__":

    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)    

    if len(sys.argv) > 1:

        if sys.argv[1] == "R":
            requestsCrawling()

        elif sys.argv[1] == "S":
            seleniumCrawling(driver)

        else:
            print("Invalid argument. Please insert 'R' for requests crawling or 'S' for selenium crawling.")
            
    else:
        seleniumCrawling(driver)


