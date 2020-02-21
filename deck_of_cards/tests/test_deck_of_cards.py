import pytest
from deck_of_cards import deck_service, cards
from deck_of_cards.player import Player


def test_create_new_shuffled_deck():
    deck = deck_service.new_deck()
    assert deck.remaining == 52
    assert deck.shuffled
    assert deck.success


def test_draw_two_cards_from_deck(deck):
    draw = deck_service.draw_cards_from_deck(deck.id, 2)
    assert draw.success
    assert draw.remaining == 50
    assert len(draw.cards) == 2


def test_draw_cards_to_pile(deck):
    player = deck_service.draw_cards_to_pile(deck.id, 'player1', 7)
    assert player['piles']['player1']['remaining'] == 7


def test_list_cards_in_pile(deck):
    deck_service.draw_cards_to_pile(deck.id, 'player1', 7)
    cards_ = deck_service.get_list_of_cards_in_pile(deck.id, 'player1')
    assert len(cards_) == 7


def test_new_player_draws_cards(deck):
    player = Player(deck.id, name='Carlos', starting_hand_count=1)
    first_card = player.cards[0]

    player.draw_cards(1)
    second_card = player.cards[1]

    assert first_card != second_card


# Testability Examples

@pytest.mark.skip(reason='example')
def test_convert_card_to_score(player):
    card = player.cards[0]
    assert cards.get_numeric_value(card) == 7


def test_convert_card_code_to_score():
    assert cards.get_numeric_value('7S') == 7
    assert cards.get_numeric_value('AH') == 14
    assert cards.get_numeric_value('JC') == 11
