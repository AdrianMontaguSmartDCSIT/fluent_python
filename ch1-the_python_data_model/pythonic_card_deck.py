"""
Example 1: Representing a deck of cards using two special methods
__getitem__ and __len__
"""

import collections

from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self) -> None:
        self._cards = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()

# Reading from the deck becomes easy
print(f"Card number 5: {deck[5]}")

# Get a random card
print(f"Random card: {choice(deck)}")

# Slicing the deck is simple - top 3 cards
print(f"Top 3 cards: {deck[0:3]}")

# Deck also becomes iterable
for card in deck[:5]:
    print(card)

# Because the deck is iterable, we can now do a sequental scan of the deck
print(f"Queen of hearts in deck: {Card('Q', 'hearts') in deck}")  # True

# Even sorting becomes easy
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
