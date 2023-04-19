import os
import json

def saveResults(pageContent, BASEUrl, url, urlList, crawlingType):
    # create result directory if it doesn't exist
    if crawlingType == "selenium":
        resultDir = 'seleniumResults'
    else:
        resultDir = 'requestsResults'
            
    if not os.path.exists(resultDir):
        os.mkdir(resultDir)

    url = url.replace(BASEUrl, '')
    url = url.replace('/', '_')
    url = url.replace('?', '_')
    url = url.replace('\\', '_')
    fileName = url + '.json'
    fileName = 'Posts.json'

    # convert the dictionary to JSON and save to a file
    outputFileJson = os.path.join(resultDir, fileName)
    with open(outputFileJson, 'a') as f:
        json.dump(pageContent, f, indent = 4)

    outputFileTxt = os.path.join(resultDir, 'urls.txt')
    # every time i arrive here i append the url to the file urls.txt
    with open(outputFileTxt, 'a') as f:
        for link in urlList:
            f.write(link + "\n")    

