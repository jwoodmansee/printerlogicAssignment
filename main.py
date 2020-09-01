from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json


def loginTest(browser, username, password):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()

    driver.get("https://jwoodmansee.printercloud.com/admin/")
    driver.find_element_by_id("relogin_user").send_keys(username)
    driver.find_element_by_id("relogin_password").send_keys(password)
    driver.find_element_by_id("admin-login-btn").send_keys(Keys.ENTER)
    time.sleep(10)
    driver.quit()


def testForgotPassword(browser, email):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()

    driver.get("https://jwoodmansee.printercloud.com/admin/")
    driver.find_element_by_id("forgot-password").click()
    if driver.current_url == "https://jwoodmansee.printercloud.com/admin/password/reset/":
        driver.find_element_by_id("email").send_keys(email)

    time.sleep(5)
    driver.quit()


def run():
    with open("config.json") as config:
        jsonData = json.load(config)
    browsers = ["chrome", "firefox", "safari"]
    print(browsers)
    for b in range(len(browsers)):
        loginTest(browsers[b], jsonData["userName"], jsonData["password"])
        testForgotPassword(browsers[b], jsonData["email"])


if __name__ == "__main__":
    run()
