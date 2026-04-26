from cards import CardDeck
from players import Player


PLAYER_COUNT = 4


class Game:
    def __init__(self):
        deck = CardDeck()

        players = [Player(h) for h in deck.deal(PLAYER_COUNT)]


    def do_round(self):
        pass