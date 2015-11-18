import cards
import player
from game_logic import calling_round

list_of_player_objects = []
PLAYERS = 4
teams = player.create_players(PLAYERS, list_of_player_objects)


def main():
    cards.deck.create_deck()
    cards.deck.print_deck()
    print(list_of_player_objects)
    print(teams)
    kitty = cards.create_hands(cards.SUITS, cards.RANKS, list_of_player_objects, cards.deck.list_of_cards)

    for player in list_of_player_objects:
        print(player.hand)
        print()
        for card in player.hand.list_of_cards:
            print(card.name)
            print()

    for card in kitty.list_of_cards:
        print("kitty")
        print(card.name)
        print()

    calling_round.calling_round_loop(kitty, list_of_player_objects)
    quit()

if __name__ == "__main__":
    main()