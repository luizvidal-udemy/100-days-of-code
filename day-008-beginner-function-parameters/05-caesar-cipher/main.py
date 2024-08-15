# alphabet = [
#     "a",
#     "b",
#     "c",
#     "d",
#     "e",
#     "f",
#     "g",
#     "h",
#     "i",
#     "j",
#     "k",
#     "l",
#     "m",
#     "n",
#     "o",
#     "p",
#     "q",
#     "r",
#     "s",
#     "t",
#     "u",
#     "v",
#     "w",
#     "x",
#     "y",
#     "z",
# ]


# def encode():
#     word = input("Type the word to encode: ").lower()
#     shift = int(input("Type the shift number: "))

#     return None


# def decode(word: str, shift: int):
#     return None


# mode = input("Type 'encode' to enter encode mode or 'decode' to enter decode mode: ")

# if mode == "encode":
#     print("You are in encode mode")
# else:
#     print("You are in decode mode")


# def shift_array(array: list, shift: int):
#     array_length = len(array)
#     shifted_array = []
#     absolute_shift = 0

#     for _ in range(array_length):
#         shifted_array.append("")

#     if shift > array_length:
#         absolute_shift = shift % len(array)
#     elif shift == array_length:
#         absolute_shift = 0
#     else:
#         absolute_shift = shift

#     if absolute_shift == 0:
#         shifted_array = array

#     else:
#         for index, element in enumerate(array):
#             if index + absolute_shift < array_length:
#                 shifted_array[index + absolute_shift] = element

#             else:
#                 shifted_array[index + absolute_shift - array_length] = element

#     return shifted_array


# def unshift_array(array: list, shift: int):
#     array_length = len(array)
#     unshifted_array = []
#     absolute_shift = 0

#     for _ in range(array_length):
#         unshifted_array.append("")

#     if shift > array_length:
#         absolute_shift = shift % len(array)
#     elif shift == array_length:
#         absolute_shift = 0
#     else:
#         absolute_shift = shift

#     if absolute_shift == 0:
#         unshifted_array = array

#     else:
#         for index, _ in enumerate(array):
#             if index + absolute_shift < array_length:
#                 unshifted_array[index] = array[index + absolute_shift]
#             else:
#                 unshifted_array[index] = array[index + absolute_shift - array_length]

#     return unshifted_array

# def encode(word: str, shift: int):
#     shifted_array = shift_array(alphabet, shift)

#     encoded_word = ""

#     for letter in word:
#         index = alphabet.index(letter)
#         print(shifted_array[index])
#         encoded_word += shifted_array[index]

#     return encoded_word


# def shift_array(array: list, shift: int) -> list:
#     for _ in range(shift):
#         array.append(array.pop(0))
#     return array


# def encode(word: str, shift: int) -> str:

#     shifted_alphabet: list[str] = shift_array(alphabet.copy(), shift)
#     encoded_word = ""

#     for letter in word:
#         try:
#             index = alphabet.index(letter.lower())

#             if letter.islower():
#                 encoded_word += shifted_alphabet[index]
#             else:
#                 encoded_word += shifted_alphabet[index].upper()

#         except:
#             encoded_word += letter

#     return encoded_word

# def decode(word: str, shift: int) -> str:
#     shifted_alphabet: list[str] = shift_array(alphabet.copy(), shift)

#     decoded_word = ""

#     for letter in word:
#         try:
#             index = shifted_alphabet.index(letter.lower())

#             if letter.islower():
#                 decoded_word += alphabet[index]
#             else:
#                 decoded_word += alphabet[index].upper()

#         except:
#             decoded_word += letter

#     return decoded_word


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

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


def encrypt(original_text: str, shift_amount: int):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f"The encoded text is {cipher_text}")


def decrypt(original_text: str, shift_amount: int):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f"The encoded text is {cipher_text}")


decrypt("b", 1)
