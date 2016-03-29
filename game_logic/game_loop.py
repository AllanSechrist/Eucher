"""
Play goes from the calling round to the play round and continues in the fashion
until one team scores a total of 10 points, in which case that team wins and the game
ends.
"""

from game_logic import calling_round, play_round
import cards


class GameLoop(object):
    """
    Manages the whole game by keep the score, and all game objects and states
    """
    def __init__(self, teams, players, deck):
        self.teams = teams
        self.players = players
        # the game loop will not actually take in the kitty, this object (along with hands),
        # must be created with in the loop, so new hands and kitties are created with each new round
        self.deck = deck
        self.rounds = 1
        self.trump = None

    def game_loop(self):
        game_over = False
        while not game_over:
            print("Dealing cards, and creating teams...")

            self.trump = self.start_calling_round()

    def start_calling_round(self):
        kitty = None
        calling_round_loop = calling_round.CallingRound(kitty, self.players)
        trump = calling_round_loop.calling_round_loop()
        return trump

    def set_trump(self):
        for suit in self.deck.suits:
            if suit == self.trump:
                suit.trump == True
