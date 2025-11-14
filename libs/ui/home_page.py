from libs.ui.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        self.url = "https://open.spotify.com"
        self.driver = driver
        super().__init__(driver)

    
