import random


def deal_cards():
    """Returns a random ard from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())
