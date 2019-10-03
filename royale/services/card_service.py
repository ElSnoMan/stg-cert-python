from typing import List

import requests

from royale.models.card import Card


def get_all_cards() -> List[Card]:
    response = requests.get("https://statsroyale.com/api/cards")

    if response.status_code != 200:
        raise Exception(f'/cards responded with: {response.status_code}')

    return [Card(**card) for card in response.json()]
