
def test_challenge_3(py):
    py.visit('https://copart.com')
    popular_models = py.find("li[ng-repeat*='popularSearch'] > a")
    for model in popular_models:
        print(f'{model.text} - {model.get_attribute("href")}')
    assert popular_models.length == 20


# def test_challenge_3_with_selenium(driver):
#     driver.get('https://copart.com')
#     popular_models = driver.find_elements(By.CSS_SELECTOR, "li[ng-repeat*='popularSearch'] > a")
#     for model in popular_models:
#         print(f'{model.text} - {model.get_attribute("href")}')
#     assert len(popular_models) == 20
