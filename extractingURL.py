from bs4 import BeautifulSoup 

# with this function I extract all the URLs from the html page
def extractURLs(driver):
    # here i obtain the whole html page
    htmlPage = driver.page_source
    # here i convert the html page into a soup object
    soup = BeautifulSoup(htmlPage, 'html.parser')

    # i extract all the URLs from the soup object and i store them in a set, so that i can remove the duplicates
    # in this lists there are absolute and relative URLs
    urlSet = set()
    for url in soup.find_all('a'):
        href = url.get('href')
        if href is not None:
            urlSet.add(href)     

    # here i convert the set into a list
    urlList = list(urlSet)

    return urlList   

# functions to test
def printSomething():
    return "something"
