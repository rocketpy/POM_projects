import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#  pytest -s -v test_file_name.py

@pytest.fixture(scope="function")  #  in case,  scope="session" , this fixture will run once by test
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
