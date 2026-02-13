"""
POM for Playlist details page
"""

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
        self.playlist_id = playlist_id
        super().__init__(driver)

    def update_details(self, playlist_data: PlaylistData) -> "PlaylistDetailsPage":
        """
        Updating details of the playlist
        
        :param playlist_data: data class instance of PlaylistData
        :return: current instance of the PlaylistDetailsPage
        """
        log.info("Updating details of playlist")
        self.click(PlaylistDetailsPageSelectors.PLAYLIST_MORE_BUTTON)
        self.click(PlaylistDetailsPageSelectors.EDIT_DETAILS)
        assert self.get_displayed_state(PlaylistDetailsPageSelectors.PL_DETAILS_MODAL)
        self.type(PlaylistDetailsPageSelectors.PL_NAME_INPUT, playlist_data.name)
        self.type(PlaylistDetailsPageSelectors.PL_DESC_INPUT, playlist_data.description)
        self.save_screenshot()
        self.click(PlaylistDetailsPageSelectors.SAVE_BUTTON)
        self.wait.until(EC.invisibility_of_element_located(PlaylistDetailsPageSelectors.PL_DETAILS_MODAL))
        self.save_screenshot()
        return self
    
    def remove_track_from_playlist(self, track: str, artist: str, album: str) -> "PlaylistDetailsPage":
        """
        Remove track from the playlist
        
        :param track: track name
        :param artist: artist name
        :param album: album name
        :return: current instance of the PlaylistDetailsPage
        """
        log.info(f"Removing track {track} by {artist} from {album} from the playlist")
        by, xpath = PlaylistDetailsPageSelectors.TRACK_MORE_BUTTON
        self.click((by, xpath.format(track=track, artist=artist, album=album)))
        self.click(PlaylistDetailsPageSelectors.REMOVE_TRACK)
        self.wait.until(EC.invisibility_of_element_located((by, xpath.format(track=track, artist=artist, album=album))))
        return self
    
    def add_track_to_playlist(self, track: str, artist: str, album: str) -> "PlaylistDetailsPage":
        """
        Add track to the playlist
        
        :param track: track name
        :param artist: artist name
        :param album: album name
        :return: current instance of the PlaylistDetailsPage
        """
        log.info(f"Adding track {track} by {artist} from {album} to the playlist")
        self.search_track(track=track)
        self.should_have_track_in_search_result(track=track, artist=artist, album=album)
        by, xpath = PlaylistDetailsPageSelectors.ADD_BUTTON_TEMPLATE
        self.click((by, xpath.format(track=track, artist=artist, album=album)))
        return self
    
    def search_track(self, track: str) -> "PlaylistDetailsPage":
        """
        Search tracks in the playlist details page
        
        :param track: track name
        :return: current instance of the PlaylistDetailsPage
        """
        log.info(f"Searching for track {track}")
        self.type(PlaylistDetailsPageSelectors.SEARCH_BAR, track)
        return self
    
    def delete_playlist(self, playlist: str) -> "PlaylistDetailsPage":
        """
        Deletes the playlist
        
        :param playlist: playlist name
        :return: current instance of the PlaylistDetailsPage
        """
        log.info("Deleting the playlist")
        self.click(PlaylistDetailsPageSelectors.PLAYLIST_MORE_BUTTON)
        self.click(PlaylistDetailsPageSelectors.DELETE_PLAYLIST)
        self.should_have_delete_dialog(playlist=playlist)
        self.click(PlaylistDetailsPageSelectors.DELETE_BUTTON)
        self.wait.until(EC.invisibility_of_element_located(PlaylistDetailsPageSelectors.DELETE_DIALOG))
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
    
    def should_have_track_in_search_result(self, track: str, artist: str, album: str) -> "PlaylistDetailsPage":
        """
        Validating track is listed in the search result
        
        :param track: track name
        :param artist: artist name
        :param album: album name
        :return: current instance of the PlaylistDetailsPage
        """
        log.info("Validating presence of the track in search result")
        by, xpath = PlaylistDetailsPageSelectors.SEARCH_TRACKLIST_ROW_TEMPLATE
        assert self.get_enabled_state((by, xpath.format(track=track, artist=artist, album=album)))
        return self
    
    def should_have_track_in_playlist(self, track: str, artist: str, album: str) -> "PlaylistDetailsPage":
        """
        Validating track is listed in the playlist
        
        :param track: track name
        :param artist: artist name
        :param album: album name
        :return: current instance of the PlaylistDetailsPage
        """
        log.info("Validating presence of the track in the playlist")
        by, xpath = PlaylistDetailsPageSelectors.PLAYLIST_TRACK_ROW_TEMPLATE
        assert self.get_enabled_state((by, xpath.format(track=track, artist=artist, album=album)))
        return self
    
    def should_not_have_track_in_playlist(self, track: str, artist: str, album: str) -> "PlaylistDetailsPage":
        """
        Validating track is not listed in the playlist
        
        :param track: track name
        :param artist: artist name
        :param album: album name
        :return: current instance of the PlaylistDetailsPage
        """
        log.info("Validating absence of the track in the playlist")
        by, xpath = PlaylistDetailsPageSelectors.PLAYLIST_TRACK_ROW_TEMPLATE
        assert not self.get_enabled_state((by, xpath.format(track=track, artist=artist, album=album)))
        return self
    
    def should_have_delete_dialog(self, playlist: str) -> "PlaylistDetailsPage":
        """
        Validating the presence of delete dialog
        
        :param playlist: playlist name
        :return: current instance of the PlaylistDetailsPage
        """
        log.info("Validating the presence of delete dialog")
        by, xpath = PlaylistDetailsPageSelectors.DELETE_DIALOG
        assert self.get_displayed_state((by, xpath.format(playlist=playlist)))
        by, xpath = PlaylistDetailsPageSelectors.DELETE_DIALOG_MESSAGE
        assert self.get_displayed_state((by, xpath.format(playlist=playlist)))
        return self
