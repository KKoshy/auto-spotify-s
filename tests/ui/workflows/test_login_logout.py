import logging
import pytest
import os
from libs.ui.login_page import LoginPage
from libs.ui.home_page import HomePage
from libs.ui.locators import NavigationBarSelectors

log = logging.getLogger(__name__)

@pytest.fixture(scope='module')
def chrome(chrome_driver):
    yield chrome_driver

class TestLogin:
    def test_login(self, chrome):
        log.info("Validating login")
        home = HomePage(chrome)
        home.click(NavigationBarSelectors.LOGIN_BUTTON)
        login = LoginPage(chrome)
        login.wait_for_url().login(username=os.getenv('SPOTIFY_USER'), password=os.getenv('SPOTIFY_PASSWORD'))
        by, xpath = NavigationBarSelectors.USER_PROFILE_BUTTON
        assert home.wait_for_url().get_enabled_state((by, xpath.format(user_name='A'))), "Login failed"
        log.info("Login succeeded")

    def test_user_nav_bar(self, chrome):
        log.info("Validating Navigation bar elements post Login")
        home = HomePage(chrome)
        home.save_screenshot()
        assert home.get_enabled_state(NavigationBarSelectors.EXPLORE_PREMIUM_BUTTON)
        assert home.get_enabled_state(NavigationBarSelectors.INSTALL_APP_BUTTON)
        assert home.get_enabled_state(NavigationBarSelectors.WHATS_NEW_BUTTON)
        assert home.get_enabled_state(NavigationBarSelectors.FRIEND_ACTIVITY_BUTTON)

    def test_logout(self, chrome):
        log.info("Validating logout")
        home = HomePage(chrome)
        home.nav_bar.logout()
        assert home.wait_for_url().get_enabled_state(NavigationBarSelectors.LOGIN_BUTTON)
