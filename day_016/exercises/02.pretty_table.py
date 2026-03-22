# Create a PrettyTable object and save it to a variable called table
from prettytable import PrettyTable

table = PrettyTable()

# Fill the table with pokemon data

table.add_column("Pokemon Name",
["Pikachu", "Squirtle", "Charmander"],
                 'l'
)
table.add_column("Type",
    ["Electric","Water","Fire"],
                 'l'
    )

print(table)