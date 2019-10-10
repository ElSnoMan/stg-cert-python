from selenium.webdriver.remote.webdriver import WebDriver

from younique.pages.cart_page import CartPage
from younique.pages.item_details_page import ItemDetailsPage


class YouniquePages:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.item_details = ItemDetailsPage(driver)
        self.cart = CartPage(driver)
