
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Aliccce', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'mooose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)
    for i in range(len(table)):
        colWidths[i] = len(max(table[i], key=len))

    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(colWidths[y]), end = ' ')
        print("")
        
        
printTable(tableData)
