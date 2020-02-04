from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class FilterMenu:
    def __init__(self, driver):
        self._driver = driver
        self.map = FilterMenuMap(driver)

    def filter_by(self, filter_name: str, search=''):
        filter_name += 'Filter'  # 'Model' => 'ModelFilter', 'Body Style' => 'Body StyleFilter'
        filter = self.map.filter(filter_name)
        attr = filter.get_attribute('class')
        if 'collapsed' in attr:
            filter.click()
        filter.find_element(By.CSS_SELECTOR, "[placeholder='Search']").send_keys(search)
        filter.find_element(By.CSS_SELECTOR, f"[type='checkbox'][value='{search}']").click()


class FilterMenuMap:
    def __init__(self, driver):
        self._driver = driver

    @property
    def filters(self) -> List[WebElement]:
        return self._driver.find_elements(By.CSS_SELECTOR, "[ng-repeat*='filter in filters']")

    def filter(self, filter_name: str) -> WebElement:
        return self._driver.find_element(
            By.CSS_SELECTOR, f"[ng-repeat*='filter in filters'] [data-uname='{filter_name}']")
