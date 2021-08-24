from password import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
        self.message = ""

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
        time.sleep(1)

        results = driver.find_elements_by_xpath("//div[@class='result-data u-align-left']")

        self.message = f"Ping: {results[0].text}\nDownload: {results[1].text}\nUpload: {results[2].text}"

    def tweet_at_provider(self):
        print("TWEET")
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        driver.get(TWITTER_URL_LOGIN)

        input_email_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "session["
                                                                                                   "username_or_email]")))
        input_email_box.send_keys(USER_TWITTER_EMAIL)

        input_password_box = driver.find_element_by_name("session[password]")
        input_password_box.send_keys(USER_TWITTER_PASSWORD)
        time.sleep(random.randint(1, 5))
        input_password_box.send_keys(Keys.ENTER)

        try:
            input_name_box = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.NAME, "session["
                                                                                                       "username_or_email]")))
            input_name_box.send_keys(USER_NAME)
            input_password_box = driver.find_element_by_name("session[password]")
            input_password_box.send_keys(USER_TWITTER_PASSWORD)
            time.sleep(random.randint(1, 5))
            input_password_box.send_keys(Keys.ENTER)
        except:
            pass

        PATH = "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div"
        text = driver.find_element_by_xpath(PATH)
        text.send_keys(self.message)

        time.sleep(1)

        tweet_button = driver.find_element(By.XPATH, "//div[@data-testid='tweetButtonInline']")
        tweet_button.click()
