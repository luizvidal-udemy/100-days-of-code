from art import logo, vs
from game_data import data
from random import choice


#   Formate the account data into printable format.
def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"Compare A: {account_name}, {account_description}, from {account_country}."


#   Use if statement to check if user is correct.
def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


#   Display art.
print(logo)
score = 0
game_should_continue = True
account_b = choice(data)

#   Make game repeatable.
while game_should_continue:

    #   Generate a random account from the game data.

    #   Making acccount at position B become the next account at posistion A.
    account_a = account_b
    account_b = choice(data)

    if account_a == account_b:
        account_b = choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #   Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(logo)

    #   Check if user is correct.
    #       Get follwer count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #   Give user feedback on their guess.
    #   Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
