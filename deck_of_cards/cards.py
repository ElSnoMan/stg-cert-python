import requests


card_suits = ['♠', '♥', '♦', '♣']

cards_api_url = 'https://deckofcardsapi.com/api/deck'


def new_deck(shuffled=True):
    if shuffled:
        response = requests.get(f'{cards_api_url}/new/shuffle/')
        requests.post()
    else:
        response = requests.get(f'{cards_api_url}/new/')

    if response.ok:
        return response.json()

    raise ValueError('Error raised when trying to create deck.')
