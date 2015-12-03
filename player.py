import cards


class Player(object):
    """
    creates the player object
    """

    def __init__(self):
        self.hand = None
        self.dealer = False
        self.tricks = 0

    def play_card(self, suit_to_follow):
        for card in self.hand.list_of_cards:
            print(card.name)

        player_card = input("please select a card to play: ").upper()

        played_card = self.check_card(suit_to_follow, player_card)

        return played_card

    def check_card(self, suit_to_follow, player_card):
        selected_card = None
        card_match = False
        for card in self.hand.list_of_cards:
            if card.name.upper() == player_card:
                selected_card = self.check_follow_suit(suit_to_follow, card)
                card_match = True

        if card_match is False:
            print("you do not have that card in your hand")

        return selected_card

    # checks to see if player has followed suit
    def check_follow_suit(self, suit_to_follow, card):
        if suit_to_follow is not None:
            print()
            print("suit to follow is " + suit_to_follow)
            if card.suit is not suit_to_follow:
                print()
                print("card is not suit to follow")
                for suit in self.hand.list_of_cards:
                    print()
                    print("checking hand for card that follows suit")
                    if suit.suit is suit_to_follow:
                        print("you have a " + suit_to_follow + " in your hand! You must follow suit!")
                        return None

                print()
                print("no card matches, playing junk card")

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
