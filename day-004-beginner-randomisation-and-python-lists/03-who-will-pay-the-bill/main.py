import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# random_index = random.randint(0, len(friends) - 1)

# payer = friends[random_index]

payer = random.choice(friends)

print(payer)