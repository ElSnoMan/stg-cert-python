from pylenium import Pylenium
from copart.pages.home_page import HomePage
from copart.pages.results_page import ResultsPage


class CopartPages:
    def __init__(self, py: Pylenium):
        self.py = py
        self.home = HomePage(py)
        self.results = ResultsPage(py)

    def search(self, query: str) -> ResultsPage:
        self.home.search(query)
        self.results.wait_for_page_load()
        return self.results
