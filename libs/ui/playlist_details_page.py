import logging
from libs.ui.locators import PlaylistDetailsPageSelectors
from libs.ui.base_page import BasePage
from libs.ui.song_data import PlaylistData
from selenium.webdriver.support import expected_conditions as EC

log = logging.getLogger(__name__)

class PlaylistDetailsPage(BasePage):
    def __init__(self, driver, playlist_id):
        self.url = f"https://open.spotify.com/playlist/{playlist_id}"
        self.driver = driver
        super().__init__(driver)

    def update_details(self, playlist_data: PlaylistData) -> "PlaylistDetailsPage":
        """
        Updating details of the playlist
        
        :param playlist_data: data class instance of PlaylistData
        :return: current instance of the PlaylistDetailsPage
        """
        log.info("Updating details of playlist")
        self.click(PlaylistDetailsPageSelectors.MORE_BUTTON)
        self.click(PlaylistDetailsPageSelectors.EDIT_DETAILS)
        assert self.get_displayed_state(PlaylistDetailsPageSelectors.PL_DETAILS_MODAL)
        self.type(PlaylistDetailsPageSelectors.PL_NAME_INPUT, playlist_data.name)
        self.type(PlaylistDetailsPageSelectors.PL_DESC_INPUT, playlist_data.description)
        self.save_screenshot()
        self.click(PlaylistDetailsPageSelectors.SAVE_BUTTON)
        self.wait.until(EC.invisibility_of_element_located(PlaylistDetailsPageSelectors.PL_DETAILS_MODAL))
        self.save_screenshot()
        return self
    
    def search_song(self, song: str):
        self.type(PlaylistDetailsPageSelectors.SEARCH_BAR, song)
        return self

    def should_have_playlist_name_desc(self, playlist_data: PlaylistData) -> "PlaylistDetailsPage":
        """
        Validating playlist name
        
        :param playlist_data: data class instance of PlaylistData
        :return: current instance of the PlaylistDetailsPage
        """
        log.info("Verifying the playlist name")
        assert self.get_text(PlaylistDetailsPageSelectors.PL_TITLE) == playlist_data.name
        by, xpath = PlaylistDetailsPageSelectors.PL_DESCRIPTION
        assert self.get_displayed_state((by, xpath.format(description=playlist_data.description)))
        return self

