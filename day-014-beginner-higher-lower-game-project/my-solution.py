from random import choice
from game_data import data, Person
from art import logo, vs


def load_random_person() -> Person:
    person = choice(data)
    data.remove(person)
    return person


def compose_compare_info(compare: Person, against: Person) -> None:
    print(
        f"Compare A: {compare['name']}, {compare['description']}, from {compare['country']} ==> {compare['follower_count']}.")

    print(vs)

    print(
        f"Against B: {against['name']}, {against['description']}, from {against['country']} ==> {against['follower_count']}.")


def clear_screen() -> None:
    print("\n" * 30)


score = 0

game_over = False

compare = load_random_person()

print(logo)

while not game_over:

    against = load_random_person()

    game_row = [compare, against]

    compose_compare_info(compare, against)

    chosen_person_index = 0 if input(
        "Who has more followers? Type 'A' or 'B': ").upper() == 'A' else 1

    chosen_person = game_row.pop(chosen_person_index)

    against = game_row[0]

    if chosen_person['follower_count'] > against['follower_count']:
        compare = against
        score += 1
        clear_screen()
        print(logo)
        print(f"You're right! Current score: {score}.")
    else:
        clear_screen()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_over = True
