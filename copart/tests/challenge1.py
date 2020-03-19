
def test_challenge_1(py):
    py.visit('https://google.com')
    assert 'Google' in py.title


# def test_challenge_1_with_selenium(driver):
#     driver.get('https://google.com')
#     assert 'Google' in driver.title
