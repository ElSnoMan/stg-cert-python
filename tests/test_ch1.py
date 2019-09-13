

def test_challenge_1(driver):
    driver.get('https://google.com')
    assert 'Google' in driver.title
