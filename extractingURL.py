from bs4 import BeautifulSoup
from urllib.parse import urljoin # to join the relative URLs with the base URL

# with this function I extract all the URLs from the html page
def extractURLs(pageSource, BASEUrl):

    htmlPage = pageSource
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
