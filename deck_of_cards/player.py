from typing import List
from deck_of_cards import deck_service
from deck_of_cards.models import Card


class Player:
    def __init__(self, deck_id, name, starting_hand_count):
        self.deck_id = deck_id
        self.name = name
        deck_service.draw_cards_to_pile(deck_id, name, starting_hand_count)

    @property
    def cards(self) -> List[Card]:
        return deck_service.get_list_of_cards_in_pile(self.deck_id, self.name)

    def draw_cards(self, count: int):
        deck_service.draw_cards_to_pile(self.deck_id, self.name, count)
