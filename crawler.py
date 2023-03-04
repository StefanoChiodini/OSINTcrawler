from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from crawlerBlockingEscape import *
from extractingURL import *
from bs4 import BeautifulSoup 

import os 
from dotenv import load_dotenv

options = Options()
options.add_experimental_option("detach", True) # this will keep the browser open after the script is finished

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)    

load_dotenv()
USERNAME = os.getenv("USERNAME")

if __name__ == "__main__":

    driver.get("https://0x00sec.org/")
    
    escaping(driver)
    
    urlList = extractURLs(driver)



