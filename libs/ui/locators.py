from selenium.webdriver.common.by import By

class HomePageSelectors:
    HOME_BUTTON = (By.XPATH, "//button[@data-testid='home-button']")
    SEARCH_BUTTON = (By.XPATH, "//button[@aria-label='Search']")
    SEARCH_INPUT = (By.XPATH, "//input[@data-testid='search-input']")
    SEARCH_CLEAR_BUTTON = (By.XPATH, "//button[@data-testid='clear-button']")
    BROWSE_BUTTON = (By.XPATH, "//button[@data-testid='browse-button']")
