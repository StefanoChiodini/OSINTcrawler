# here i will handle all the crawling process
# i will cycle through all the URLs in the list, getting all of them, extracting the URLs and then getting the next URL in the list
# If a URL is already in the visitedUrls list, i will not visit it again. When i extract the url from the list i will parse and extract all the page content in a josn format
# i will get the next URL in the list
from crawlerBlockingEscape import *
from extractingURL import *
from htmlPageParser import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from savingResults import *

# initialize a list to keep track of visited URLs
visitedUrls = []

def crawlingFunction(driver, BASEUrl, urlList, userCookies):

    for cookie in userCookies:
        driver.add_cookie(cookie)
        
    for url in urlList:
        
        # check if the URL has the same base URL as the website you're crawling -> if not, skip it
        if not url.startswith(BASEUrl):
            continue

        # check if the URL has already been visited -> if yes, skip it and increment the counter associated with the URL
        if url in visitedUrls:
            continue

        escaping(driver)
        driver.get(url)
        escaping(driver)
        #TODO: FIX THIS -> #statusCode = driver.execute_script("return window.performance.getEntries()[0].response.status")

        #if statusCode >= 400:
        #    continue

        escaping(driver)
        #wait until the page is fully loaded
        try:
            wait = WebDriverWait(driver, 10)  # wait for up to 10 seconds
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            wait.until(EC.presence_of_element_located((By.XPATH, "//a")))  # wait for at least one link to be present
            wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")   
        except TimeoutException as e:
            # if the page is not loaded in 10 seconds, i will return an empty list TODO -> CHECK THE RETURN VALUE
            return []
        
        # get the whole page source
        pageSource = driver.page_source

        # if i arrive here, it means that the URL has been visited for the first time and the page has been retrieved successfully    
        # check if the page is successfully loaded
        if pageSource is not None:

            pageContent = htmlPageParser(pageSource, url) # extract all the content from the page (tags, text, etc.)

            # extract all the URLs from the already downloaded page. Page source is the html page
            # functions return a list of URLs -> then i will insert them in the list of URLs to be visited to keep crawling the website
            linksList = extractURLs(pageSource, url)
            escaping(driver)

            visitedUrls.append(url)

            # insert all the URLs extracted from the current URL into the list of URLs to be visited and the make the list unique
            for link in linksList:
                    urlList.append(link)

            # make the list unique
            urlList = list(set(urlList))

            # save results
            saveResults(pageContent, BASEUrl, url, urlList)
    
        else:
            continue
