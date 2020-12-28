from selenium.webdriver.common.by import By


class DResultPage:
    LINK_DIVS = (By.CSS_SELECTOR, '#')
    SEARCH_INPUT = (By.ID, '')
    
    @classmethod
    def words_results(cls, words):
        xpath = f"//div[@id='links']//*[contains(text(), '{words}')]"
        return (By.XPATH, xpath)
      
      
    def __init__(self, browser):
        self.browser = browser
        
        
    def link_div_count(self):
        link_divs = self.browser.find_elements(*self.LINK_DIVS)
        return len(link_divs)
      
      
    def phrase_result_count(self, phrase):
        words_results = self.browser.find_elements(*self.PHRASE_RESULTS(phrase))
        return len(words_results)
      
      
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')
