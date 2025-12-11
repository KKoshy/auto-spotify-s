import os
import logging
import pytest
from libs.ui.home_page import HomePage
from libs.ui.locators import NavigationBarSelectors
from libs.ui.login_page import LoginPage
from libs.ui.playlist_details_page import PlaylistDetailsPage
from libs.ui.song_data import PlaylistData

log = logging.getLogger(__name__)

playlist_data = PlaylistData()

@pytest.fixture(scope='module')
def chrome(chrome_driver):
    home = HomePage(chrome_driver)
    home.click(NavigationBarSelectors.LOGIN_BUTTON)
    login = LoginPage(chrome_driver)
    login.wait_for_url().login(username=os.getenv('SPOTIFY_USER'), password=os.getenv('SPOTIFY_PASSWORD'))
    yield chrome_driver, home

class TestCreatePlaylist:
    @pytest.mark.dependency(name='create')
    def test_create_playlist(self, chrome):
        driver, home = chrome
        log.info(f"Validating playlist creation with driver {driver}")
        details = home.left_side_menu.create_playlist()
        playlist_data.pl_id = details.playlist_id
        details.update_details(playlist_data=playlist_data)
        details.should_have_playlist_name_desc(playlist_data=playlist_data)
        home.left_side_menu.should_have_playlist(playlist=playlist_data.name)

    @pytest.mark.dependency(name='add_track', depends=['create'])
    def test_add_track_to_playlist(self, chrome):
        driver, _ = chrome
        log.info("Validating track addition to the playlist")
        details = PlaylistDetailsPage(driver, playlist_data.pl_id)
        details.add_track_to_playlist("Believer", "Imagine Dragons", "Evolve")
        details.should_have_track_in_playlist("Believer", "Imagine Dragons", "Evolve")

    @pytest.mark.dependency(name='remove_track', depends=['add_track'])
    def test_remove_track_from_playlist(self, chrome):
        driver, _ = chrome
        log.info("Validating track removal from the playlist")
        details = PlaylistDetailsPage(driver, playlist_data.pl_id)
        details.remove_track_from_playlist("Believer", "Imagine Dragons", "Evolve")
        details.should_not_have_track_in_playlist("Believer", "Imagine Dragons", "Evolve")   

    @pytest.mark.dependency(depends=['create'])
    def test_delete_playlist(self, chrome):
        driver, home = chrome
        log.info("Validating playlist deletion")
        details = PlaylistDetailsPage(driver, playlist_data.pl_id)
        details.delete_playlist(playlist=playlist_data.name)
        home.left_side_menu.should_not_have_playlist(playlist=playlist_data.name)

