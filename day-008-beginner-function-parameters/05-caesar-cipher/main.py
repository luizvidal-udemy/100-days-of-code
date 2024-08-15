from art import logo

print(logo)

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

should_continue = True


def caesar(original_text, shift_amount, direction):
    output_text = ""

    if direction == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter

        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"The {direction}d text is {output_text}")


while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n"
    ).lower()

    if restart == "no":
        should_continue = False
        print("Goodbye")
