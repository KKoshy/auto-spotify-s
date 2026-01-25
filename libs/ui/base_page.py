import os
import time
import allure
from uuid import uuid4
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://open.spotify.com"
        self.wait = WebDriverWait(driver, 35)

    def find(self, locator: tuple, condition: object = EC.presence_of_element_located, timeout_ignore: bool=False):
        try:
            return self.wait.until(condition(locator))
        except TimeoutException as e:
            if timeout_ignore:
                return False
            raise e

    def click(self, locator: tuple):
        self.find(locator, condition=EC.element_to_be_clickable).click()

    def get_text(self, locator: tuple):
        return self.find(locator).text

    def type(self, locator: tuple, text: str):
        element = self.find(locator)
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.DELETE)
        for ch in text:
            element.send_keys(ch)
            time.sleep(0.08)

    def get_enabled_state(self, locator: tuple):
        try: 
            return self.find(locator).is_enabled()
        except TimeoutException:
            return False

    def get_displayed_state(self, locator: tuple):
        try:
            return self.find(locator).is_displayed()
        except TimeoutException:
            return False
    
    def save_screenshot(self):
        img_path = os.path.join("allure-results", "{}.png".format(uuid4()))
        self.driver.save_screenshot(img_path)
        allure.attach.file(source=img_path)
