from pylenium import Pylenium
from pylenium.element import Element, Elements
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from copart.pages.filter_options_menu import FilterMenu


class ResultsPage:
    def __init__(self, py: Pylenium):
        self.py = py
        self.map = ResultsPageMap(py)
        self.filter_menu = FilterMenu(py)

    def change_num_of_entries_shown(self, count: int):
        """ Changes the number of entries/results shown in the table.

        Default is 20.

        :param count: 20 | 50 | 100
        """
        if count != 20 or 50 or 100:
            raise Exception(f'count must be 20, 50 or 100 but was {count}')

        self.map.show_entries_dropdown.select(str(count))
        self.wait_for_new_results_load()

    def filter_by(self, filter_name: str, search: str):
        self.filter_menu.filter_by(filter_name, search)
        self.wait_for_new_results_load()

    def wait_for_page_load(self):
        self.py.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'tbody')))

    def wait_for_new_results_load(self):
        self.py.wait.until(lambda _: self.map.table_spinner.get_attribute('style') == 'display: block;')
        self.py.wait.until(lambda _: self.map.table_spinner.get_attribute('style') == 'display: none;')


class ResultsPageMap:
    def __init__(self, py: Pylenium):
        self._py = py

    @property
    def show_entries_dropdown(self) -> Element:
        return self._py.get('select[name="serverSideDataTable_length"]')

    @property
    def table_spinner(self) -> Element:
        return self._py.get('#serverSideDataTable_processing')

    @property
    def model_results(self) -> Elements:
        return self._py.xpath("//span[@data-uname='lotsearchLotmodel']")

    @property
    def damage_results(self) -> Elements:
        return self._py.xpath("//span[@data-uname='lotsearchLotdamagedescription']")
