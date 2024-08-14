def life_in_weeks(age):
    remaining_weeks = (90 - age) * 52

    print(f"You have {remaining_weeks} weeks left.")


age = int(input("Whats is your age? "))

life_in_weeks(age)
