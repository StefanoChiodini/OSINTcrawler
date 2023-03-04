from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from crawlerBlockingEscape import *
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
    # here i obtain the whole html page
    htmlPage = driver.page_source
    # here i convert the html page into a soup object
    soup = BeautifulSoup(htmlPage, 'html.parser')

    # i extract all the URLs from the soup object and i store them in a set, so that i can remove the duplicates
    # in this lists there are absolute and relative URLs
    urlList = set()
    for url in soup.find_all('a'):
        href = url.get('href')
        if href is not None:
            urlList.add(href)

    # print the unique urlList
    for url in urlList:
        print(url)

