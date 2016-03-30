import cards
import player


def calling_round():
    # creates a loop that manages logic for player selection of the trump suit
    # happens at the start of every new play round
    top_card = cards.Deck.Cards[0]
    name = top_card.suit.name

    def loop():
        done = False
        while not done:
            top_of_kitty()
            done = pass_or_call()

    def top_of_kitty():
        print(top_card.name)

    def pass_or_call():

        for p in player.Player.List:
            done = False
            while not done:
                player_input = get_player_input(p)
                if player_input == 'PASS':
                    done = True
                elif player_input == 'TRUMP':
                    print(name + " has been made trump")
                    return True
                else:
                    print('invalid input')

        return pass_or_call_2()

    def get_player_input(p):
        player_input = input('player ' + str(p.player_number) + " PASS or TRUMP? :").upper()
        return player_input

    def pass_or_call_2():

        for p in player.Player.List:
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
                                return True
                            elif trump_input == name:
                                print('You cannot call that trump')
                                break
                            else:
                                print('invalid input')
                                break
                else:
                    print('invalid input')

    loop()
