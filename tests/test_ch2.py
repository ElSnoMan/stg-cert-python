from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_challenge_2(driver):
    driver.get('https://copart.com')
    driver.find_element(By.ID, 'input-search').send_keys('exotics' + Keys.ENTER)
    table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'tbody')))
    assert 'PORSCHE' in table.text
