from art import logo

def calculate(first_number: float, second_number: float, operation: str) -> float:
    result = 0

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    else:
        result = first_number / second_number

    print(f"{first_number} {operation} {second_number} = {result}")

    return result


previous_result = None

while True:
    print(logo)
    first_number = 0

    if previous_result == None:
        first_number = float(input("What's the first number?: "))
    else:
        first_number = previous_result

    operation = input("+\n-\n*\n/\nPick an operation: ")
    next_number = float(input("What's the next number?: "))
    previous_result = calculate(first_number, next_number, operation)

    start_new = input(
        f"Type 'y' to continue calculating with {previous_result}, or type 'n' to start a new calculation: "
    ).lower() == 'n'

    if start_new:
        print("\n" * 100)
        previous_result = None
