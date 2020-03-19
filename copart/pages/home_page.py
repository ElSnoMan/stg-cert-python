from pylenium import Pylenium
from pylenium.element import Element
from selenium.webdriver.common.keys import Keys


class HomePage:
    def __init__(self, py: Pylenium):
        self.py = py
        self.map = HomePageMap(py)

    def search(self, search_term: str):
        self.map.search_field.type(search_term + Keys.ENTER)


class HomePageMap:
    def __init__(self, py: Pylenium):
        self._py = py

    @property
    def search_field(self) -> Element:
        return self._py.get('#input-search')
