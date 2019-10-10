from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class ItemDetailsPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self.map = ItemDetailsPageMap(driver)

    def goto(self) -> 'ItemDetailsPage':
        self._driver.get('https://www.youniqueproducts.com/products/view/US-51081-01')
        return self

    def add_to_cart(self, quantity: int) -> 'ItemDetailsPage':
        self.map.quantity_input.send_keys(quantity)
        self.map.add_to_cart_button.click()
        return self

    def proceed_to_checkout(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(lambda _: self.map.proceed_to_checkout_button).click()
        wait.until(lambda _: self._driver.find_element(By.ID, 'cartview').is_displayed())


class ItemDetailsPageMap:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def add_to_cart_button(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='addToCartBtn']")

    @property
    def quantity_input(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "input[class*='pdpItemQty']")

    @property
    def proceed_to_checkout_button(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='checkout']")
