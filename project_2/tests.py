from MainPage import Searcher


def test_search(browser):
    main_page = Searcher(browser)
    main_page.go_to_website()
    main_page.enter_word("Cars")
    main_page.click_on_the_search_button()
    elems = main_page.check_navigation_bar()
    
    assert "Images" and "Videos" in elems
    
