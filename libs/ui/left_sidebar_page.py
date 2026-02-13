"""
POM for Left side bar
"""

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
    
    def open_library(self) -> "LeftSideBarPage":
        """
        Opening the library
        
        :return: current instance of LeftSideBarPage
        """
        log.info("Open library")
        if not self.get_enabled_state(LeftSideBarSelectors.COLLAPSE_LIBRARY):
            self.click(LeftSideBarSelectors.OPEN_LIBRARY)
            assert self.get_enabled_state(LeftSideBarSelectors.COLLAPSE_LIBRARY)
        return self
    
    def search_playlist(self, playlist: str) -> "LeftSideBarPage":
        """
        Search for the playlist in library
        
        :param playlist: playlist name
        :return: current instance of LeftSideBarPage
        """
        log.info(f"Searching for playlist {playlist}")
        if not self.get_displayed_state(LeftSideBarSelectors.SEARCH_BAR):
            self.click(LeftSideBarSelectors.SEARCH_BUTTON)
        self.type(LeftSideBarSelectors.SEARCH_BAR, playlist)
        return self
    
    def should_have_playlist(self, playlist: str) -> "LeftSideBarPage":
        """
        Validating the presence of playlist in the library
        
        :param playlist: playlist name
        :return: current instance of LeftSideBarPage
        """
        log.info(f"Validating the presence of playlist {playlist}")
        self.search_playlist(playlist=playlist)
        by, xpath = LeftSideBarSelectors.PLAYLIST_TEMPLATE
        assert self.get_displayed_state((by, xpath.format(playlist=playlist)))
        return self
    
    def should_not_have_playlist(self, playlist: str) -> "LeftSideBarPage":
        """
        Validating the absence of playlist in the library
        
        :param playlist: playlist name
        :return: current instance of LeftSideBarPage
        """
        log.info(f"Validating the absence of playlist {playlist}")
        self.search_playlist(playlist=playlist)
        by, xpath = LeftSideBarSelectors.PLAYLIST_TEMPLATE
        assert not self.get_displayed_state((by, xpath.format(playlist=playlist)))
        return self

