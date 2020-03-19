import requests
from selenium.webdriver.common.keys import Keys



def test_challenge_2(py):
    py.visit('https://copart.com')
    py.get('#input-search').type('exotics' + Keys.ENTER)
    assert 'PORSCHE' in py.get('tbody').text
    response = py.request.post('', {'name': 'foo'}).json()
    assert response['name'] == 'foo'


# def test_challenge_2_with_selenium(driver):
#     driver.get('https://copart.com')
#     driver.find_element(By.ID, 'input-search').send_keys('exotics', Keys.ENTER)
#     table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(By.TAG_NAME, 'tbody'))
#     assert 'PORSCHE' in table.text
