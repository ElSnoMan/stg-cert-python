from pydantic import BaseModel

face_card_values = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    # 'a': 1  # ACE can be 1 or 14
}

card_suits = {
    'S': '♠',
    'H': '♥',
    'D': '♦',
    'C': '♣'
}


class Card(BaseModel):
    code: str  # two-character representation like '7H' or 'AS'
    image: str
    suit: str  # example: 'SPADES'
    value: str  # example: '3' or 'ACE'

    @property
    def face_value(self) -> str:
        return get_face_value(self.code)

    @property
    def numeric_value(self) -> int:
        return get_numeric_value(self.code)

    class Config:
        extra = 'ignore'


def get_numeric_value(card_code: str) -> int:
    """ Convert a card code to its numeric value.

    Example: '7S' => 7, 'KH' => 13

    :param card_code: The card code to convert.
    """
    value = card_code[0]
    if value.isdigit():
        return int(value)

    return face_card_values[value]


def get_face_value(card_code) -> str:
    """ Convert a card code to its face value.

    Example: '7S' => '7♠', 'KH' => 'K♥'
    :param card_code: the card code to convert.
    """
    value = card_code[0]
    suit = card_code[1]
    return f'{value}{card_suits[suit]}'
