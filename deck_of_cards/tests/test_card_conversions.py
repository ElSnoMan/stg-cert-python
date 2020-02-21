from deck_of_cards import cards


def test_convert_code_to_face_value():
    card_code = '7S'
    face_value = cards.get_face_value(card_code)
    assert face_value == '7♠'


def test_convert_code_to_numeric_value():
    card_code = 'KH'
    numeric_value = cards.get_numeric_value(card_code)
    assert numeric_value == 13
