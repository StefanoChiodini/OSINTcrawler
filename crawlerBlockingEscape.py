import random 
import time
from selenium.webdriver.common.action_chains import ActionChains

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

def refreshPage(driver):
    # Refresh the page
    time.sleep(0.2)
    driver.refresh()    

# TODO: THIS FUNCTION IS NOT WORKING
def mouseMovement(driver):
    # get the dimensions of the viewport
    # get the width and height of the screen
    screen_width = driver.execute_script("return window.innerWidth")
    screen_height = driver.execute_script("return window.innerHeight")
    # Move the mouse to a random position on the screen
    actions = ActionChains(driver)
    # move the mouse to random positions in the viewport
    times = random.randint(2, 6)
    for i in range(times):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        actions.move_by_offset(x, y).perform()
        actions.reset_actions()

# functions that randomly choose a function from the group of functions above and execute it
def escaping(driver):
    index = random.randint(0, 2)
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