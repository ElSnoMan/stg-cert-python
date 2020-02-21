from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class FilterMenu:
    def __init__(self, driver):
        self._driver = driver

    def filter_by(self, filter_name: str, search: str):
        """ Filter the table results using the Filter Options menu.

        :param filter_name: Examples: 'Model' | 'Body Style'
        :param search: The search term to use. The first option after the search is selected.
        """
        filter = FilterComponent(self._driver, filter_name)
        if filter.is_collapsed:
            filter.toggle.click()

        filter.search_field.send_keys(search)
        filter.option(search).click()


class FilterComponent:
    def __init__(self, driver, name):
        self._driver = driver
        self.name = name

    @property
    def current(self) -> WebElement:
        """ The Parent element that holds the elements of this current Filter. """
        return self._driver.find_element(
            By.XPATH, f"//a[@data-uname='{self.name}Filter']/ancestor::li")

    @property
    def toggle(self) -> WebElement:
        """ The Toggle element to open or collapse the Filter. """
        return self.current.find_element(By.CSS_SELECTOR, "a[data-toggle='collapse']")

    @property
    def is_collapsed(self) -> bool:
        """ Checks if the Filter is collapsed or not. """
        collapsed = self.toggle.get_attribute('aria-expanded')
        return True if collapsed is None or 'false' else False

    @property
    def clear_button(self) -> WebElement:
        """ The Clear button that resets the current filter and refreshes the table. """
        return self.current.find_element(By.CSS_SELECTOR, "[data-uname='watchlistClear']")

    @property
    def search_field(self) -> WebElement:
        """ The Input element to enter a query. """
        return self.current.find_element(By.CSS_SELECTOR, 'input[placeholder="Search"]')

    def option(self, name: str) -> WebElement:
        """ Gets a single Filter Option checkbox by its name/value. """
        return self.current.find_element(By.CSS_SELECTOR, f"input[type='checkbox'][value='{name}']")
