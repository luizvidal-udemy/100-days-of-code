import prettytable  

a = prettytable.PrettyTable()


a.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
a.add_column("Type", ["Electric", "Water", "Fire"])

print(a)    