def count_letter_in_word(word: str, letter: str):
    return word.count(letter)


name = input("Type your name: ").lower()
lover_name = input("Type your love name: ").lower()

couple_name = f"{name} {lover_name}"


first_word = "true"
second_word = "love"

def calculate_love_score():
    first_digit = 0
    second_digit = 0

    for letter in first_word:
        first_digit += count_letter_in_word(couple_name, letter)

    for letter in second_word:
        second_digit += count_letter_in_word(couple_name, letter)

    return f"{first_digit}{second_digit}"

print(f"Your love score is {calculate_love_score()}")