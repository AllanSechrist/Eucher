import cards
import player
from game_logic import calling_round, game_loop, play_round

list_of_player_objects = []
list_of_team_objects = []
PLAYERS = 4
player.create_players(PLAYERS, list_of_player_objects, list_of_team_objects)
"""
team1 = player.Team([list_of_player_objects[0], list_of_player_objects[2]])
team2 = player.Team([list_of_player_objects[1], list_of_player_objects[3]])

list_of_team_objects.append(team1)
list_of_team_objects.append(team2)
"""
playround = play_round.PlayRound(list_of_player_objects, list_of_team_objects)


def main():
    cards.deck.create_deck()
    # cards.deck.print_deck()
    # print(list_of_player_objects)
    # print(teams)
    kitty = cards.create_hands(list_of_player_objects, cards.deck.list_of_cards)
    """
    for player in list_of_player_objects:
        print(player.hand)
        print()
        for card in player.hand.list_of_cards:
            print(card.name)
            print()
    """
    for card in kitty.list_of_cards:
        print("kitty")
        print(card.name)
        print()

    calling_round_loop = calling_round.CallingRound(kitty, list_of_player_objects)
    calling_round_loop.calling_round_loop()
    playround.play_loop()
    quit()


if __name__ == "__main__":
    main()
