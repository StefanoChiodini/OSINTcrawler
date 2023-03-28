# here escaping functions are not required, the page is already downloaded so i proceed to format the page in json format
from bs4 import BeautifulSoup
from filteredTHTMLtag import *

# with this function i extract all the content from the html page and i format it in json format
def htmlPageParser(pageSource, url):
    
        # here i convert the html page into a soup object
        soup = BeautifulSoup(pageSource, 'html.parser')

        # here we can extract all the content from the page and format it in json format
        def extract_tag_data(tag):
            checkTag = removeUselessTags(tag)
            if checkTag == "to be removed":
                return "to be removed" # TODO -> CLEAN THE CODE HERE
            
            else :
                if tag.name is not None and (tag.text.strip() != '' or tag.attrs):
                    data = {
                        'name': tag.name,
                        'text': tag.get_text(strip=True),
                        'attrs': {}
                    }
                    for attr, value in tag.attrs.items():

                        if attr not in ['class', 'style', 'width', 'height', 'loading']: # here i remove the useless attributes
                            data['attrs'][attr] = value
                    return data
                
                return "to be removed"

        # create a function to extract the data from all tags in the HTML
        def extractAllData(soup):
            data = []
            for tag in soup.descendants:
                if tag.name:
                    tag_data = extract_tag_data(tag)
                    if tag_data != "to be removed":
                        data.append(tag_data)
            return data

        # extract the data and store in a dictionary
        pageData = {
            'url': url,
            'data': extractAllData(soup)
        }

        return pageData

        
