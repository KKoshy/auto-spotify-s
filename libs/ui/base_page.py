import os
import allure
from uuid import uuid4
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def get_enabled_state(self, locator):
        return self.find(locator).is_enabled()

    def get_displayed_state(self, locator):
        return self.find(locator).is_displayed()
    
    def save_screenshot(self):
        img_path = os.path.join("allure-report", "{}.png".format(uuid4()))
        self.driver.save_screenshot(img_path)
        allure.attach.file(source=img_path)
