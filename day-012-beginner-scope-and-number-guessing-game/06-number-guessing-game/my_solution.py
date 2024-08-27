from typing import TypedDict, Dict
from art import logo
import random


def welcome() -> None:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def generate_random_number() -> int:
    return random.randint(1, 100)


def decrease_remaining_lives() -> None:
    game_data["remaining_lives"] -= 1


def set_remaining_lives(amount: int) -> None:
    game_data["remaining_lives"] = amount


def set_guess(guess: int):
    game_data["latest_guess"] = guess


def show_tip():
    if game_data["latest_guess"] < game_data['random_number']:
        print("Too low.")
    else:
        print("Too high.")


def have_remaining_lives() -> bool:
    return game_data['remaining_lives'] > 0


def guessed_wrong() -> bool:
    return game_data['latest_guess'] != game_data["random_number"]


class GameData(TypedDict):
    random_number: int
    remaining_lives: int
    latest_guess: int


game_data: GameData = {
    "latest_guess": 0,
    "random_number": generate_random_number(),
    "remaining_lives": 0
}


DIFFICULTY = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


if DIFFICULTY == 'easy':
    set_remaining_lives(10)
else:
    set_remaining_lives(5)

while have_remaining_lives() and guessed_wrong():
    print(game_data["random_number"])
    print(
        f"You have {game_data['remaining_lives']} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    set_guess(guess)
    show_tip()
    decrease_remaining_lives()

if not have_remaining_lives():
    print("You've run out of guesses, you lose.")

if not guessed_wrong():
    print(f"You got it! The answer was {game_data['random_number']}.")
