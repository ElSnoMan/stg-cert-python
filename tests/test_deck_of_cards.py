import pytest
import requests

from deck_of_cards import cards

cards_api_url = 'https://deckofcardsapi.com/api/deck'


def test_create_new_shuffled_deck():
    deck = cards.new_deck()
    assert deck['remaining'] == 52
    assert deck['shuffled']


def test_create_new_deck():
    deck = cards.new_deck(shuffled=False)
    assert deck['remaining'] == 52
    assert deck['shuffled'] == False











def new_deck(shuffled=True):
    if shuffled:
        response = requests.get(f'{cards_api_url}/new/shuffle/')
    else:
        response = requests.get(f'{cards_api_url}/new/')

    if response.ok:
        return response.json()

    raise ValueError('Error raised when trying to create deck.')
#
#
# def new_player(deck_id, player_name):
#     response = requests.get(f'{cards_api_url}/{deck_id}/pile/{player_name}/add/')
#     if response.ok:
#         return response.json()
#     raise ValueError('Error raised when creating a new player pile.')
#
#
# def test_create_new_shuffled_deck():
#     deck = new_deck()
#     assert deck['remaining'] == 52
#     assert deck['deck_id'] is not None
#     assert deck['shuffled']
#     assert deck['success']
#
#
# def test_create_player():
#     deck = new_deck()
#     player = new_player(deck['deck_id'], 'player 1')
#     assert player is not None
#
#
# def test_player_can_draw_card():
#     pass
#
#
# def test_highest_card_wins():
#     pass
