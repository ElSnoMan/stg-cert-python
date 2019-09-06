from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultsPage:
    def __init__(self, driver):
        self._driver = driver
        self.map = ResultsPageMap(driver)

    def change_num_of_entries_shown(self, count: int):
        """ Changes the number of entries/results shown in the table.

        Default is 20.

        :param count: 20 | 50 | 100
        """
        Select(self.map.show_entries_dropdown).select_by_value(str(count))
        self.wait_for_new_results_load()

    def wait_for_page_load(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'tbody')))

    def wait_for_new_results_load(self):
        wait = WebDriverWait(self._driver, 30)
        wait.until(lambda _: self.map.table_spinner.get_attribute('style') == 'display: block;')
        wait.until(lambda _: self.map.table_spinner.get_attribute('style') == 'display: none;')


class ResultsPageMap:
    def __init__(self, driver):
        self._driver = driver

    @property
    def show_entries_dropdown(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, 'select[name="serverSideDataTable_length"]')

    @property
    def table_spinner(self) -> WebElement:
        return self._driver.find_element(By.ID, 'serverSideDataTable_processing')

    @property
    def model_results(self) -> List[WebElement]:
        return self._driver.find_elements(By.XPATH, "//span[@data-uname='lotsearchLotmodel']")

    @property
    def damage_results(self) -> List[WebElement]:
        return self._driver.find_elements(By.XPATH, "//span[@data-uname='lotsearchLotdamagedescription']")
