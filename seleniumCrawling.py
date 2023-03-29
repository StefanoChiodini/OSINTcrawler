import os 
from dotenv import load_dotenv
from crawlingFunction import *
from filteredTHTMLtag import *
from seleniumCrawling import *
from crawlerBlockingEscape import *
from extractingURL import *
from userLogin import *

def seleniumCrawling(driver):
    
    load_dotenv()
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    EMAIL = os.getenv("EMAIL")

    BASEUrl = "https://0x00sec.org" # without the last slash
    startingURL = "https://0x00sec.org"

    driver.get(startingURL)
    driver.maximize_window()
    
    escaping(driver)
    userCookies = login(EMAIL, PASSWORD, driver)
    escaping(driver)
    
    pageSource = driver.page_source

    urlList = extractURLs(pageSource, BASEUrl)

    # here i add cookies to the driver
    for cookie in userCookies:
        driver.add_cookie(cookie)

    crawlingFunction(driver, BASEUrl, urlList, userCookies)

    driver.quit()