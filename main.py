from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# chromeDriver = webdriver.Chrome()
# # foxDriver = webdriver.Firefox()


def loginTest(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()

    driver.get("https://jwoodmansee.printercloud.com/admin/")
    print(driver.current_url)
    driver.find_element_by_id("relogin_user").send_keys("username")
    driver.find_element_by_id("relogin_password").send_keys("password")
    driver.find_element_by_id("admin-login-btn").send_keys(Keys.ENTER)
    print(driver.title)
    time.sleep(10)
    driver.quit()


# # def loginTest_FireFox():
# #     foxDriver.get("https://jwoodmansee.printercloud.com/admin/")
# #     print(foxDriver.current_url)
# #     # foxDriver.find_element_by_id("relogin_user").send_keys("username")
# #     # foxDriver.find_element_by_id("relogin_password").send_keys("password")
# #     # foxDriver.find_element_by_id("admin-login-btn").send_keys(Keys.ENTER)
# #     # print(foxDriver.title)
# #     # time.sleep(30)
# #     foxDriver.close()

def testForgotPassword(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()

    driver.get("https://jwoodmansee.printercloud.com/admin/")
    driver.find_element_by_id("forgot-password").click()
    print(driver.current_url)


# loginTest_Chrome()
# # loginTest_FireFox()

def run():
    browsers = ["chrome", "firefox", "safari"]
    print(browsers)
    for b in range(len(browsers)):
    #     # print(drivers[d])
    #     loginTest(browsers[b])
        testForgotPassword(browsers[b])
    


if __name__ == "__main__":
    run()
