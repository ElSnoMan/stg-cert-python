from selenium.webdriver.remote.webdriver import WebDriver

from copart.pages.home_page import HomePage
from copart.pages.results_page import ResultsPage


class Pages:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.home = HomePage(driver)
        self.results = ResultsPage(driver)

    def search(self, query: str) -> ResultsPage:
        self.home.search(query)
        self.results.wait_for_page_load()
        return self.results
