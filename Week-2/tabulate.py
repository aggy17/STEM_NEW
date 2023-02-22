from prettytable import PrettyTable
#specify column names
myTable = PrettyTable(["names","city"])
#add rows
myTable.add_row (["agnes","sydney"])
myTable.add_row(["ramsey","nairobi"])
myTable.add_row(["emma","nakuru"])
print(myTable)
 