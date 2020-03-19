from pylenium import Pylenium
from royale.pages.card_details_page import CardDetailsPage
from royale.pages.cards_page import CardsPage


class RoyalePages:
    def __init__(self, py: Pylenium):
        self.py = py
        self.cards = CardsPage(py)
        self.card_details = CardDetailsPage(py)
