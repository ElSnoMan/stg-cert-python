import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

from copart.pages.pages import Pages
from younique.pages.pages import YouniquePages


@pytest.fixture
def copart():
    driver = webdriver.Chrome()
    pages = Pages(driver)
    driver.get('https://copart.com')
    yield pages
    driver.quit()


@pytest.fixture
def royale():
    driver = webdriver.Chrome()
    driver.get('https://statsroyale.com')
    pages = Pages(driver)
    yield pages
    driver.quit()


@pytest.fixture
def younique():
    driver = webdriver.Chrome()
    pages = YouniquePages(driver)
    yield pages
    driver.quit()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def hover(driver):
    def _hover(element):
        action = ActionChains(driver)
        action.move_to_element(element).perform()
    return _hover
