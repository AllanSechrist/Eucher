import random
import itertools

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['9', '10', 'Jack', 'Queen', 'King', 'Ace']

class Card(object):
    """
    creates the card object. In Eucher, only 24 cards are used to play,
     9 through Ace (Ace being high) of every suit
    """

    # all a card is, is its suit and rank
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Deck(object):
    """
    creates a deck of cards
    """
    # there are 4 suits (Hearts, Diamonds, Clubs and Spades) and 7 ranks (9, 10, Jack, Queen, King and Ace)
    def __init__(self, list_of_suits, list_of_ranks, size=24):
        self.suits = list_of_suits
        self.ranks = list_of_ranks
        self.size = size
        self.list_of_cards = []

    def create_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                card = Card(suit, rank)
                self.list_of_cards.append(card)
    #debug
    def print_deck(self):
        for card in self.list_of_cards:
            print(card.rank + " of " + card.suit)

deck = Deck(SUITS, RANKS)
