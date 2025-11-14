from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import pytest
import allure
from pathlib import Path
import logging

log = logging.getLogger(__name__)

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")     
options.add_argument("--disable-dev-shm-usage")  

@pytest.fixture(scope='module')
def chrome_driver():
    driver = Chrome(options=options)
    driver.get("https://open.spotify.com")
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(items):
    """
    Modifying the test cases before it starts
    """
    repo = "auto-spotify-s"
    for item in items:
        item.add_marker(allure.story(repo))
        _file = Path(item.nodeid.split("::")[0])
        item.add_marker(allure.parent_suite(repo))
        suite = "".join(_file.parent.parts[1])
        item.add_marker(allure.suite(suite))
        sub_suite = "".join(_file.parent.parts[2:])
        item.add_marker(allure.sub_suite(sub_suite))

