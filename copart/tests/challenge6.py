

def test_challenge_6(copart):
    # 1. go to copart.com and search 'nissan'
    copart.search(query='nissan')

    # 2. Try to filter by Model and Search
    try:
        query = 'Skyline'
        copart.results.filter_by('Model', search=query)

        model = copart.results.map.model_results[0]
        assert model.text == query

    # 3. If the query doesn't exist, catch the exception and take a screenshot
    except BaseException as error:
        copart.py.save_screenshot('test_fail.png')
        raise error
