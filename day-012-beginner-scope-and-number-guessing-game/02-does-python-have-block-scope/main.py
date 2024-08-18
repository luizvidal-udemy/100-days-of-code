"""day-012-beginner-scope-and-number-guessing-game/02-does-python-have-block-scope/main.py"""

GAME_LEVEL = 3
enemies = [
    "skeleton",
    "zombie",
    "alien"
]


def create_enemy():
    """A function that creates an enemy"""
    new_enemy = ""
    if GAME_LEVEL < 5:
        new_enemy = enemies[0]

    print(new_enemy)


create_enemy()
