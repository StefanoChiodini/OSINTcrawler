import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.remote_connection import LOGGER
from crawlingFunction import *
from filteredTHTMLtag import *
import json
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
#BASEUrl = "https://xss.is"
#startingURL = "https://xss.is"
startingURL = "https://0x00sec.org"
tempURL = "https://0x00sec.org/c/forensics/106"
temp1URL = "https://0x00sec.org/c/hardware/68"

# dictionary that collects the results of the crawling
results = {}

if __name__ == "__main__":

    driver.get(startingURL)
    driver.maximize_window()
    
    escaping(driver)
    userCookies = login(EMAIL, PASSWORD, driver)
    escaping(driver)
    
    #urlList = extractURLs(driver, BASEUrl)

    # here i add cookies to the driver
    for cookie in userCookies:
        driver.add_cookie(cookie)

    '''
    results = crawlingFunction(driver, BASEUrl, urlList, userCookies)

    # print the results in the txt file results.txt in a way that is easy to read: there will be only one url and its count per line
    with open("results.txt", "w") as f:
        for url in results:
            f.write(url + " " + str(results[url]) + "\n")
    '''
    driver.get(temp1URL)
    pageSource = driver.page_source

    # check if the page is successfully loaded
    if pageSource is not None:
        # here i convert the html page into a soup object
        soup = BeautifulSoup(pageSource, 'html.parser')

        # TODO -> here we can extract all the content from the page and format it in json format
        # Extract the tags and their content 
        data = {}

        for tag in soup.find_all():
            
            if tag.name not in data:
                data[tag.name] = []

            resultCheck = removeUselessTags(tag)
            if resultCheck == "to be removed":
                continue
            else:   
                # insert the tag and its content in the dictionary
                data[tag.name].append({
                    'name': tag.name,
                    'attrs': dict(tag.attrs), 
                    'text': tag.get_text(strip=True)
                    })

        # Convert the dictionary to a JSON string
        json_str = json.dumps(data, indent=3)

        # print the JSON string in the file jsonPage.json
        with open("jsonFilteredPage.json", "w") as f:
            f.write(json_str)

        # here i extract all the links from the page
        urlList = []
        for url in soup.find_all('a'):
            href = url.get('href')
            if href is not None:
                urlList.append(href)     

        # i convert the relative URLs into absolute URLs
        for i in range(len(urlList)):
            urlList[i] = urljoin(BASEUrl, urlList[i])

        # i remove the duplicates
        urlList = list(set(urlList))    

        # write the links in the file links.txt
        with open("links.txt", "w") as f:
            for url in urlList:
                f.write(url + "\n")
          
    driver.quit()

