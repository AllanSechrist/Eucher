import cards
import player
import random


def assign_play_order():
    play_order = []
    player_list = player.Player.List
    for person in player_list:
        if person.dealer is True:
            if person.player_number is 0:
                play_order = [player_list[1], player_list[2], player_list[3], player_list[0]]
            elif person.player_number is 1:
                play_order = [player_list[2], player_list[3], player_list[0], player_list[1]]
            elif person.player_number is 2:
                play_order = [player_list[3], player_list[0], player_list[1], player_list[2]]
            elif person.player_number is 3:
                play_order = [player_list[0], player_list[1], player_list[2], player_list[3]]

    return play_order


def assign_dealer(count):

    if count < 1:
        dealer = random.choice(player.Player.List)
        dealer.dealer = True
        count += 1
        print('player ' + str(dealer.player_number) + ' has been made dealer')

        # debug
        print(dealer.dealer)
    else:
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
    play_order = assign_play_order()

    # manages function
    def loop():
        done = False
        while not done:
            top_of_kitty()
            done = pass_or_call()

    def top_of_kitty():
        print(top_card.name)

    def make_suit_trump(suit_name):
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
                    make_suit_trump(name)
                    pick_up_trump()
                    return True
                else:
                    print('invalid input')

        return pass_or_call_2()

    def get_player_input(p):
        player_input = input('player ' + str(p.player_number) + " PASS or TRUMP? :").upper()
        return player_input

    def pick_up_trump():
        dealers_hand = play_order[3].hand.cards
        for card in dealers_hand:
            print(card.name)

        done = False
        while not done:
            dealer_input = input('please select a card to discard: ').lower()
            for card in dealers_hand:
                if card.name.lower() == dealer_input:
                    dealers_hand.append(top_card)
                    cards.Deck.Cards.remove(top_card)
                    dealers_hand.remove(card)
                    cards.Deck.Cards.append(card)
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
                                make_suit_trump(trump_input)
                                return True
                            elif trump_input == name:
                                print('You cannot call that trump')
                                break

                else:
                    print('invalid input')

    loop()

# ----------START PLAY ROUND LOGIC------------

def play_round():
    pass
