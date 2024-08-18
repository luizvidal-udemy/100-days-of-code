"""day-012-beginner-scope-and-number-guessing-game/03-prime-number-checker"""


def is_prime(number: int) -> bool:
    """A function that checks if a number is prime"""
    divisors = 0

    for index in range(1, number + 1):
        if number % index == 0:
            divisors += 1

    if divisors == 2:
        return True

    return False


print(is_prime(75))
