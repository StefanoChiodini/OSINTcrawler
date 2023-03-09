# here i will handle all the crawling process
# i will cycle through all the URLs in the list, getting all of them, extracting the URLs and then getting the next URL in the list
# implement here a dictorary that will count the number of times a URL is visited so that i can avoid infinite loops
# If a URL is already in the dictionary, i will not visit it again. I will increment the counter of the URL in the dictionary and then
# i will get the next URL in the list
from crawlerBlockingEscape import *
from extractingURL import *

# initialize a dictionary to keep track of click counts
clickCounts = {}

# initialize a list to keep track of visited URLs
visitedUrls = []

def crawlingFunction(driver, BASEUrl, urlList, userCookie):
    for url in urlList:
        
        # check if the URL has the same base URL as the website you're crawling -> if not, skip it
        if not url.startswith(BASEUrl):
            continue

        # check if the URL has already been visited -> if yes, skip it and increment the counter associated with the URL
        if url in visitedUrls:
            clickCounts[url] += 1
            continue

        # if the URL has not been visited yet, visit it and add it to the list of visited URLs and to the dictionary of click counts
        #TODO: FIX THIS -> #driver.add_cookie(userCookie)
        escaping(driver)
        driver.get(url)
        escaping(driver)
        #TODO: FIX THIS -> #statusCode = driver.execute_script("return window.performance.getEntries()[0].response.status")

        #if statusCode >= 400:
        #    continue

        # if i arrive here, it means that the URL has been visited for the first time and the page has been retrieved successfully    

        escaping(driver)
        linksList = extractURLs(driver, url)
        escaping(driver)

        clickCounts[url] = 1
        visitedUrls.append(url)

        # insert all the URLs extracted from the current URL into the list of URLs to be visited
        for link in linksList:
            urlList.append(link)

    return clickCounts
