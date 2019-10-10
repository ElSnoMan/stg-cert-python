from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from younique.models.cart_summary import CartSummary
from younique.models.item_row import ItemRow


class CartPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self.map = CartPageMap(driver)

    def goto(self):
        self.map.view_cart_icon.click()
        self.wait_for_page_load()

    def get_item_rows(self) -> List[ItemRow]:
        item_rows = []
        for row in self.map.item_rows:
            item_rows.append(ItemRow(
                sku=row.find_element(By.XPATH, "//span[text()='SKU']/following-sibling::span").text,
                product=row.find_element(By.CSS_SELECTOR, '.itemName').text,
                unit_price=float(row.find_element(
                    By.XPATH, "//span[text()='Unit Price']/following-sibling::span").text.replace('$', '')),
                quantity=int(row.find_element(
                    By.CSS_SELECTOR, "[data-testid='quantityInput']").get_attribute('value')),
                total=float(row.find_element(
                    By.CSS_SELECTOR, "[class*='receiptLineTotal']").text.replace('$', ''))
            ))
        return item_rows

    def get_cart_summary(self) -> CartSummary:
        return CartSummary(
            total_items=int(self._driver.find_element(
                By.XPATH, "//td[text()='Total Items:']/following-sibling::td").text),
            subtotal=float(self._driver.find_element(
                By.XPATH, "//td[text()='Subtotal:']/following-sibling::td").text.replace('$', '')),
            tax=self._driver.find_element(
                By.XPATH, "//td[contains(text(), 'Tax')]/following-sibling::td").text,
            shipping=float(self._driver.find_element(
                By.CSS_SELECTOR, "[data-testid='shippingDisplay']").text.replace('$', '')),
            total_balance_due=float(self._driver.find_element(By.ID, 'carttotal').text.split()[0].replace('$', ''))
        )

    def wait_for_page_load(self):
        WebDriverWait(self._driver, 10).until(lambda _: self.map.cart_container.is_displayed())


class CartPageMap:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def view_cart_icon(self) -> WebElement:
        return self._driver.find_element(By.ID, 'viewCart')

    @property
    def cart_container(self) -> WebElement:
        return self._driver.find_element(By.ID, 'cartview')

    @property
    def item_rows(self) -> List[WebElement]:
        return self._driver.find_elements(By.CSS_SELECTOR, '.itemRow')
