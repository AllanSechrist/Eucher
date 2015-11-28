import cards


class Player(object):
    """
    creates the player object
    """

    def __init__(self):
        self.hand = []
        self.dealer = False
        self.tricks = 0

    def play_card(self, board, suit_to_follow):
        for card in self.hand:
            print(card.name)

        player_card = input("please select a card to play: ").upper()
        """
        for card in self.hand:
            if card.name.upper() == player_card:
                board.append(card)
                cards.remove_copy(board, self.hand)
                return player_card
        """
        self.check_follow_suit(suit_to_follow, player_card, board)
        print("you do not have that card in your hand")

    def check_follow_suit(self, suit_to_follow, player_card, board):
        for card in self.hand:
            if card.name.upper() == player_card:
                if suit_to_follow is not None:
                    if card.suit != suit_to_follow:
                        for suit in self.hand:
                            if suit.suit == suit_to_follow:
                                print("You have a " + suit_to_follow + " in your hand! You must follow suit!")
                            else:
                                return card
            board.append(card)
            cards.remove_copy(board, self.hand)
            return card


class Team(object):
    """
    creates the Team object
    """

    def __init__(self, players):
        self.players = players
        self.score = 0
        self.tricks = 0

    def scoring(self):
        if self.tricks == 3:
            self.score += 1
        elif self.tricks == 5:
            self.score += 2

    def tricks(self):
        self.tricks = self.players[0].tricks + self.players[1].tricks


def create_teams(players):
    team1 = Team((players[0], players[2]))
    team2 = Team((players[1], players[3]))
    return team1, team2


def create_players(number_of_players, player_objects):
    for player in range(number_of_players):
        player = Player()
        player_objects.append(player)
    return create_teams(player_objects)
