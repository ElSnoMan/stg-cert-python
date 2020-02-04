

def test_challenge_6(copart):
    copart.search('nissan')
    copart.results.filter_by('Model', search='300zx')
    model = copart.results.map.model_results[0]
    assert model.text == '300ZX'
