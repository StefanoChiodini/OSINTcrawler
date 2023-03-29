import sys

from seleniumCrawling import seleniumCrawling
from requestsCrawling import requestsCrawling

if __name__ == "__main__":

    if len(sys.argv) > 1:

        if sys.argv[1] == "R":
            requestsCrawling()

        elif sys.argv[1] == "S":
            seleniumCrawling()

        else:
            print("Invalid argument. Please insert 'R' for requests crawling or 'S' for selenium crawling.")
            
    else:
        seleniumCrawling()


