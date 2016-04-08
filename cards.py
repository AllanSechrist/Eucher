import random
import player


class Suit(object):
    """
    creates a suit object
    """
    suits = []
    NAMES = ['hearts', 'diamonds', 'clubs', 'spades']

    def __init__(self, name):
        self.name = name
        self.trump = False

        Suit.suits.append(self)


class Card(object):
    """
    creates a card with a suit and a rank
    """

    ranks = {'9': 0, '10': 1, 'Jack': 2, 'Queen': 3, 'King': 4, 'Ace': 5}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.name = rank + " of " + suit.name


class Deck(object):
    """
    creates a deck of cards
    """
    Cards = []

    def __init__(self):
        Deck.create_suits()
        Deck.create_cards()

    @staticmethod
    def create_suits():
        for name in Suit.NAMES:
            Suit(name)

    @staticmethod
    def create_cards():
        for suit in Suit.suits:
            for rank in Card.ranks.keys():
                Deck.Cards.append(Card(suit, rank))

    @staticmethod
    def shuffle():
        random.shuffle(Deck.Cards)


class Hand(object):
    """
    creates a hand of cards
    """

    HAND_SIZE = 5

    def __init__(self, player):
        # a list of cards
        self.cards = []
        self.make_hand()
        player.hand = self

    def make_hand(self):
        for slot in range(Hand.HAND_SIZE):
            Deck.shuffle()
            self.swap(Deck.Cards[0])

    def swap(self, card):
        Deck.Cards.remove(card)
        self.cards.append(card)


def create_hands():
    for person in player.Player.List:
        Hand(person)
