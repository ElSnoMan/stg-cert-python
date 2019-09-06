from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class HomePage:
    def __init__(self, driver):
        self.map = HomePageMap(driver)

    def search(self, search_term: str):
        self.map.search_field.send_keys(search_term + Keys.ENTER)


class HomePageMap:
    def __init__(self, driver):
        self._driver = driver

    @property
    def search_field(self) -> WebElement:
        return self._driver.find_element(By.ID, 'input-search')
