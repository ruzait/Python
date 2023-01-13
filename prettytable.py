from prettytable import PrettyTable


#IF you use rows:
        #Creat column names
    #myTable = PrettyTable(['Student_Name', 'Class', 'Index'])

        #Add rows
    #myTable.add_row(['Ruzait', 'E-Tech', '11983'])
    #myTable.add_row(['Afnan', 'E-Tech', '11971'])
    #myTable.add_row(['Ijas', 'E-Tech', '12452'])
    #myTable.add_row(['Reef', 'E-Tech', '13584'])
    #myTable.add_row(['Naji', 'E-Tech', '91285'])


#IF you use columns:

    #myTable = PrettyTable()
    #columns = ['Student_Name', 'Class', 'Index']

    #myTable.add_column(columns[0], ["ru"])
    #myTable.add_column(columns[1], ["A"])
    #myTable.add_column(columns[2], ["11983"])

# Creat column names
myTable = PrettyTable(['Student_Name', 'Class', 'Index'])

# Add rows
myTable.add_row(['Ruzait', 'E-Tech', '11983'])
myTable.add_row(['Afnan', 'E-Tech', '11971'])
myTable.add_row(['Ijas', 'E-Tech', '12452'])
myTable.add_row(['Reef', 'E-Tech', '13584'])
myTable.add_row(['Naji', 'E-Tech', '91285'])
myTable.add_autoindex('Sr_No')

print(myTable)
# myTable.del_row(2)
# myTable.del_column('Class')
# myTable.clear()
# myTable.clear_rows()