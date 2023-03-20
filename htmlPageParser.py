# here escaping functions are not required, the page is already downloaded so i proceed to format the page in json format
import json
from bs4 import BeautifulSoup

# with this function i extract all the content from the html page and i format it in json format
def htmlPageParser(pageSource):
    
    # check if the page is successfully loaded
    if pageSource is not None:
        # here i convert the html page into a soup object
        soup = BeautifulSoup(pageSource, 'html.parser')

        # TODO -> here we can extract all the content from the page and format it in json format
