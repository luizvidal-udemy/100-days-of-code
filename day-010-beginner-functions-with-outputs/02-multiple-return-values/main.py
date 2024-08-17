def format_name(f_name: str, l_name: str) -> str:
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    return f"{f_name.title()} {l_name.title()}"


print(
    format_name(
        input("What is your first name? "),
        input("What is your last name? ")
    )
)
