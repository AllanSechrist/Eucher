import cards
import player
from game_logic import game_logic as gl


# anything not in a function is for debug/testing


def main():
    decks = cards.Deck()
    player.create_players()

    print(player.Player.List)
    for player_number in player.Player.List:
        print(player_number.player_number)

    player.create_teams()
    cards.create_hands()
    gl.calling_round()

    print(player.Team.List)
    for team in player.Team.List:
        for person in team.players:
            print()
            print(person.player_number)
            for card in person.hand.cards:
                print(card.name)

        print()

    for card in decks.Cards:
        print(card.name)
    print()
    print(len(decks.Cards))


if __name__ == "__main__":
    main()
