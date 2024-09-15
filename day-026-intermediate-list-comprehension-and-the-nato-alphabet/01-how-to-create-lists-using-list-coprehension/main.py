# List Comprehension
# new_list = [new_item for item in list]

numbers = [1, 2, 3]

new_numbers = [number + 1 for number in numbers]

# print(new_numbers)

double_numbers = [number * 2 for number in range(1, 5)]

# print(double_numbers)

# Conditional List Comprehension
# new_list = [new_item for item in list if condition]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]

long_names_uppercase = [name.upper() for name in names if len(name) > 5]

print(long_names_uppercase)
