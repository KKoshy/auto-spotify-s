import logging
import pytest
from libs.ui.home_page import HomePage
from libs.ui.locators import HomePageSelectors, NavigationBarSelectors


log = logging.getLogger(__name__)

@pytest.fixture(scope='module')
def home(chrome_driver):
    home = HomePage(chrome_driver)
    yield home
    home.save_screenshot()

class TestNavigationBar:
    def test_home_button(self, home):
        log.info("Checking for Home button state")
        assert home.get_displayed_state(NavigationBarSelectors.HOME_BUTTON)

    def test_search_bar(self, home):
        log.info("Checking for search bar elements")
        assert home.get_enabled_state(NavigationBarSelectors.SEARCH_BUTTON)
        assert home.get_displayed_state(NavigationBarSelectors.SEARCH_INPUT)
        assert home.get_enabled_state(NavigationBarSelectors.SEARCH_CLEAR_BUTTON)
        assert home.get_enabled_state(NavigationBarSelectors.BROWSE_BUTTON)

    def test_premium_button(self, home):
        log.info("Checking for Premium button")
        assert home.get_enabled_state(NavigationBarSelectors.PREMIUM_BUTTON)

    def test_support_button(self, home):
        log.info("Checking for Support button")
        assert home.get_enabled_state(NavigationBarSelectors.SUPPORT_BUTTON)

    def test_download_button(self, home):
        log.info("Checking for Download button")
        assert home.get_enabled_state(NavigationBarSelectors.DOWNLOAD_BUTTON)

    def test_install_app_button(self, home):
        log.info("Checking for Install App button")
        assert home.get_enabled_state(NavigationBarSelectors.INSTALL_APP_BUTTON)

    def test_sign_up_button(self, home):
        log.info("Checking for Sign up button")
        assert home.get_enabled_state(NavigationBarSelectors.SIGN_UP_BUTTON)

    def test_login_button(self, home):
        log.info("Checking for Login button")
        assert home.get_enabled_state(NavigationBarSelectors.LOGIN_BUTTON)

class TestLeftSideBar:
    def test_library_header(self, home):
        log.info("Checking for Your library header")
        assert home.get_displayed_state(HomePageSelectors.YOUR_LIBRARY_HEADER)

    def test_create_playlist(self, home):
        log.info("Checking for Create Playlist button")
        assert home.get_enabled_state(HomePageSelectors.CREATE_PL_FL)
        home.click(HomePageSelectors.CREATE_PL_FL)
        assert home.get_enabled_state(HomePageSelectors.CREATE_PLAYLIST_OPTION)

class TestLegalLinks:
    def test_legal_link(self, home):
        log.info("Checking for Legal link")
        assert home.get_enabled_state(HomePageSelectors.LEGAL_LINK)

    def test_safety_and_privacy_center(self, home):
        log.info("Checking for Safety and Privacy Center link")
        assert home.get_enabled_state(HomePageSelectors.SAFETY_AND_PRIVACY_LINK)

    def test_privacy_policy_link(self, home):
        log.info("Checking for Privacy policy link")
        assert home.get_enabled_state(HomePageSelectors.PRIVACY_POLICY_LINK)

    def test_cookies_link(self, home):
        log.info("Checking for Cookies link")
        assert home.get_enabled_state(HomePageSelectors.COOKIES_LINK)

    def test_about_ads_link(self, home):
        log.info("Checking for About Ads link")
        assert home.get_enabled_state(HomePageSelectors.ABOUT_ADS_LINK)

    def test_accessibility_link(self, home):
        log.info("Checking for Accessibility link")
        assert home.get_enabled_state(HomePageSelectors.ACCESSIBILITY_LINK)
