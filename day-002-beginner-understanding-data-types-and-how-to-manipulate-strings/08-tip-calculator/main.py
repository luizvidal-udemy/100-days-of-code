print("Welcome to the tip calculator!")

total_bill = float(
  input("What was the total bill? $")
)

tip_percentage = float(
  input("How much tip would you like to give? 10, 12, or 15? ")
) / 100

number_of_people = int(
  input("How many people to split the bill? ")
)

total_bill *= (1 + tip_percentage)

bill = round(total_bill / number_of_people, 2)

print(f"Each person should pay: ${bill}")