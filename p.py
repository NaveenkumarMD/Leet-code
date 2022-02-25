from prettytable import PrettyTable

#create a sample tableof names and age
table = PrettyTable(["Name", "Age"])
table.add_row(["Johndddddddddddddddddddddd", "18"])
table.add_row(["Bob", "20"])
table.add_row(["Marry", "17"])
print(table)
