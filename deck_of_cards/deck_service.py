from typing import List
import requests

from deck_of_cards.cards import Card
from deck_of_cards.models import Deck, CardDraw


cards_api_url = 'https://deckofcardsapi.com/api/deck'


def new_deck(shuffled=True) -> Deck:
    """ Open a brand new deck.

    :param shuffled: Should the deck be shuffled?
    """
    if shuffled:
        response = requests.get(f'{cards_api_url}/new/shuffle/')
    else:
        response = requests.get(f'{cards_api_url}/new/')

    if response.ok:
        return Deck(**response.json())

    raise ValueError(f'Error raised when trying to create deck. {response.status_code}: {response.content}')


def draw_cards_from_deck(deck_id: str, count: int) -> CardDraw:
    """ Draw x cards from a deck.

    :param deck_id: The deck to draw from.
    :param count: The number of cards to draw.
    """
    response = requests.get(f'{cards_api_url}/{deck_id}/draw/?count={count}')
    if response.ok:
        return CardDraw(**response.json())
    raise ValueError(f'Error raised when drawing cards from a deck. {response.status_code}: {response.content}')


def add_cards_to_pile(deck_id: str, pile_name: str, *card_codes):
    """ Add cards to a pile from a deck. If the pile doesn't exist, a new one is created.

    :param deck_id: The deck to add cards from.
    :param pile_name: The pile to add the cards to.
    :param card_codes: Comma-separated list of card codes to add to pile.
    """
    cards = ','.join(card_codes)
    response = requests.get(f'{cards_api_url}/{deck_id}/pile/{pile_name}/add/?cards={cards}')
    if response.ok:
        return response.json()
    raise ValueError(f'Error raised when creating a new player player. {response.status_code}: {response.content}')


def draw_cards_to_pile(deck_id: str, pile_name: str, count: int):
    """ Draw x cards from a deck to a pile.

    This could simulate things like:
        * A player drawing x cards
        * Discarding the top x cards from deck

    :param deck_id: The deck to add cards from.
    :param pile_name: The pile to add the cards to.
    :param count: The number of cards to draw.
    """
    draw = draw_cards_from_deck(deck_id, count)
    pile = add_cards_to_pile(deck_id, pile_name, *[card.code for card in draw.cards])
    return pile


def get_list_of_cards_in_pile(deck_id: str, pile_name: str) -> List[Card]:
    """ Get the list of cards from the specified pile.

    :param deck_id: The deck the pile originated from.
    :param pile_name: The pile to get the list of cards from.
    """
    response = requests.get(f'{cards_api_url}/{deck_id}/pile/{pile_name}/list/')
    if response.ok:
        return [Card(**card) for card in response.json()['piles'][pile_name]['cards']]
    raise ValueError(f'Error raised when listing cards from pile. {response.status_code}: {response.content}')
