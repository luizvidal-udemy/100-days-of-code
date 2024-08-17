def check_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 400 == 0:
            return True

        if year % 100 == 0:
            return False

        return True

    return False


year = int(input("Which year do you want to check: "))

print(check_leap_year(year))