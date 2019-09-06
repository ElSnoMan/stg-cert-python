from selenium.webdriver.common.by import By


def test_challenge_3(driver):
    driver.get('https://copart.com')
    popular_models = driver.find_elements(By.CSS_SELECTOR, "li[ng-repeat*='popularSearch'] > a")
    for model in popular_models:
        print(f'{model.text} - {model.get_attribute("href")}')

    assert len(popular_models) == 20
