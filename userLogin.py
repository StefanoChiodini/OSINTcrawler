# here we will handle the login of the user and cookies if requested
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login(email, password, driver):
    # first i need to click the login button
    loginButton = driver.find_element(By.XPATH, '//*[@id="ember6"]/header/div/div/div[2]/span/button[2]')
    loginButton.click()
    time.sleep(0.3)

    # now i will fill the email and password fields
    emailField = driver.find_element(By.ID, "login-account-name")
    passwordField = driver.find_element(By.ID, "login-account-password")

    emailField.send_keys(email)
    time.sleep(1)
    passwordField.send_keys(password)
    time.sleep(1)

    loginButton = driver.find_element(By.ID, "login-button")
    loginButton.click()

    wait = WebDriverWait(driver, 10)  # wait for up to 10 seconds
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    wait.until(EC.presence_of_element_located((By.XPATH, "//a")))  # wait for at least one link to be present
    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")