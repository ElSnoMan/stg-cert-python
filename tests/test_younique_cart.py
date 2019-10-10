""" Younique Cart Challenge

User Story:
------------
As a user, I want to see an overview of the items in my cart and the different totals like
Unit Price, Quantity, Overall Total, etc. before completing my purchase.

Steps:
--------
1. Go to https://www.youniqueproducts.com/products/view/US-51081-01
2. Add the item to the Cart
3. Go to the Cart
4. Validate the Cart Overview
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_younique_cart_overview_scripted(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('https://www.youniqueproducts.com/products/view/US-51081-01')
    driver.find_element(By.CSS_SELECTOR, "[class*='addToCartBtn']").click()
    wait.until(lambda _: driver.find_element(By.CSS_SELECTOR, "[class*='checkout']")).click()
    wait.until(lambda _: driver.find_element(By.ID, 'cartview').is_displayed())

    # Gather Item Row totals
    unit_price_element = driver.find_element(By.XPATH, "//span[text()='Unit Price']/following-sibling::span")
    unit_price = float(unit_price_element.text.replace('$', ''))

    quantity_element = driver.find_element(By.CSS_SELECTOR, "input[data-testid='quantityInput']")
    quantity = int(quantity_element.get_attribute('value'))

    item_row_total_element = driver.find_element(By.CSS_SELECTOR, "[class*='receiptLineTotal']")
    item_row_total = float(item_row_total_element.text.replace('$', ''))

    # Gather Cart Summary totals
    total_items_element = driver.find_element(By.XPATH, "//td[text()='Total Items:']/following-sibling::td")
    total_items = int(total_items_element.text)

    subtotal_element = driver.find_element(By.XPATH, "//td[text()='Subtotal:']/following-sibling::td")
    subtotal = float(subtotal_element.text.replace('$', ''))

    tax_element = driver.find_element(By.XPATH, "//td[contains(text(), 'Tax')]/following-sibling::td")
    tax = tax_element.text

    shipping_element = driver.find_element(By.CSS_SELECTOR, "[data-testid='shippingDisplay']")
    shipping = float(shipping_element.text.replace('$', ''))

    total_balance_element = driver.find_element(By.ID, 'carttotal')
    total_balance_due = float(total_balance_element.text.split()[0].replace('$', ''))

    # Validate
    assert unit_price == 12.00
    assert quantity == 1
    assert item_row_total == 12.00

    assert total_items == 1
    assert subtotal == 12.00
    assert tax == 'To be determined'
    assert shipping == 5.50
    assert total_balance_due == 17.50


def test_younique_cart_overview(younique):
    younique.item_details\
        .goto()\
        .add_to_cart(quantity=1)\
        .proceed_to_checkout()

    items = younique.cart.get_item_rows()
    item = items[0]

    assert item.unit_price == 12.00
    assert item.quantity == 1
    assert item.total == item.unit_price * item.quantity

    summary = younique.cart.get_cart_summary()
    assert summary.total_items == sum(item.quantity for item in items)
    assert summary.subtotal == sum(item.total for item in items)
    assert summary.tax == 'To be determined'
    assert summary.shipping == 5.50
    assert summary.total_balance_due == summary.subtotal + summary.shipping
