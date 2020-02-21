from selenium.webdriver.common.by import By


def test_carlos_is_on_leadership_page(driver, hover):
    driver.get('https://qap.dev')
    hover(driver.find_element(By.CSS_SELECTOR, "a[href='/about']"))
    driver.find_element(By.CSS_SELECTOR, "a[href='/leadership'][class^='Header-nav']").click()
    assert driver.find_element(By.XPATH, "//*[contains(text(), 'Carlos Kidman')]")
