from deck_of_cards import cards

cards_api_url = 'https://deckofcardsapi.com/api/deck'


def game():
    deck = cards.new_deck()
    print('in the game')


if __name__ == '__main__':
    game()
