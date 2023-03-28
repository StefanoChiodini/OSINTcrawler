import os
import json

def saveResults(pageContent, BASEUrl, url, urlList):
    # create result directory if it doesn't exist
    resultDir = 'result'
    if not os.path.exists(resultDir):
        os.mkdir(resultDir)

    url = url.replace(BASEUrl, '')
    url = url.replace('/', '_')
    fileName = url + '.json'

    # convert the dictionary to JSON and save to a file
    output_file = os.path.join(resultDir, fileName)
    with open(output_file, 'w') as f:
        json.dump(pageContent, f, indent=3)

