from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SearchPage:
    URL = 'https://www...'
    SEARCH_INPUT = (By.ID, 'search_form')
    
    def __init__(self, browser):
        self.browser = browser
        
        
    def load(self):
        self.browser.get(self.URL)
        
        
    def search(self, word):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(word + Keys.RETURN)
