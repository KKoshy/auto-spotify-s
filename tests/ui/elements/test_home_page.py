import logging
import pytest
from libs.ui.home_page import HomePage
from libs.ui.locators import HomePageSelectors


log = logging.getLogger(__name__)

@pytest.fixture(scope='module')
def home(chrome_driver):
    home = HomePage(chrome_driver)
    yield home


def test_home_button(home):
    log.info("Checking for Home button state")
    assert home.get_displayed_state(HomePageSelectors.HOME_BUTTON)


def test_search_bar(home):
    log.info("Checking for search bar elements")
    assert home.get_enabled_state(HomePageSelectors.SEARCH_BUTTON)
    assert home.get_displayed_state(HomePageSelectors.SEARCH_INPUT)
    assert home.get_enabled_state(HomePageSelectors.SEARCH_CLEAR_BUTTON)
    assert home.get_displayed_state(HomePageSelectors.BROWSE_BUTTON)
