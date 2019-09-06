import pytest
from selenium import webdriver

from copart.pages.pages import Pages


@pytest.fixture
def copart():
    driver = webdriver.Chrome()
    pages = Pages(driver)
    driver.get('https://copart.com')
    yield pages
    driver.quit()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
