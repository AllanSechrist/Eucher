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

