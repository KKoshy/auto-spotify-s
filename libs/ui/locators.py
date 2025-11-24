from selenium.webdriver.common.by import By

class HomePageSelectors:
    HOME_BUTTON = (By.XPATH, "//button[@data-testid='home-button']")
    SEARCH_BUTTON = (By.XPATH, "//button[@aria-label='Search']")
    SEARCH_INPUT = (By.XPATH, "//input[@data-testid='search-input']")
    SEARCH_CLEAR_BUTTON = (By.XPATH, "//button[@data-testid='clear-button']")
    BROWSE_BUTTON = (By.XPATH, "//button[@data-testid='browse-button']")
    PREMIUM_BUTTON = (By.XPATH, "//button[normalize-space()='Premium']")
    SUPPORT_BUTTON = (By.XPATH, "//button[normalize-space()='Support']")
    DOWNLOAD_BUTTON = (By.XPATH, "//button[normalize-space()='Download']")
    INSTALL_APP_BUTTON = (By.XPATH, "//a[@href='/download']")
    SIGN_UP_BUTTON = (By.XPATH, "//button[@data-testid='signup-button']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-testid='login-button']")
    YOUR_LIBRARY_HEADER = (By.XPATH, "//div/h1[normalize-space()='Your Library']")
    CREATE_PL_FL = (By.XPATH, "//button[@aria-label='Create playlist or folder']")
    CREATE_PLAYLIST_OPTION = (By.XPATH, "//button[contains(., 'Create a new playlist')]")
    LEGAL_LINK = (By.XPATH, "//a[contains(., 'Legal')]")
    SAFETY_AND_PRIVACY_LINK = (By.XPATH, "//a[contains(., 'Safety & Privacy Center')]")
    PRIVACY_POLICY_LINK = (By.XPATH, "//a[contains(., 'Privacy Policy')]")
    COOKIES_LINK = (By.XPATH, "//a[contains(., 'Cookies')][@data-encore-id='textLink']")
    ABOUT_ADS_LINK = (By.XPATH, "//a[contains(., 'About Ads')]")
    ACCESSIBILITY_LINK = (By.XPATH, "//a[contains(., 'Accessibility')]")


