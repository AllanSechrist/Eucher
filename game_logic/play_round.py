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

    def __init__(self, players, teams):
        self.players = players
        self.teams = teams
        self.trump = None

    def play_loop(self):
        turn = 0
        # creates a new board at the start of every new play round
        board = Board()

        for player in self.players:
            print("player " + str(player.player_number) + " it is your turn")
            board.get_card(player)
            turn += 1

        board.determine_trick_winner(self.teams, board.select_highest_card())





class Board(object):
    """
    creates board for card interaction during play round
    also manages game logic(?)
    """

    def __init__(self):
        # the board state keeps track of what cards have been played
        self.board_state = []
        self.trump = None
        self.suit_to_follow = None

    def get_card(self, player_turn):
        card = None
        while card is None:
            card = player_turn.play_card(self.suit_to_follow)

        self.board_state.append(card)
        cards.remove_copy(self.board_state, player_turn.hand.list_of_cards)

        if self.suit_to_follow is None:
            self.suit_to_follow = card.suit

        # debug
        print("We have exited the get card loop")
        for x in self.board_state:
            print(x.name)
            print()
        for x in player_turn.hand.list_of_cards:
            print()
            print(x.name)

    def select_highest_card(self):
        card_values = []
        high_card = None
        for card in self.board_state:
            if card.suit is not self.suit_to_follow:
                continue
            else:
                card_values.append(cards.RANKS[card.rank])
                if cards.RANKS[card.rank] == max(card_values):
                    high_card = card

        return high_card

    def determine_trick_winner(self, teams, high_card):
        for team in teams:
            for player in team.players:
                if player.played_card == high_card:
                    player.tricks += 1
                    print("player " + str(player.player_number) + " took the trick with " + player.played_card.name)
                print("player number: " + str(player.player_number) + " " + str(player.tricks))

