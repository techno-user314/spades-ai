from enum import Enum
import random


class Suits(Enum):
    HEARTS = 2
    DIAMONDS = 3
    CLUBS = 4
    SPADES = 1


class CardRank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class CardException(Exception):
    pass


class Card:
    def __init__(self, suit, rank):
        if suit in Suits and rank in CardRank:
            self.suit = suit
            self.rank = rank
        else:
            raise CardException("Suit/rank combination not valid")

    def _check_card_validity(self, other_obj):
        if not isinstance(other_obj, Card):
            raise CardException("Cannot compare Card with non-Card object")

    def __gt__(self, other): # >
        self._check_card_validity(other)
        if self.suit == other.suit:
            return self.rank > other.rank
        elif self.suit == Suits.SPADES:
            return True
        return False

    def __lt__(self, other): # <
        self._check_card_validity(other)
        if self.suit == other.suit:
            return self.rank < other.rank
        elif other == Suits.SPADES:
            return True
        return True

    def __str__(self):
        return f"{self.rank.name} of {self.suit.name}"


class CardDeck:
    def __init__(self):
        self.cards = [Card(suit, rank) for rank in CardRank for suit in Suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, player_count):
        odd_cards = len(self.cards) % player_count
        for _ in range(odd_cards):
            self.cards.pop()

        self.shuffle()
        hands = [Hand() for _ in range(player_count)]
        while len(self.cards) > 0:
            for hand in hands:
                hand.add_card(self.cards.pop())
        return hands


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        if not isinstance(card, Card):
            raise TypeError("Cannot add non-Card object to Hand")
        self.cards.append(card)


if __name__ == '__main__':
    deck = CardDeck()
    for hand in deck.deal(3):
        for card in hand.cards:
            print(card)
        print("")
