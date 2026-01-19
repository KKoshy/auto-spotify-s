import logging
import pytest
import os
from libs.ui.login_page import LoginPage
from libs.ui.home_page import HomePage
from libs.ui.locators import NavigationBarSelectors, LoginPageSelectors

log = logging.getLogger(__name__)

@pytest.fixture(scope='class')
def chrome(chrome_driver):
    yield chrome_driver

@pytest.mark.positive
class TestLogin:
    @pytest.mark.dependency(name='login')
    def test_login(self, chrome):
        log.info("Validating login")
        home = HomePage(chrome)
        home.click(NavigationBarSelectors.LOGIN_BUTTON)
        login = LoginPage(chrome)
        login.wait_for_url().login(username=os.getenv('SPOTIFY_USER'), password=os.getenv('SPOTIFY_PASSWORD'))
        by, xpath = NavigationBarSelectors.USER_PROFILE_BUTTON
        assert home.wait_for_url().get_enabled_state((by, xpath.format(user_name='A'))), "Login failed"
        log.info("Login succeeded")

    @pytest.mark.dependency(depends=['login'])
    def test_user_nav_bar(self, chrome):
        log.info("Validating Navigation bar elements post Login")
        home = HomePage(chrome)
        home.save_screenshot()
        assert home.get_enabled_state(NavigationBarSelectors.EXPLORE_PREMIUM_BUTTON)
        assert home.get_enabled_state(NavigationBarSelectors.INSTALL_APP_BUTTON)
        assert home.get_enabled_state(NavigationBarSelectors.WHATS_NEW_BUTTON)
        assert home.get_enabled_state(NavigationBarSelectors.FRIEND_ACTIVITY_BUTTON)

    @pytest.mark.dependency(depends=['login'])
    def test_logout(self, chrome):
        log.info("Validating logout")
        home = HomePage(chrome)
        home.nav_bar.logout()
        assert home.wait_for_url().get_enabled_state(NavigationBarSelectors.LOGIN_BUTTON)


@pytest.mark.negative
class TestNegativeLogin:

    @pytest.mark.dependency(name='no_user')
    def test_no_user(self, chrome):
        log.info("Validating login with no username")
        home = HomePage(chrome)
        home.click(NavigationBarSelectors.LOGIN_BUTTON)
        login = LoginPage(chrome).wait_for_url()
        login.click(LoginPageSelectors.CONTINUE_LOGIN_BUTTON)
        login.save_screenshot()
        login.should_have_username_error()

    @pytest.mark.dependency(name='no_account', depends=['no_user'])
    def test_user_with_no_account(self, chrome):
        log.info("Validating user with no spotify account")
        login = LoginPage(chrome)
        login.type(LoginPageSelectors.USERNAME, "asoidnfasodn")
        login.click(LoginPageSelectors.CONTINUE_LOGIN_BUTTON)
        login.should_have_no_account_error()

    @pytest.mark.dependency(name='no_password', depends=['no_account'])
    def test_user_with_no_password(self, chrome):
        log.info("Validating user with no password")
        login = LoginPage(chrome)
        login.login(username=os.getenv('SPOTIFY_USER'), password="")
        login.should_have_no_password_error()

    @pytest.mark.dependency(depends=['no_password'])
    def test_user_with_incorrect_creds(self, chrome):
        log.info("Validating user with wrong password")
        login = LoginPage(chrome)
        login.type(LoginPageSelectors.PASSWORD, os.getenv('SPOTIFY_PASSWORD'))
        login.click(LoginPageSelectors.CONTINUE_LOGIN_BUTTON)
        login.should_have_incorrect_creds_error()
