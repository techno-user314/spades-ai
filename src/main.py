from cards import CardDeck
from players import Player


PLAYER_COUNT = 4


class Game:
    def __init__(self):
        deck = CardDeck()
        self.rounds = 0

        self.players = [Player(h) for h in deck.deal(PLAYER_COUNT)]


    def do_round(self):
        self.rounds += 1

        on_table = []
        winner = 0
        for player in self.players:
            on_table.append(player.play(on_table))

        for i, card in enumerate(on_table[1:]):
            if card > on_table[winner]:
                winner = i

        for i, player in enumerate(self.players):
            player.did_win(winner==i)

        for card in on_table:
            print(card)
        print(winner)


if __name__ == '__main__':
    game = Game()
    game.do_round()
