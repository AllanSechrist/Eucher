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

    # debug
    def print_deck(self):
        for card in self.list_of_cards:
            print(card.rank + " of " + card.suit)


class Hand(Deck):
    """
    creates a hand of cards

    The idea behind making the Hand class a child class of Deck
    is due to the fact that a Hand of cards has the same function
    as a Deck, It is just a description of a grouping of Cards
    """

    def __init__(self, list_of_suits, list_of_ranks, size=5):
        Deck.__init__(self, list_of_suits, list_of_ranks, size)

    def remove_copy(self, copied_to, copied_from):
        for card in copied_to:
            for copy in copied_from:
                if copy == card:
                    copied_from.remove(copy)

    def create_hand(self, deck):
        self.list_of_cards = random.sample(deck, self.size)
        self.remove_copy(self.list_of_cards, deck)


class Kitty(Deck):
    """
    creates the Kitty object

    In Eucher, the Kitty is the remaining 4 cards in the deck, after the
    hands have been dealt to the players. The cards in the Kitty remain
    unknown to all players EXCEPT for the card on top of the Kitty.
    This card is revealed to all players, locking what players can make
    Trump until all players have passed or it is ordered up (in which case
    the suit of the face up card becomes trump and is placed into the dealers
    hand).
    """

    def __init__(self, list_of_suits, list_of_ranks, size=4):
        Deck.__init__(self, list_of_suits, list_of_ranks, size)

    def create_kitty(self, deck):
        self.list_of_cards = deck


def create_hands(list_of_suits, list_of_ranks, list_of_players, deck):
    for player in list_of_players:
        player.hand = Hand(list_of_suits, list_of_ranks)
        player.hand.create_hand(deck)
    kitty = Kitty(list_of_suits, list_of_ranks)
    kitty.create_kitty(deck)
    return kitty

deck = Deck(SUITS, RANKS)
