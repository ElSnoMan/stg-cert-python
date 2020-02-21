import pytest

from deck_of_cards import deck_service
from deck_of_cards.player import Player


@pytest.fixture
def deck():
    return deck_service.new_deck()


@pytest.fixture
def player(deck):
    return Player(deck.id, 'Carlos', starting_hand_count=1)
