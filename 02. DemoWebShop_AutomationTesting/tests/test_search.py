import pytest

from pages.search_result_page import SearchResultsPage
from pages.home_page import HomePage

@pytest.mark.regression
def test_search_product(driver):

    driver.get("https://demowebshop.tricentis.com/")

    home_page = HomePage(driver)
    home_page.search("computer")

    search_results = SearchResultsPage(driver)

    assert search_results.get_product_count() > 0

@pytest.mark.regression
def test_search_no_results(driver):

    driver.get("https://demowebshop.tricentis.com/")

    home_page = HomePage(driver)
    home_page.search("xyzabc123")

    search_results = SearchResultsPage(driver)

    assert search_results.is_no_results_displayed()

