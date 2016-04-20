import cards
import player
import random


def assign_deal_order():
    play_order = []
    player_list = player.Player.List

    for person in player_list:
        if person.dealer is True:
            if person.player_number is 0:  # I'm sure there is a better way to do this, but for now this, to have something that works
                play_order = [player_list[1], player_list[2], player_list[3], player_list[0]]
            elif person.player_number is 1:
                play_order = [player_list[2], player_list[3], player_list[0], player_list[1]]
            elif person.player_number is 2:
                play_order = [player_list[3], player_list[0], player_list[1], player_list[2]]
            elif person.player_number is 3:
                play_order = [player_list[0], player_list[1], player_list[2], player_list[3]]

    return play_order


def assign_play_order():
    play_order = []
    player_list = player.Player.List
    for person in player_list:

        if person.took_last_trick is True:
            if person.player_number is 0:  # I'm sure there is a better way to do this, but for now this, to have something that works
                play_order = [player_list[0], player_list[1], player_list[2], player_list[3]]
            elif person.player_number is 1:
                play_order = [player_list[1], player_list[2], player_list[3], player_list[0]]
            elif person.player_number is 2:
                play_order = [player_list[2], player_list[3], player_list[0], player_list[1]]
            elif person.player_number is 3:
                play_order = [player_list[3], player_list[0], player_list[1], player_list[2]]
            person.took_last_trick = False  # ensures that variable is set to False after play order has been set
        """
        elif person.dealer is True:
            if person.player_number is 0:  # I'm sure there is a better way to do this, but for now this, to have something that works
                play_order = [player_list[1], player_list[2], player_list[3], player_list[0]]
            elif person.player_number is 1:
                play_order = [player_list[2], player_list[3], player_list[0], player_list[1]]
            elif person.player_number is 2:
                play_order = [player_list[3], player_list[0], player_list[1], player_list[2]]
            elif person.player_number is 3:
                play_order = [player_list[0], player_list[1], player_list[2], player_list[3]]
            person.dealer = False  # sets dealer to False to prevent person being picked twice during play
        """
    return play_order


def assign_dealer(count):
    if count < 1:
        dealer = random.choice(player.Player.List)  # assign random person to be dealer at game start
        dealer.dealer = True
        count += 1  # keeps track of number of rounds(may be changed later to a boolean for the start of the game)
        print('player ' + str(dealer.player_number) + ' has been made dealer')

        # debug
        print(dealer.dealer)
    else:  # if not the start of the game, the person to the left of the dealer becomes the new dealer
        for person in player.Player.List:
            if person.player_number is 3 and person.dealer is True:
                person.dealer = False
                player.Player.List[0].dealer = True
            elif person.dealer is True:
                person.dealer = False
                player.Player.List[person.player_number + 1].dealer = True


def calling_round():
    # creates a loop that manages logic for player selection of the trump suit
    # happens at the start of every new play round
    top_card = cards.Deck.Cards[0]
    name = top_card.suit.name  # name of the suit that is on the top of the
    round_count = 0  # keeps track of number of rounds

    assign_dealer(round_count)
    play_order = assign_deal_order()

    # manages function
    def loop():
        done = False
        while not done:
            top_of_kitty()
            done = pass_or_call()

    def top_of_kitty():
        print(top_card.name)

    def make_suit_trump(suit_name):  # sets trump to true for selected suit
        for suit in cards.Suit.suits:
            if suit.name == suit_name:
                suit.trump = True
                # debug
                print(suit.name + ' ' + str(suit.trump))

    def pass_or_call():

        for p in play_order:
            done = False
            while not done:
                player_input = get_player_input(p)
                if player_input == 'PASS':
                    done = True
                elif player_input == 'TRUMP':
                    print(name + " has been made trump")
                    make_suit_trump(name)  # set selected suit.trump to True
                    pick_up_trump()  # dealer must pick up the face up card and discard a card(can be the same card)
                    return True
                else:
                    print('invalid input')

        return pass_or_call_2()

    def get_player_input(p):
        player_input = input('player ' + str(p.player_number) + " PASS or TRUMP? :").upper()
        return player_input

    def pick_up_trump():
        dealers_hand = play_order[3].hand.cards

        dealers_hand.append(top_card)  # adds the top card of the kitty to the dealers hand
        cards.Deck.Cards.remove(top_card)  # removes top card from the kitty

        # the dealer adds the extra card to their hand before deciding which card to discard
        # the card that is discarded by the dealer MAY be the same card the dealer picked up

        for card in dealers_hand:
            print(card.name)

        done = False
        while not done:
            dealer_input = input('please select a card to discard: ').lower()
            for card in dealers_hand:
                if card.name.lower() == dealer_input:
                    dealers_hand.remove(card)  # removes chosen card from dealers hand
                    cards.Deck.Cards.append(card)  # places chosen card into the kitty
                    done = True

    # conditions after all players pass for the first time change
    def pass_or_call_2():

        for p in play_order:
            done = False
            while not done:
                player_input = get_player_input(p)
                if player_input == 'PASS':
                    done = True
                elif player_input == 'TRUMP':
                    while True:
                        trump_input = input('please select a suit to call trump: ')
                        for suit in cards.Suit.NAMES:

                            if trump_input == suit and suit != name:
                                print(suit + ' has been made trump')
                                make_suit_trump(trump_input)  # make selected suit trump (changes suit.trump to True)
                                return True
                            elif trump_input == name:
                                print('You cannot call that trump')
                                break

                else:
                    print('invalid input')

    """
    def set_trump_value():
        for suit in cards.Suit.suits:
            if suit.trump is True:
                for card in cards.Deck.Cards:
                    if card.suit == suit:
                        pass
    """

    loop()


# ///////////////////////////START PLAY ROUND LOGIC///////////////////////////////////////////////////////////////////


def play_round():
    board = []
    # event loop for play round

    def loop():
        count = 0
        done = False

        while not done:

            if count == 0:
                play_order = assign_deal_order()
            else:
                play_order = assign_play_order()

            for player in play_order:
                select_card(player)

            # debug ------------------------------
            print()
            for card in board:
                print(card.name)
                print(card.ranks[card.rank])
            # end debug --------------------------

            select_highest_card()  # picks highest card and awards the trick to the player who played it
            clean_board()  # resets board for next round of play

            count += 1

            if count > 4:
                done = True
                award_points()

    def select_card(player):
        print()
        print("player " + str(player.player_number) + " please select a card to play")
        print()
        for card in player.hand.cards:
            print(card.name)

        done = False
        while not done:
            player_input = input("please select a card to play: ").lower()
            for card in player.hand.cards:
                if card.name.lower() == player_input:
                    done = check_suit(card, player)  # check if player is following suit

    def play_card(card, player):  # removes selected card from players hand and adds it to the board

        board.append(card)
        player.hand.cards.remove(card)
        player.card_played = card

    def check_suit(card, player):
        suit_to_follow = set_suit_to_follow()

        if suit_to_follow is not None:  # checks if suit to follow is None
            print()
            print("suit to follow is " + suit_to_follow.name)
            if card.suit is not suit_to_follow:  # checks selected card's suit to see if it matches suit to follow
                print()
                print("card is not suit to follow")
                for card_in_hand in player.hand.cards:  # checks players hand for cards that match suit to follow
                    print()
                    print("checking hand for card that follows suit")
                    if card_in_hand.suit is suit_to_follow:  # player must follow suit, return False and select again
                        print("you have a " + suit_to_follow.name + " in your hand! you must follow suit")
                        return False

                print('playing off suit card')  # shows us that we cannot follow suit, so we can play anything

        play_card(card, player)
        return True

    def set_suit_to_follow():
        if len(board) > 0:
            suit_to_follow = board[0].suit
        else:
            suit_to_follow = None
        return suit_to_follow

    def select_highest_card():
        card_values = []  # keeps track of card values
        suit_to_follow = set_suit_to_follow()
        high_card = None
        for card in board:
            if card.suit is not suit_to_follow:
                continue
            else:
                card_values.append(card.ranks[card.rank])
                if card.ranks[card.rank] == max(card_values):
                    high_card = card

        award_trick(high_card)

    def award_trick(high_card):
        for person in player.Player.List:
            if person.card_played == high_card:
                person.tricks += 1
                print('player ' + str(person.player_number) + ' took the trick with ' + high_card.name)
                print('player ' + str(person.player_number) + ' has ' + str(person.tricks) + ' tricks.')
                person.took_last_trick = True
                print(str(person.took_last_trick) + " player " + str(person.player_number))

    def award_points():
        for team in player.Team.List:
            total_tricks = 0
            for partner in team:
                total_tricks += partner.tricks
            if 2 < total_tricks < 5:
                team.points += 1
            elif total_tricks == 5:
                team.points += 2

    def clean_board():  # empties the board list
        for card in board[::-1]:
            board.remove(card)

    loop()  # manages play round
