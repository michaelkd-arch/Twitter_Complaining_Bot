from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from fake_useragent import FakeUserAgent
import time
import random
import os

URL = "https://twitter.com"


class TwitterManager:
    def __init__(self):
        self.ua = FakeUserAgent()
        self.user_agent = self.ua.random
        self.options = webdriver.ChromeOptions()
        # self.options.add_experimental_option("detach", True)
        # self.options.add_argument(f"user_agent={self.user_agent}")
        self.options.add_experimental_option("debuggerAddress", "localhost:8989")
        self.driver = webdriver.Chrome(options=self.options)

    def send_message(self, message):
        self.driver.get(url=URL)
        self.driver.maximize_window()
        time.sleep(3)
        input_post = self.driver.find_element(By.XPATH,
                                              '//*[@id="react-root"]/div/div/div[2]'
                                              '/main/div/div/div/div[1]/div/div[3]/div'
                                              '/div[2]/div[1]/div/div/div/div[2]/div[1]'
                                              '/div/div/div/div/div/div/div/div/div/div'
                                              '/label/div[1]/div/div')
        input_post.click()
        time.sleep(1)
        input_type = self.driver.find_element(By.XPATH,
                                              '//*[@id="react-root"]/div/div'
                                              '/div[2]/main/div/div/div/div[1]/div'
                                              '/div[3]/div/div[2]/div[1]/div/div/div'
                                              '/div[2]/div[1]/div/div/div/div/div/div'
                                              '/div/div/div/div/label/div[1]/div/div'
                                              '/div/div/div/div[2]/div/div/div/div')
        input_type.send_keys(message)
        time.sleep(1)
        post_button = self.driver.find_element(By.XPATH,
                                               '//*[@id="react-root"]/div/div/div[2]/main'
                                               '/div/div/div/div[1]/div/div[3]/div/div[2]'
                                               '/div[1]/div/div/div/div[2]/div[2]/div[2]'
                                               '/div/div/div/div[3]/div/span/span')
        post_button.click()
        time.sleep(1)
        self.driver.quit()

    def deploy(self):
        self.driver.get(url=URL)
        time.sleep(3)
        iframe = self.driver.find_element(By.TAG_NAME, 'iframe')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/span[1]').click()
        time.sleep(1)
        parent_window = str(self.driver.current_window_handle)
        all_window_handles = self.driver.window_handles
        for i in all_window_handles:
            if str(i) != parent_window:
                self.driver.switch_to.window(i)
        time.sleep(1)
        input_field = self.driver.find_element(By.XPATH, '//*[@id="identifierId"]')
        input_field.send_keys(os.environ['U_EMAIL_ACCOUNT_NAME'])
        input_field.send_keys(Keys.ENTER)
        time.sleep(2)
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
        password_field.send_keys(os.environ["U_KEY"])
        password_field.send_keys(Keys.ENTER)
        self.driver.switch_to.window(parent_window)
        time.sleep(2)
        