from deck_of_cards import deck_service
from deck_of_cards.player import Player


def play_game():
    deck = deck_service.new_deck()
    p1 = Player(deck.id, name='player1', starting_hand_count=1)
    p2 = Player(deck.id, name='player2', starting_hand_count=1)

    while True:
        p1_card = p1.cards[0].numeric_value
        p2_card = p2.cards[0].numeric_value
        if p1_card > p2_card:
            winner = f'{p1.name}: {p1_card} beat {p2_card}'
            break
        elif p1_card < p2_card:
            winner = f'{p2.name}: {p2_card} beat {p1_card}'
            break
        else:  # it's a tie, so try again
            p1.draw_cards(count=1)
            p2.draw_cards(count=1)

    print(winner)


if __name__ == '__main__':
    play_game()
