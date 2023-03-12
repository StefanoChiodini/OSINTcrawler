from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from urllib.parse import urljoin # to join the relative URLs with the base URL

# with this function I extract all the URLs from the html page
def extractURLs(driver, BASEUrl):
    #wait until the page is fully loaded
    try:
        wait = WebDriverWait(driver, 10)  # wait for up to 10 seconds
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        wait.until(EC.presence_of_element_located((By.XPATH, "//a")))  # wait for at least one link to be present
        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")   
    except TimeoutException as e:
        # if the page is not loaded in 10 seconds, i will return an empty list
        return []

    # here i obtain the whole html page
    htmlPage = driver.page_source
    # check if the page is successfully loaded
    if htmlPage is not None:
        # here i convert the html page into a soup object
        soup = BeautifulSoup(htmlPage, 'html.parser')

        # i extract all the URLs from the soup object and i store them in a set, so that i can remove the duplicates
        # in this lists there are absolute and relative URLs
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

        return urlList  # list of absolute and unique URLs
