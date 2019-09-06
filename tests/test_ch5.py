from pprint import pprint
from typing import List, Dict

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_count_types_of_porsche_models(driver):
    # setup
    wait = WebDriverWait(driver, 10)
    driver.get('https://copart.com')

    # search 'porsche'
    driver.find_element(By.ID, 'input-search').send_keys('porsche' + Keys.ENTER)
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'tbody')))

    # change number of entries shown and wait for spinner
    spinner = driver.find_element(By.ID, "serverSideDataTable_processing")
    Select(driver.find_element(By.NAME, 'serverSideDataTable_length')).select_by_value('100')
    wait.until(lambda _: spinner.get_attribute('style') == 'display: block;')
    wait.until(lambda _: spinner.get_attribute('style') == 'display: none;')

    # challenge 5
    results: Dict[str, int] = {}
    models: List[WebElement] = driver.find_elements(By.XPATH, "//span[@data-uname='lotsearchLotmodel']")

    for model in models:
        if model.text not in results.keys():
            results[model.text] = 1
        else:
            results[model.text] += 1

    pprint(results)


def test_count_types_of_damages(copart):
    """ Using Page Object Model """
    copart.search('porsche')
    copart.results.change_num_of_entries_shown(100)

    # Left challenge-specific logic in the test
    results = {
        'REAR END': 0,
        'FRONT END': 0,
        'MINOR DENT/SCRATCHES': 0,
        'UNDERCARRIAGE': 0,
        'MISC': 0
    }

    for damage in copart.results.map.damage_results:
        if damage.text == 'REAR END':
            results['REAR END'] += 1

        elif damage.text == 'FRONT END':
            results['FRONT END'] += 1

        elif damage.text == 'MINOR DENT/SCRATCHES':
            results['MINOR DENT/SCRATCHES'] += 1

        elif damage.text == 'UNDERCARRIAGE':
            results['UNDERCARRIAGE'] += 1

        else:
            results['MISC'] += 1

    pprint(results)
