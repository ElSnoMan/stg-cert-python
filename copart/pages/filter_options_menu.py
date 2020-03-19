from pylenium import Pylenium
from pylenium.element import Element


class FilterMenu:
    def __init__(self, py: Pylenium):
        self._py = py

    def filter_by(self, filter_name: str, search: str):
        """ Filter the table results using the Filter Options menu.

        :param filter_name: Examples: 'Model' | 'Body Style'
        :param search: The search term to use. The first option after the search is selected.
        """
        filter = FilterComponent(self._py, filter_name)
        if filter.is_collapsed:
            filter.toggle.click()

        filter.search_field.send_keys(search)
        filter.option(search).click()


class FilterComponent:
    def __init__(self, py: Pylenium, name):
        self._py = py
        self.name = name

    @property
    def current(self) -> Element:
        """ The Parent element that holds the elements of this current Filter. """
        return self._py.xpath(f"//a[@data-uname='{self.name}Filter']/ancestor::li")

    @property
    def toggle(self) -> Element:
        """ The Toggle element to open or collapse the Filter. """
        return self.current.get("a[data-toggle='collapse']")

    @property
    def is_collapsed(self) -> bool:
        """ Checks if the Filter is collapsed or not. """
        collapsed = self.toggle.get_attribute('aria-expanded')
        return True if collapsed is None or 'false' else False

    @property
    def clear_button(self) -> Element:
        """ The Clear button that resets the current filter and refreshes the table. """
        return self.current.get("[data-uname='watchlistClear']")

    @property
    def search_field(self) -> Element:
        """ The Input element to enter a query. """
        return self.current.get('input[placeholder="Search"]')

    def option(self, name: str) -> Element:
        """ Gets a single Filter Option checkbox by its name/value. """
        return self.current.get(f"input[type='checkbox'][value='{name}']")
