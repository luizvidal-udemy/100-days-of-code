import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

user_choice = int(
    input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors: ")
)
computer_choice = random.randint(0, 2)

if 0 <= user_choice <= 2:
    result = ""

    if user_choice == computer_choice:
        result = "It's a draw!"

    elif (user_choice == 0 and computer_choice == 2) or (
        user_choice == 1 and computer_choice == 0
    ):
        result = "You win!"

    else:
        result = "You lose!"

    print(
        f"""
          
    You chose:
    {choices[user_choice]}

    Computer chose:
    {choices[computer_choice]}

    {result}

    """
    )

else:
    print("You typed an invalid number!")
