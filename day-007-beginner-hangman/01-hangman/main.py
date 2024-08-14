# import random

# word_list = ["aardvark", "baboon", "camel"]

# chosen_word = random.choice(word_list)

# lives = len(chosen_word)

# placeholder = ""

# for letter in chosen_word:
#     placeholder += "_"

# def mutate_string(string, position, character):
#     return string[:position] + character + string[position + 1:]

# while lives > 0 and placeholder != chosen_word:
#     print(placeholder)

#     guess = input("Guess a letter: ").lower()

#     if guess not in chosen_word:
#         print(f"You guessed {guess}, that's not in the word. You lose a life. current lives: {lives}")
#         lives -= 1

#     for index in range(len(chosen_word)):
#         if chosen_word[index] == guess:
#             placeholder = mutate_string(placeholder, index, guess)

#     print(placeholder)

# if placeholder == chosen_word:
#     print(f"You win! The word is {chosen_word}.")
# else:
#     print(f"You lose. The word was {chosen_word}.")


import random
from hangman_words import word_list
from hangman_art import stages, logo



lives = 6

chosen_word = random.choice(word_list)

print(logo)

# print(chosen_word)

placeholder = ""

word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"

game_over = False

correct_letters = []

while not game_over:
    print(f"****************************** {lives}/6 LIVES LEFT ******************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives  == 0:
            game_over = True
            print(f"********************** IT WAS {chosen_word}! YOU LOSE ****************************")

    if "_" not in display:
        game_over = True
        print("************************************* YOU WIN *************************************")


    print(stages[lives]) 
