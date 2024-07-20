from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from fake_useragent import FakeUserAgent
import time
import random

URL = "https://www.speedtest.net/"


class SpeedManager:
    def __init__(self):
        self.ua = FakeUserAgent()
        self.user_agent = self.ua.random
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument(f"user_agent={self.user_agent}")
        self.driver = webdriver.Chrome(options=self.options)

    def test_speed(self):
        self.driver.get(url=URL)
        self.driver.maximize_window()
        time.sleep(2)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        time.sleep(70)
        download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed").text.replace(" -", "")
        upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed").text.replace(" -", "")
        self.driver.quit()
        return [download_speed, upload_speed]
