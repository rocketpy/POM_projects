from base_page import BasePage
from selenium.webdriver.common.by import By


class LoginFormLocators:
    LOCATOR_EMAIL_FIELD = (By.ID, "")
    LOCATOR_PASSWORD_FIELD = (By.ID, "")
    LOCATOR_LOGIN_BUTTON = (By.CLASS_NAME, "")


class Loginer(BasePage):

    def input_email(self, email):
        email_field = self.find_element(LOginFormLocators.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(email)
        return email_field

      
    def input_password(self, password):
        password_field = self.find_element(LoginLocators.LOCATOR_PASSWORD_FIELD)
        password_field.send_keys(password)
        return password_field      
    
    
    def click_on_login_button(self):
        return self.find_element(LoginFormLocators.LOCATOR_LOGIN_BUTTON, time=2).click()

 
