import requests
import os 
from dotenv import load_dotenv
from extractingURL import *
from crawlerBlockingEscape import *
from crawlingFunction import *

BASEUrl = "https://0x00sec.org" # without the last slash
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
startingURL = "https://0x00sec.org"

def login(session, user, psw):    
    url = "%s/login" % (BASEUrl,) 

    headers = {
        'User-Agent': userAgent,
    }

    data = {
            'username': user, 
            'password': psw
            } 
    r = session.post(url, data = data, headers = headers) # r is the output of the request
    if r.status_code == 200: # everything is ok and the login is successful
        return True
    else:
        return False # login failed


def requestsCrawling():

    load_dotenv()
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    EMAIL = os.getenv("EMAIL")
    
    session = requests.Session() # this will keep the cookies
    checkLogin = login(session, USERNAME, PASSWORD)
    if checkLogin == False:
        print("Login failed")
        return
    else:
        # get the first page
        url = "%s" % (BASEUrl,)

        changeUserAgent = requestEscaping()

        if changeUserAgent != "not changed":
            # Convert the string to a dictionary using json.loads()
            session.headers.update(changeUserAgent) 

        r = session.get(startingURL, headers = session.headers) # r is the output of the request

        changeUserAgent = requestEscaping()

        if changeUserAgent != "not changed":
            # Convert the string to a dictionary using json.loads()
            session.headers.update(changeUserAgent) 

        urlList = extractURLs(r.text, BASEUrl) # extract the urls from the html code of the page

        requestsCrawlingFunction(session, BASEUrl, urlList)
