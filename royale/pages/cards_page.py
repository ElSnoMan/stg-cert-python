from pylenium import Pylenium
from pylenium.element import Element


class CardsPage:
    def __init__(self, py: Pylenium):
        self.py = py
        self.map = CardsPageMap(py)

    def goto(self):
        self.map.cards_link().click()

    def get_card_by_name(self, card_name: str) -> Element:
        if ' ' in card_name:
            card_name = card_name.replace(' ', '+')
        return self.map.card(card_name)


class CardsPageMap:
    def __init__(self, py: Pylenium):
        self._py = py

    def cards_link(self) -> Element:
        return self._py.get("a[href='/cards']")

    def card(self, card_name: str) -> Element:
        """ Gets the card on the page given the card name.

        Args:
            card_name: The card name

        Returns:
            The card as a WebElement
        """
        return self._py.get(f"a[href*='{card_name}']")
