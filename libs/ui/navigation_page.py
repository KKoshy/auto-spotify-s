import logging
from libs.ui.base_page import BasePage
from libs.ui.locators import NavigationBarSelectors

log = logging.getLogger(__name__)

class NavigationBar(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def logout(self):
        """
        Log out of the current account
        """
        log.info("Logging out")
        self.click(NavigationBarSelectors.USER_WIDGET_BUTTON)
        self.save_screenshot()
        self.click(NavigationBarSelectors.LOGOUT_BUTTON)
        return self
