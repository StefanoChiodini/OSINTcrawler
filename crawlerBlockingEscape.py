import random 
import time

# group of functions to help escape blocking techniques when crawling a website

def randomSleep():
    # Sleep for a random amount of time between 1 and 3 seconds
    time.sleep(random.randint(1, 3))

def scrollDown(driver):
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  

def scrollUp(driver):
    # Scroll up to top
    driver.execute_script("window.scrollTo(0, 0);")       

# functions that randomly choose a function from the group of functions above and execute it
def escaping(driver):
    index = random.randint(0, 2)
    if index == 0:
        randomSleep()
    elif index == 1:
        scrollDown(driver)
    elif index == 2:
        scrollUp(driver)       