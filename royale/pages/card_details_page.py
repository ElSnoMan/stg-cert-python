from pylenium import Pylenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from royale.models.card import Card


class CardDetailsPage:
    def __init__(self, py: Pylenium):
        self.py = py
        self.map = CardDetailsPageMap(py)

    def get_base_card(self) -> Card:
        card_deets = self.map.card_deets.text.split(', ')
        card_type = card_deets[0]  # "Troop"
        card_arena = int(card_deets[1].split()[-1])  # "Arena 8"
        card_name = self.map.card_name.text
        card_rarity = self.map.card_rarity.text

        return Card(**{
            'id': 0,
            'cost': 0,
            'icon': None,
            'name': card_name,
            'rarity': card_rarity,
            'type': card_type,
            'arena': card_arena
        })

    def wait_for_page_load(self):
        self.py.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Statistics']")))


class CardDetailsPageMap:
    def __init__(self, py: Pylenium):
        self._py = py

    @property
    def card_name(self):
        return self._py.get("[class*='cardName']")

    @property
    def card_deets(self):
        return self._py.get("[class='card__rarity']")

    @property
    def card_rarity(self):
        return self._py.get("[class*='card__count']")
