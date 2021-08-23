from password import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP

    def get_internet_speed(self):
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        driver.get(SPEEDTEST_URL)

        cookie = driver.find_element_by_id("_evidon-banner-acceptbutton")
        cookie.click()

        go_button = driver.find_element_by_class_name("start-text")
        go_button.click()

        time.sleep(60)

        pop_up = driver.find_element_by_xpath(
            "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a")
        pop_up.click()

        time.sleep(5)

        print("GET")

        results = driver.find_elements_by_xpath("//div[@class='result-data u-align-left']")

        print(f"Ping: {results[0].text}")
        print(f"Download: {results[1].text}")
        print(f"Upload: {results[2].text}")

        for result in results:
            print(result.text)

    def tweet_at_provider(self):
        print("TWEET")
