import os
import logging
import pytest
from libs.ui.home_page import HomePage
from libs.ui.locators import NavigationBarSelectors, LeftSideBarSelectors
from libs.ui.login_page import LoginPage
from libs.ui.song_data import PlaylistData

log = logging.getLogger(__name__)


@pytest.fixture(scope='module')
def chrome(chrome_driver):
    home = HomePage(chrome_driver)
    home.click(NavigationBarSelectors.LOGIN_BUTTON)
    login = LoginPage(chrome_driver)
    login.wait_for_url().login(username=os.getenv('SPOTIFY_USER'), password=os.getenv('SPOTIFY_PASSWORD'))
    yield chrome_driver, home

class TestCreatePlaylist:
    def test_create_playlist(self, chrome):
        driver, home = chrome
        log.info(f"Validating playlist creation with driver {driver}")
        home = HomePage(driver)
        details = home.left_side_menu.create_playlist()
        details.update_details(playlist_data=PlaylistData)
        details.should_have_playlist_name_desc(playlist_data=PlaylistData)
        

