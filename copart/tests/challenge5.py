from pprint import pprint
from selenium.webdriver.common.keys import Keys


def test_challenge_5_with_pylenium_and_page_object_model(copart):
    copart.search('porsche')
    copart.results.change_num_of_entries_shown(100)

    results = {
        'REAR END': 0,
        'FRONT END': 0,
        'MINOR DENT/SCRATCHES': 0,
        'UNDERCARRIAGE': 0,
        'MISC': 0
    }

    # count the occurrences of each damage type in the table
    for damage in copart.results.map.damage_results:
        if damage.text in results.keys():
            results[damage.text] += 1
        else:
            results['MISC'] += 1
    pprint(results)


def test_count_types_of_porsche_models_with_pylenium(py):
    # setup
    py.visit('https://copart.com')

    # search 'porsche'
    py.get('#input-search').type('porsche', Keys.ENTER)

    # change number of entries shown and wait for spinner
    py.get('[name="serverSideDataTable_length"]').select('100')
    spinner = py.get('#serverSideDataTable_processing')
    py.wait.until(lambda _: spinner.get_attribute('style') == 'display: block;')
    py.wait.until(lambda _: spinner.get_attribute('style') == 'display: none;')

    # count the number of occurrences for each Model in the table
    results = {}
    for model in py.xpath("//span[@data-uname='lotsearchLotmodel']"):
        if model.text not in results.keys():
            results[model.text] = 1
        else:
            results[model.text] += 1
    pprint(results)


# def test_count_types_of_porsche_models_with_selenium(driver):
#     # setup
#     wait = WebDriverWait(driver, 10)
#     driver.get('https://copart.com')
#
#     # search 'porsche'
#     driver.find_element(By.ID, 'input-search').send_keys('porsche' + Keys.ENTER)
#     wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'tbody')))
#
#     # change number of entries shown and wait for spinner
#     Select(driver.find_element(By.NAME, 'serverSideDataTable_length')).select_by_value('100')
#     spinner = driver.find_element(By.ID, "serverSideDataTable_processing")
#     wait.until(lambda _: spinner.get_attribute('style') == 'display: block;')
#     wait.until(lambda _: spinner.get_attribute('style') == 'display: none;')
#
#     # challenge 5
#     results: Dict[str, int] = {}
#     models: List[WebElement] = driver.find_elements(By.XPATH, "//span[@data-uname='lotsearchLotmodel']")
#
#     for model in models:
#         if model.text not in results.keys():
#             results[model.text] = 1
#         else:
#             results[model.text] += 1
#
#     pprint(results)
