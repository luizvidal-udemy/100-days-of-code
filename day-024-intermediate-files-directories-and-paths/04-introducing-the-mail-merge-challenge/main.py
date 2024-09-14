import os


# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
STARTING_LETTER_PATH = os.path.join(
    CURRENT_DIR, "Input/Letters/starting_letter.txt")
INVITED_NAMES_PATH = os.path.join(CURRENT_DIR, "Input/Names/invited_names.txt")
READY_TO_SEND_PATH = os.path.join(CURRENT_DIR, "Output/ReadyToSend")
PLACEHOLDER = "[name]"

starting_letter = ""

invited_names = []

with open(STARTING_LETTER_PATH) as file:
    starting_letter = file.read()

with open(INVITED_NAMES_PATH) as file:
    invited_names = file.readlines()


for name in invited_names:
    name = name.strip()

    letter = starting_letter.replace(PLACEHOLDER, name)

    with open(f"{READY_TO_SEND_PATH}/letter_for_{name}.txt", "w") as file:
        file.write(letter)
