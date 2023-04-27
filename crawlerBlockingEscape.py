import random 
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import JavascriptException
from selenium.common.exceptions import MoveTargetOutOfBoundsException


# group of functions to help escape blocking techniques when crawling a website

def randomSleep():
    # Sleep for a random amount of time between 1 and 3 seconds
    time.sleep(random.randint(1, 3))


def scrollDown(driver):
    # Scroll down to bottom
    try:
        # perform action that may raise a JavascriptException
        # for example, scrolling to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  
    except JavascriptException:
        time.sleep(1) # if there are some problems with the javascript, i will wait 1 second and then go on with some other action


def scrollUp(driver):
    # Scroll up to top
    driver.execute_script("window.scrollTo(0, 0);")   


def refreshPage(driver):
    # Refresh the page
    time.sleep(0.2)
    driver.refresh()    


def mouseMovement(driver):
    # get the dimensions of the viewport
    # get the width and height of the screen
    screen_width = driver.execute_script("return window.innerWidth")
    screen_height = driver.execute_script("return window.innerHeight")
    # Move the mouse to a random position on the screen
    actions = ActionChains(driver)
    # move the mouse to random positions in the viewport
    times = random.randint(2, 6)
    try: 
        for i in range(times):
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_height)
            actions.move_by_offset(x, y).perform()
            actions.reset_actions()
    except MoveTargetOutOfBoundsException as e:
        time.sleep(1)


# functions that randomly choose a function from the group of functions above and execute it
def seleniumEscaping(driver):
    numberOfActions = random.randint(1, 3)
    for i in range(numberOfActions):
        index = random.randint(0, 4)

        if index == 0:
            randomSleep()
        elif index == 1:
            scrollDown(driver)
        elif index == 2:
            scrollUp(driver)
        elif index == 3:
            refreshPage(driver)
        elif index == 4:
            mouseMovement(driver)  


# i rotate the user agent to avoid being blocked by the website
userAgentDict = {
                    0: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
                    1: "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
                    2: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
                    3: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
                    4: "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
                    5: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
                    6: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
                    7: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
                }


def changeUserAgent():
    # change the user agent to avoid being blocked by the website, extract a random user agent from the dictionary and return it as a dictionary
    index = random.randint(0, len(userAgentDict) - 1)
    return userAgentDict[index]


def requestEscaping():
    numberOfActions = random.randint(1, 3)
    for i in range(numberOfActions):
        index = random.randint(0, 1)
        if index == 0:
            randomSleep()
        if index == 1:
            # the dictionary line extracted is in this form-> 0: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            # but had to became like this -> {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
            # so i can use it as a header
            userAgent = changeUserAgent()
            userAgent = {"User-Agent": userAgent}
            return userAgent
        
    randomSleep()  # if user agent remains the same i will stay idle for a random amount of time
    return "not changed"
