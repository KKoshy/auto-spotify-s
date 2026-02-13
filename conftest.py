"""
Pytest configuration
"""

from selenium.webdriver import Chrome
import pytest
import os
import allure
from pathlib import Path
import logging
from selenium.webdriver.chrome.options import Options
from libs.api.artists.artists_api import ArtistsAPI
from libs.api.playlists.playlists_api import PlaylistsAPI
from libs.api.users.users_api import UsersAPI

log = logging.getLogger(__name__)


@pytest.fixture(scope='module')
def chrome_driver():
    options = Options() 
    # options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.headless = False
    driver = Chrome(options=options)
    driver.get("https://open.spotify.com")
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def artists():
    return ArtistsAPI(client_id=os.getenv('SPOTIFY_CLIENT_ID'), 
                      client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'))

@pytest.fixture(scope="module")
def playlists():
    return PlaylistsAPI(client_id=os.getenv('SPOTIFY_CLIENT_ID'), 
                        client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'), 
                        refresh_token=os.getenv('SPOTIFY_REFRESH_TOKEN'))

@pytest.fixture(scope="module")
def users():
    return UsersAPI(client_id=os.getenv('SPOTIFY_CLIENT_ID'), 
                    client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'), 
                    refresh_token=os.getenv('SPOTIFY_REFRESH_TOKEN'))

@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(items):
    """
    Modifying the test cases before it starts
    """
    repo = "auto-spot-s"
    for item in items:
        item.add_marker(allure.story(repo))
        _file = Path(item.nodeid.split("::")[0])
        item.add_marker(allure.parent_suite(repo))
        suite = "".join(_file.parent.parts[1])
        item.add_marker(allure.suite(suite))
        sub_suite = "".join(_file.parent.parts[2:])
        item.add_marker(allure.sub_suite(sub_suite))
