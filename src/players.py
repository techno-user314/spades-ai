class Player:
    def __init__(self, hand):
        self.cards = hand
        self.tricks = 0


    def bid(self):
        return 1


    def play(self, table):
        return self.cards.play(0)


    def did_win(self, did_i_win):
        self.tricks += int(did_i_win)
