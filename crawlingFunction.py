# here i will handle all the crawling process
# i will cycle through all the URLs in the list, getting all of them, extracting the URLs and then getting the next URL in the list
# If a URL is already in the visitedUrls list, i will not visit it again. When i extract the url from the list i will parse and extract all the page content in a josn format
# i will get the next URL in the list
from crawlerBlockingEscape import *
from extractingURL import *
from htmlPageParser import *
from urllib.parse import urlparse, urlunparse
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from savingResults import *

# initialize a list to keep track of visited URLs
visitedUrls = []

def seleniumCrawlingFunction(driver, BASEUrl, urlList, userCookies):

    for cookie in userCookies:
        driver.add_cookie(cookie)

    print("Selenium crawling started...") 
    while(len(urlList) > 0):
        url = urlList.pop(0) # get the first URL in the list and remove it from the list
        
        # parse the URL
        parsed_url = urlparse(url)

        # remove the fragment identifier (the part after the # symbol) and the query string (the part after the ? symbol)
        parsed_url = parsed_url._replace(fragment='')._replace(query='')

        # convert the URL back to a string
        path_components = parsed_url.path.split('/')
        # Remove any numeric parts from the end of the URL
        while path_components[-1].isdigit():
            path_components = path_components[:-1]

        base_path = '/'.join(path_components)
        url = urlunparse((parsed_url.scheme, parsed_url.netloc, base_path, "", "", ""))

        # check if the URL has the same base URL as the website you're crawling -> if not, skip it
        if not url.startswith(BASEUrl):
            continue

        # check if the URL has already been visited -> if yes, skip it and increment the counter associated with the URL
        if url in visitedUrls:
            continue

        if "/u/" in url: # if the URL is a user profile, skip it
            continue
        
        if "/c/" in url: # if the URL is a category, skip it
            continue

        if "/tag/" in url: # if the URL is a tag, skip it
            continue
        
        seleniumEscaping(driver)
        driver.get(url)
        seleniumEscaping(driver)

        seleniumEscaping(driver)
        #wait until the page is fully loaded
        try:
            wait = WebDriverWait(driver, 10)  # wait for up to 10 seconds
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            wait.until(EC.presence_of_element_located((By.XPATH, "//a")))  # wait for at least one link to be present
            wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete") 

        except TimeoutException as e:
            pageSourceNoneCounter += 1
            continue # go to the next page   

        # get the whole page source
        pageSource = driver.page_source

        # if i arrive here, it means that the URL has been visited for the first time and the page has been retrieved successfully    
        # check if the page is successfully loaded
        if pageSource is not None:

            pageContent = htmlPageParser(pageSource, url) # extract all the content from the page (tags, text, etc.)

            # extract all the URLs from the already downloaded page. Page source is the html page
            # functions return a list of URLs -> then i will insert them in the list of URLs to be visited to keep crawling the website
            linksList = extractURLs(pageSource, url)
            seleniumEscaping(driver)

            visitedUrls.append(url)

            # insert all the URLs extracted from the current URL into the list of URLs to be visited and the make the list unique
            urlList.extend(linksList)

            # make the list unique
            urlList = list(set(urlList))

            # save results
            crawlingType = "selenium"
            saveResults(pageContent, BASEUrl, url, linksList, crawlingType)

        else:
            pageSourceNoneCounter += 1
            continue
    
    print("Selenium crawling finished!") 
    

def requestsCrawlingFunction(session, BASEUrl, urlList):

    print("Requests crawling started...")
    while(len(urlList) > 0):
        url = urlList.pop(0) # get the first URL in the list and remove it from the list
        
        # parse the URL
        parsed_url = urlparse(url)

        # remove the fragment identifier (the part after the # symbol) and the query string (the part after the ? symbol)
        parsed_url = parsed_url._replace(fragment='')._replace(query='')

        # convert the URL back to a string
        path_components = parsed_url.path.split('/')
        # Remove any numeric parts from the end of the URL
        while path_components[-1].isdigit():
            path_components = path_components[:-1]
            
        base_path = '/'.join(path_components)
        url = urlunparse((parsed_url.scheme, parsed_url.netloc, base_path, "", "", ""))
        
        # check if the URL has the same base URL as the website you're crawling -> if not, skip it
        if not url.startswith(BASEUrl):
            continue

        # check if the URL has already been visited -> if yes, skip it and increment the counter associated with the URL
        if url in visitedUrls:
            continue
        
        if "/u/" in url: # if the URL is a user profile, skip it
            continue
        
        if "/c/" in url: # if the URL is a category, skip it
            continue

        if "/tag/" in url: # if the URL is a tag, skip it
            continue

        changeUserAgent = requestEscaping()

        if changeUserAgent != "not changed":
            # Convert the string to a dictionary using json.loads()
            session.headers.update(changeUserAgent) 

        r = session.get(url, headers = session.headers) # get the page

        changeUserAgent = requestEscaping()

        if changeUserAgent != "not changed":
            # Convert the string to a dictionary using json.loads()
            session.headers.update(changeUserAgent) 
 
        if r.status_code >= 400: # there is an error
            continue
        
        # get the whole page source
        pageSource = r.text

        # if i arrive here, it means that the URL has been visited for the first time and the page has been retrieved successfully    
        # check if the page is successfully loaded
        if pageSource is not None:

            pageContent = htmlPageParser(pageSource, url) # extract all the content from the page (tags, text, etc.)

            # extract all the URLs from the already downloaded page. Page source is the html page
            # functions return a list of URLs -> then i will insert them in the list of URLs to be visited to keep crawling the website
            linksList = extractURLs(pageSource, url)

            changeUserAgent = requestEscaping()

            if changeUserAgent != "not changed":
                # Convert the string to a dictionary using json.loads()
                session.headers.update(changeUserAgent)  
 
            visitedUrls.append(url)

            # insert all the URLs extracted from the current URL into the list of URLs to be visited and the make the list unique
            for link in linksList:
                    urlList.append(link)

            # make the list unique
            urlList = list(set(urlList))

            # save results
            crawlingType = "requests"
            saveResults(pageContent, BASEUrl, url, linksList, crawlingType)

        else:
            continue

    print("Requests crawling finished!")  

    
