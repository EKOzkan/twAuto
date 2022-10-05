import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from socket import timeout
from os.path import exists
import os
import requests
import bs4
from bs4 import BeautifulSoup
from urllib import request


class twAuto:
    driver = None
    cookies_exists = exists('cookies.pkl')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])

    def __init__(
        self,
        password="",
        username="",
        email="",
        user_agent=None,
        headless=True
    ):
        self.email = email
        self.username = username
        self.password = password
        if headless:
            twAuto.chrome_options.add_argument('--headless')

    # start selenium driver
    def start(self):
        twAuto.driver = webdriver.Chrome(
            "chromedriver.exe", options=twAuto.chrome_options)

    # test function to open twitter on chrome
    def openTw(self):
        twAuto.driver.get("https://twitter.com/home")

    # login to twitter
    def login(self):
        twAuto.driver.get("https://twitter.com/")
        # this cookie importing prevents 'New login notification" in every action
        if twAuto.cookies_exists:
            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                twAuto.driver.add_cookie(cookie)
        if twAuto.cookies_exists:
            twAuto.driver.get("https://twitter.com/")
        else:
            twAuto.driver.get("https://twitter.com/login")
            try:
                wait = WebDriverWait(twAuto.driver, 120)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")))
            except TimeoutException:
                pass
            mailInput = twAuto.driver.find_element(
                'xpath', "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
            mailInput.send_keys(self.email)
            twAuto.driver.find_element(
                'xpath', "//div[@class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu']").click()
            time.sleep(3)

            try:
                userNameInput = twAuto.driver.find_element(
                    'xpath', "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            except:
                userNameInput = twAuto.driver.find_element(
                    'xpath', "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")

            userNameInput.send_keys(self.username)

            twAuto.driver.find_element(
                'xpath', "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div").click()

            try:
                wait = WebDriverWait(twAuto.driver, 120)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")))
            except TimeoutException:
                pass
            passwordInput = twAuto.driver.find_element(
                'xpath', "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            passwordInput.send_keys(self.password)
            twAuto.driver.find_element(
                'xpath', "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div").click()

        try:
            wait = WebDriverWait(twAuto.driver, 120)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[1]")))
            print("Succesfully Logged In")
        except TimeoutException:
            print('Login Error')

        twAuto.driver.get("https://twitter.com/Twitter/")

        if not twAuto.cookies_exists:
            pickle.dump(twAuto.driver.get_cookies(), open("cookies.pkl", "wb"))

    # tweet text
    def tweet(self, imgpath=None, text=""):
        # load tweeting page
        twAuto.driver.get('https://twitter.com/compose/tweet')

        # try finding tweet inbox
        try:
            wait = WebDriverWait(twAuto.driver, 120)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div")))
        except TimeoutException:
            print('Couldnt tweet.')

        # modify tweet text
        full_text = text

        input_field = twAuto.driver.find_element(
            'xpath', "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div")
        input_field.send_keys(full_text)

        try:
            wait = WebDriverWait(twAuto.driver, 120)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]")))
        except TimeoutException:
            print('Couldnt tweet.')
        if imgpath != None:
            element = twAuto.driver.find_element(
                By.XPATH, "//input[@type='file']")
            '''//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[1]/div[1]'''
            twAuto.driver.execute_script(
                "arguments[0].style.display = 'block';", element)

            element.send_keys(imgpath)

        twAuto.driver.find_element(By.XPATH,
                                   '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]').click()
        try:
            wait = WebDriverWait(twAuto.driver, 5)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div[2]/a/span")))
            twAuto.driver.find_element(
                'xpath', "//*[@id='layers']/div[2]/div/div/div/div/div[2]/a/span").click()
            tweetUrl = twAuto.driver.current_url
            print("Tweeted Successfully")
            print("Tweet URL:"+tweetUrl)
            return tweetUrl
        except TimeoutException:
            try:
                twAuto.driver.find_element(
                    'xpath', "//*[@id='layers']/div[3]/div/div/div/div/div[1]")
                print('Couldnt Tweet.')
                return None
            except:
                try:
                    wait = WebDriverWait(twAuto.driver, 5)
                    wait.until(EC.presence_of_element_located(
                        (By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div[2]/a/span")))
                    twAuto.driver.find_element(
                        By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div[2]/a/span").click()
                    tweetUrl = twAuto.driver.current_url
                    print("Tweeted Successfully")
                    print("Tweet URL:"+tweetUrl)
                except:
                    print('Couldnt Tweet.')
                    return None

    # quote tweet. this function uses the "adding the quoted tweets url to end of the text method" but maybe i will add the another version of this function that uses the quote tweet function later
    def quoteTweet(self, url="", text=""):
        modified_text = text + "\n" + url
        result = self.tweet(text=modified_text)
        if result == None:
            print('Quote Tweet Failed')
            return None
        else:
            print('Quoted Tweet Successfully')
            print('Quote Tweet URL:'+result)
            return result

    # retweet and like functions are not working with tweets or replies with no text. I will fix it in the future.
    def retweet(self, url=""):
        twAuto.driver.get(url)
        container_element = self.findTweet(url=url)
        try:
            try:
                body_element = container_element.find_element(
                    By.XPATH, './/div[3]/div[8]/div/div[2]/div')
            except:
                body_element = container_element.find_element(
                    By.XPATH, './/div[3]/div[7]/div/div[2]/div')
            body_element.click()
            try:
                retweetButton = twAuto.driver.find_element(
                    By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div')
                retweetButton.click()
                return True
            except:
                return False
        except:
            return False

    # likes tweet
    def like(self, url=""):
        twAuto.driver.get(url)
        container_element = self.findTweet(url=url)
        try:
            try:
                body_element = container_element.find_element(
                    By.XPATH, './/div[3]/div[8]/div/div[3]/div')
            except:
                body_element = container_element.find_element(
                    By.XPATH, './/div[3]/div[7]/div/div[3]/div')
            body_element.click()
            return True
        except:
            return False

    # reply to a tweet
    def reply(self, url="", text=""):
        twAuto.driver.get(url)
        container_element = self.findTweet(url=url)
        try:
            try:
                body_element = container_element.find_element(
                    By.XPATH, './/div[3]/div[8]/div/div[1]/div')
            except:
                body_element = container_element.find_element(
                    By.XPATH, './/div[3]/div[7]/div/div[1]/div')
            body_element.click()
            try:
                wait = WebDriverWait(twAuto.driver, 5)
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div")))
                twAuto.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div").send_keys(text+" ")
                tweetReplyButton = twAuto.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]")
                tweetReplyButton.click()
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/a")))
                replyURL = twAuto.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/a").get_attribute("href")
                return replyURL
            except:
                return False
        except:
            return False

    # locates tweet in the page based on the tweets content
    def findTweet(self, url=""):
        twAuto.driver.get(url)
        try:
            wait = WebDriverWait(twAuto.driver, 120)
            wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".css-1dbjc4n.r-18u37iz.r-15zivkp")))
            time.sleep(1)
            tmp_element = twAuto.driver.find_element(
                By.CSS_SELECTOR, ".css-1dbjc4n.r-18u37iz.r-15zivkp")
            container_element = tmp_element.find_element(By.XPATH, '..')
            return container_element
        except TimeoutException:
            return None

    # logs out from twitter and deletes the cookies
    def logout(self):
        twAuto.driver.get("https://twitter.com/logout")
        try:
            wait = WebDriverWait(twAuto.driver, 120)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]")))
        except TimeoutException:
            print('Couldnt log out.')
        twAuto.driver.find_element(
            'xpath', "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]").click()
        os.remove("cookies.pkl")
        print("Succesfully logged out")

    # closes selenium driver
    def close(self):
        twAuto.driver.quit()
