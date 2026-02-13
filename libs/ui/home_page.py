"""
POM for Home Page
"""

from libs.ui.base_page import BasePage
from libs.ui.navigation_page import NavigationBar
from libs.ui.left_sidebar_page import LeftSideBarPage
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    def __init__(self, driver):
        self.url = r"^https://open.spotify.com"
        self.driver = driver
        self.nav_bar = NavigationBar(driver)
        self.left_side_menu = LeftSideBarPage(driver)
        super().__init__(driver)

    def wait_for_url(self):
        """
        Wait for the page URL

        :return: self for method chaining
        """
        self.wait.until(EC.url_matches(self.url))
        return self
