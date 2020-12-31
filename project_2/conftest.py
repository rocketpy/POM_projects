import pytest
from selenium import webdriver


@pytest.fixture(scope="session")  #  one time per session
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    yield driver
    driver.quit()
