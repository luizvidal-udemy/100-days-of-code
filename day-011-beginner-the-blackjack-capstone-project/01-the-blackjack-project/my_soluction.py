import random
from typing import TypedDict, List
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


class Player(TypedDict):
    score: int
    cards: List[int]


def draw_card():
    return random.choice(cards)


def blackjack_row():
    player_card = draw_card()
    player["cards"].append(player_card)
    player["score"] += player_card

    computer_card = draw_card()
    computer["cards"].append(computer_card)
    computer["score"] += computer_card


print(logo)

player: Player = {
    "score": 0,
    "cards": []
}

computer: Player = {
    "score": 0,
    "cards": []
}

for index in (range(2)):
    blackjack_row()

wish_continue = True

while player["score"] < 21 and computer["score"] < 21 and wish_continue:
    print(f"Your cards: {player['cards']}, current score: {player['score']}")
    print(f"Computer's first card: {computer['cards'][0]}")

    another_row = input(
        "Type 'y' to get another card, type 'n' to pass: ").lower() == "y"

    if another_row:
        blackjack_row()
    else:
        wish_continue = False

player_absolute_score = abs(21 - player["score"])
computer_absolute_score = abs(21 - computer["score"])

if player_absolute_score < computer_absolute_score:
    print("You win!")

elif player_absolute_score == computer_absolute_score:
    print("It's a draw!")

else:
    print("You lose!")

print(f"{player['cards']} -> {player['score']}")
print(f"{computer['cards']} -> {computer['score']}")
