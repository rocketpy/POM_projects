import pytest
from pages.result_page import ResultPage
from pages.base_page import SearchPage
from selenium.webdriver import Chrome


#  to run test: pipenv run python -m pytest
#  without venv: python -m pytest
#  python -v pytest  # verbose result

@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    
    
def test_basic_page(browser):
    WORDS = 'cars'  # words for input 
    search_page = SearchPage(browser)
    search_page.load()
    search_page.search(WORDS)
    result_page = ResultPage(browser)
    
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(WORDS) > 0
    assert result_page.search_input_value() == WORDS
    
