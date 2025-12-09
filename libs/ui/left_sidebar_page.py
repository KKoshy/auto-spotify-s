import logging
import re
from libs.ui.base_page import BasePage
from libs.ui.locators import LeftSideBarSelectors
from libs.ui.playlist_details_page import PlaylistDetailsPage
from selenium.webdriver.support import expected_conditions as EC

log = logging.getLogger(__name__)

class LeftSideBarPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def create_playlist(self) -> "PlaylistDetailsPage":
        """
        Create a new playlist

        :return: New instance of PlaylistDetails page
        """
        log.info("Creating playlist")
        self.click(LeftSideBarSelectors.CREATE_PL_FL)
        self.click(LeftSideBarSelectors.CREATE_PLAYLIST_OPTION)
        pattern = rf'{self.base_url}/playlist/([a-zA-Z0-9]+)'
        self.wait.until(EC.url_matches(pattern))
        pl_id = re.findall(pattern, self.driver.current_url)[0]
        return PlaylistDetailsPage(self.driver, pl_id)
