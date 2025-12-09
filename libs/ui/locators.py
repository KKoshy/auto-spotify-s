from selenium.webdriver.common.by import By

class LoginPageSelectors:
    USERNAME = (By.XPATH, "//input[@data-testid='login-username']")
    CONTINUE_LOGIN_BUTTON = (By.XPATH, "//button[@data-testid='login-button']")
    LOGIN_WITH_PASSWORD = (By.XPATH, "//button[contains(., 'Log in with a password')]")
    PASSWORD = (By.XPATH, "//input[@data-testid='login-password']")
    LOGIN_ALERT = (By.XPATH, "//div[@data-encore-id='banner'][contains(., 'Oops! Something went wrong, please try again or check out our help area')]")

class NavigationBarSelectors:
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
    USER_WIDGET_BUTTON = (By.XPATH, "//button[@data-testid='user-widget-link']")
    USER_PROFILE_BUTTON = (By.XPATH, "//button[@data-testid='user-widget-link']/span[contains(text(),'{user_name}')]")
    EXPLORE_PREMIUM_BUTTON = (By.XPATH, "//button[normalize-space()='Explore Premium']")
    WHATS_NEW_BUTTON = (By.XPATH, "//button[@data-testid='whats-new-feed-button']")
    FRIEND_ACTIVITY_BUTTON = (By.XPATH, "//button[@data-testid='friend-activity-button']")
    LOGOUT_BUTTON = (By.XPATH, "//button[@data-testid='user-widget-dropdown-logout']")

class HomePageSelectors:
    LEGAL_LINK = (By.XPATH, "//a[contains(., 'Legal')]")
    SAFETY_AND_PRIVACY_LINK = (By.XPATH, "//a[contains(., 'Safety & Privacy Center')]")
    PRIVACY_POLICY_LINK = (By.XPATH, "//a[contains(., 'Privacy Policy')]")
    COOKIES_LINK = (By.XPATH, "//a[contains(., 'Cookies')][@data-encore-id='textLink']")
    ABOUT_ADS_LINK = (By.XPATH, "//a[contains(., 'About Ads')]")
    ACCESSIBILITY_LINK = (By.XPATH, "//a[contains(., 'Accessibility')]")

class LeftSideBarSelectors:
    YOUR_LIBRARY_HEADER = (By.XPATH, "//div/h1[normalize-space()='Your Library']")
    CREATE_PL_FL = (By.XPATH, "//button[@aria-label='Create playlist or folder'] | //button[@aria-label='Create']")
    CREATE_PLAYLIST_OPTION = (By.XPATH, "//button[contains(., 'Create a new playlist')] | //button[contains(.,'Create a playlist')]")

class PlaylistDetailsPageSelectors:
    MORE_BUTTON = (By.XPATH, "//button[@data-testid='more-button']")
    EDIT_DETAILS = (By.XPATH, "//button[contains(., 'Edit details')]")
    PL_DETAILS_MODAL = (By.XPATH, "//div[@data-testid='playlist-edit-details-modal']")
    PL_NAME_INPUT = (By.XPATH, "//input[@data-testid='playlist-edit-details-name-input']")
    PL_DESC_INPUT = (By.XPATH, "//textarea[@data-testid='playlist-edit-details-description-input']")
    SAVE_BUTTON = (By.XPATH, "//button[@data-testid='playlist-edit-details-save-button']")
    PL_TITLE = (By.XPATH, "//span[@data-testid='entityTitle']")
    PL_DESCRIPTION = (By.XPATH, "//span/div[text()='{description}']")
    SEARCH_BAR = (By.XPATH, "//input[@placeholder='Search for songs or episodes']")
    
