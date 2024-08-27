from prettytable import PrettyTable, PLAIN_COLUMNS, MSWORD_FRIENDLY, ORGMODE, SINGLE_BORDER, DOUBLE_BORDER

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])

table.set_style(SINGLE_BORDER)
table.align = "l"

print(table)
