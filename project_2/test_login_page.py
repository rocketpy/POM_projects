from login_page import Loginer


def test_login(browser):
    login_page = Loginer(browser)
    login_page.go_to_website()
    login_page.input_email("email@gmail")
    login_page.input_password("password")
    login_page.click_on_login_button()
    
    
    assert #  need add assert check status !
