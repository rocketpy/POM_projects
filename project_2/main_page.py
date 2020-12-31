from base_page import BasePage
from selenium.webdriver.common.by import By


class SeacrhLocators:
    LOCATOR_SEARCH_FIELD = (By.ID, "")
    LOCATOR_SEARCH_BUTTON = (By.CLASS_NAME, "")
    LOCATOR_NAVIGATION_BAR = (By.CSS_SELECTOR, "")


class Searcher(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(SeacrhLocators.LOCATOR_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    
    def click_on_the_search_button(self):
        return self.find_element(SeacrhLocators.LOCATOR_SEARCH_BUTTON, time=2).click()

    
    def check_navigation_bar(self):
        all_list = self.find_elements(SeacrhLocators.LOCATOR_NAVIGATION_BAR, time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu    
    
