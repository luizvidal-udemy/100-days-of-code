def format_name(f_name: str, l_name: str) -> str:
    """Take a first and last name and format it to return the title case version of the name."""
    return f"{f_name.title()} {l_name.title()}"


print(format_name("luiZ", "VIdaL"))
