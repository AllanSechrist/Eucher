class Player(object):
    """
    creates the player object
    """

    def __init__(self, dealer=False):
        self.hand = []
        self.dealer = dealer


class Team(object):
    """
    creates the Team object
    """

    def __init__(self, players):
        self.players = players
        self.score = 0


def create_teams(players):
    team1 = Team((players[0], players[2]))
    team2 = Team((players[1], players[3]))
    return team1, team2


def create_players(number_of_players, player_objects):
    for player in range(number_of_players):
        player = Player()
        player_objects.append(player)
    return create_teams(player_objects)