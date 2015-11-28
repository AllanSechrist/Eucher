import cards

"""
During the play round, players take turn player cards, starting with the player to
the left of the dealer (or the player that took the last trick) until everyone plays all
five cards in their hand. Players must follow the suit of the first card played, with the
highest of that suit's rank winning the trick, unless a player cannot follow suit and plays
a card from the suit that was made trump, then the highest ranked trump will win the trick.
players score points by winning 3 or more tricks, 3 or 4 will score 1 point and taking all 5
will score 2 points. If the team that DID NOT call trump takes 3 tricks, that is a Eucher, and
that team is awarded 2 points. If a player thinks that they can take ALL 5 tricks by themselves, they
have the option of going alone, which must be declared after THEY call trump. If the player manages
to take all 5 tricks alone, the team is awarded 4 points; if they take 3 or 4, they only get 1 point,
if the other team Euchers them, the other team gets 2 points.
"""


class PlayRound(object):
    """
    creates playround loop
    """

    def __init__(self, players):
        self.players = players

    def play_loop(self):
        done = False
        turn = 0
        # creates a new board at the start of every new play round
        board = Board()

        while not done:
            player_turn = self.players[turn]
            print("player " + str(turn + 1) + " it is your turn")
            board.play_card(player_turn)


class Board(object):
    """
    creates board for card interaction during play round
    also manages game logic(?)
    """

    def __init__(self):
        # the board state keeps track of what cards have been played
        self.board_state = []
        self.trump = 0
        self.suit_to_follow = None

    def play_card(self, player_turn):
        card = None
        while card is None:
            card = player_turn.play_card(self.board_state, self.suit_to_follow)

    """
    def player_input(self, track_turn):
        player_hand = self.players[track_turn].hand
        played = False

        for card in player_hand:
            print(card)

        player_card = input("please select a card to play: ").upper()

        for card in player_hand:
            if card.name.upper() == player_card:
                print("You play " + card.name)
                self.board_state.append(card)
                cards.remove_copy(self.board_state, player_hand)
                played = True
                break

            else:
                print("You do not have that card in your hand")

        return played
    """
