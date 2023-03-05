from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import os 
from dotenv import load_dotenv

from crawlerBlockingEscape import *
from extractingURL import *
from userLogin import *

options = Options()
options.add_experimental_option("detach", True) # this will keep the browser open after the script is finished

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)    

load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
EMAIL = os.getenv("EMAIL")

BASEUrl = "https://0x00sec.org" # without the last slash

if __name__ == "__main__":

    driver.get("https://0x00sec.org/")
    
    escaping(driver)
    login(EMAIL, PASSWORD, driver)
    escaping(driver)
    
    urlList = extractURLs(driver, BASEUrl)
    # i print the list of urls in the file urls.txt
    with open("urls.txt", "w") as f:
        for url in urlList:
            f.write(url + "\n")
