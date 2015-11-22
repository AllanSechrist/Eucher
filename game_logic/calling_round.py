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

class CallingRound(object):
    """
    creates calling round object
    """

    def __init__(self, kitty, list_of_players):
        self.kitty = kitty
        self.list_of_players = list_of_players

    # manages calling round loop
    def calling_round_loop(self):
        print(self.kitty.list_of_cards[0].name)
        self.pass_or_call()

    # class method that starts logic loop for the games calling round
    def pass_or_call(self):
        for player in range(len(self.list_of_players)):
            player_input = self.get_player_input(player)
            if player_input == "PASS":
                continue
            elif player_input == "TRUMP":
                print(self.kitty.list_of_cards[0].suit + " has been made trump")
                # make_trump(self.kitty.list_of_cards[0].suit)
                break
            else:
                print("invalid input")


    # method that returns player input
    def get_player_input(self, get_player):
        player = get_player + 1
        player_input = input("player " + str(player) + " PASS or TRUMP? :").upper()
        return player_input
