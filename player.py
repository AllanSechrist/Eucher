

class Player(object):
    """
    create a player object
    """
    NUMBER_OF_PLAYERS = 4
    List = []

    def __init__(self, player_number):
        self.dealer = False
        self.hand = None
        self.tricks = 0
        self.player_number = player_number
        self.card_played = None
        self.took_last_trick = False
        self.team = None
        Player.List.append(self)

class Dealer(Player):
    pass


class Team(object):
    """
    create team object
    """

    List = []
    DBG = False

    def __init__(self):
        self.points = 0
        self.players = []
        Team.List.append(self)


def create_teams():
    team1 = Team()
    team2 = Team()

    for player in Player.List:
        if Team.DBG:
            print("play")
        if player.player_number is 0 or player.player_number is 2:
            player.team = team1
            team1.players.append(player)
        else:
            player.team = team2
            team2.players.append(player)


def create_players():
    for player_number in range(Player.NUMBER_OF_PLAYERS):
        Player(player_number)
