import pandas
from pathlib import Path

CURRENT_DIR = Path(__file__).parent

NATO_PHONETIC_DATA_PATH = CURRENT_DIR / "nato_phonetic_alphabet.csv"

data = pandas.read_csv(NATO_PHONETIC_DATA_PATH)

nato_data = {row.letter: row.code for (_, row) in data.iterrows()}

word = input("Type a word: ").upper()

phonetic_code_list = [nato_data[letter] for letter in word]

print(phonetic_code_list)
