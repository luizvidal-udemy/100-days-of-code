from pathlib import Path


CURRENT_DIR = Path(__file__).parent

FILE_1_PATH = CURRENT_DIR / "file1.txt"

FILE_2_PATH = CURRENT_DIR / "file2.txt"


def read_numbers_from_file(path):
    with open(path) as file:
        return [int(number.strip()) for number in file.readlines()]


file_1_numbers = read_numbers_from_file(FILE_1_PATH)

file_2_numbers = read_numbers_from_file(FILE_2_PATH)

all_numbers = [*file_1_numbers, *file_2_numbers]

result = [
    number for number in all_numbers if number in file_1_numbers and number in file_2_numbers
]

print(result)
