
def test_carlos_is_on_leadership_page(py):
    py.visit('https://qap.dev')
    py.get('a[href="/about"]').hover()
    py.get("a[href='/leadership'][class^='Header-nav']").click()
    assert py.wait.until(lambda _: py.xpath("//*[text()='Carlos Kidman']").is_displayed())


# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()
#
# def test_carlos_is_on_leadership_page_with_selenium(driver):
#     driver.get('https://qap.dev')
#
#     # hover About link
#     about_link = driver.find_element(By.CSS_SELECTOR, "a[href='/about']")
#     actions = ActionChains(driver)
#     actions.move_to_element(about_link).perform()
#
#     # click Leadership link in About menu
#     driver.find_element(By.CSS_SELECTOR, "a[href='/leadership'][class^='Header-nav']").click()
#
#     # check if 'Carlos Kidman' is on the page
#     assert driver.find_element(By.XPATH, "//*[contains(text(), 'Carlos Kidman')]")
