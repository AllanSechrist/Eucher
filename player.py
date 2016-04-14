

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
        Player.List.append(self)


class Team(object):
    """
    create team object
    """

    List = []

    def __init__(self, players):
        self.points = 0
        self.players = players
        Team.List.append(self)


def create_teams():
    team1 = []
    team2 = []
    for player in Player.List:
        if player.player_number is 0 or player.player_number is 2:
            team1.append(player)
        else:
            team2.append(player)

    Team(team1)
    Team(team2)


def create_players():
    for player_number in range(Player.NUMBER_OF_PLAYERS):
        Player(player_number)
