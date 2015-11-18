"""
In Eucher, each player takes turns deciding if they want the face up
card on the kitty to become trump. Starting with the left of the
dealer and continuing in a clockwise motion (to the left),
each player has a chance to "order up" the face up card,
making that suit trump (and ending the calling round) or
passing the choice to the next person. If a card is "ordered up",
the dealer places the face up card into their hand and discards a card,
face down, and the play round starts (with the person to the left of the
dealer). If everyone passes and the choice falls to the dealer, the dealer
can pick up the card to make that suit trump as normal, or pass by turning
the face up card face down. If the dealer passes, the calling round continues
in the same fashion, the player to the left of the dealer has a chance to
make any suit trump, except for the suit that was just turned down, or to
pass. In the event that it gets back to the dealer, some variations of the game
allow for the passing round to continue if the dealer does not wish to call, but
this version will feature the "stab/shaft the dealer" rule in which the dealer
MUST call trump.
"""


# calling round loop

def calling_round_loop(kitty, list_of_players):
    print(kitty.list_of_cards[0].name)
    pass_or_call(list_of_players)


def pass_or_call(list_of_players):
    for player in range(list_of_players):
        player_input = get_player_input()
        if player_input == "PASS":
            continue
        elif player_input == "TRUMP":
            # make_trump()
            break
        else:
            print("invalid input")


def get_player_input():
    player_input = input("PASS or TRUMP? :").upper()
    return player_input


