from selenium.webdriver import Chrome
import pytest
import allure
from pathlib import Path
import logging
from selenium.webdriver.chrome.options import Options

log = logging.getLogger(__name__)



@pytest.fixture(scope='module')
def chrome_driver():
    options = Options() 
    driver = Chrome(options=options)
    driver.get("https://open.spotify.com")
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(items):
    """
    Modifying the test cases before it starts
    """
    repo = "auto-spot-sel"
    for item in items:
        item.add_marker(allure.story(repo))
        _file = Path(item.nodeid.split("::")[0])
        item.add_marker(allure.parent_suite(repo))
        suite = "".join(_file.parent.parts[1])
        item.add_marker(allure.suite(suite))
        sub_suite = "".join(_file.parent.parts[2:])
        item.add_marker(allure.sub_suite(sub_suite))

