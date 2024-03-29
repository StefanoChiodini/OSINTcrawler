# here escaping functions are not required, the page is already downloaded so i proceed to format the page in json format
from bs4 import BeautifulSoup
from filteredHTMLtag import *
import threading
from readableFormat import *

# here we can extract all the content from the page and format it in json format 

# create a function to extract the data from all tags in the HTML
def extractAllData(htmlChuck):
    soup = BeautifulSoup(htmlChuck, 'html.parser')
    data = []
    data = obtainReadableFormat(soup)
    return data


# with this function i extract all the content from the html page and i format it in json format
def htmlPageParser(pageSource, url):

    # Split the HTML code into chunks to be processed in parallel
    chunk_size = len(pageSource) // 4
    chunks = [pageSource[i:i+chunk_size] for i in range(0, len(pageSource), chunk_size)]

    # Create worker threads to process the HTML chunks
    threads = []
    results = []
    for chunk in chunks:
        thread = threading.Thread(target=lambda: results.append(extractAllData(chunk)))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    final_result = []
    for result in results:
        final_result += result

    #final_result = obtainReadableFormat(final_result)

    # extract the data and store in a dictionary -> to be formatted in json format
    pageData = {
        'url': url,
        'data': final_result
    }

    return pageData

        
