import logging
from libs.ui.base_page import BasePage
from libs.ui.locators import LoginPageSelectors
from selenium.webdriver.support import expected_conditions as EC
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_fixed,
)



log = logging.getLogger(__name__)

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.url = r"^https://accounts.spotify.com/.*/login"
        super().__init__(driver)

    def wait_for_url(self) -> "LoginPage":
        """
        Wait for the page URL

        :return: self for method chaining
        """
        self.wait.until(EC.url_matches(self.url))
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        """
        Login with username and password

        :param username: username/mail of the user
        :param password: password of the user
        :return: self for method chaining
        """
        log.info(f"Logging in as {username}")
        self.save_screenshot()
        self._login_user(username)
        self.save_screenshot()
        self.click(LoginPageSelectors.LOGIN_WITH_PASSWORD)
        self.type(LoginPageSelectors.PASSWORD, password)
        self.click(LoginPageSelectors.CONTINUE_LOGIN_BUTTON)
        self.save_screenshot()
        return self

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_fixed(30),
        retry=retry_if_exception_type(SystemError),
        before_sleep=before_sleep_log(log, logging.INFO),
        reraise=True,
    )
    def _login_user(self, username: str):
        self.type(LoginPageSelectors.USERNAME, username)
        self.click(LoginPageSelectors.CONTINUE_LOGIN_BUTTON)
        if self.get_displayed_state(LoginPageSelectors.LOGIN_ALERT):
            self.save_screenshot()
            raise SystemError("Unexpected error")

