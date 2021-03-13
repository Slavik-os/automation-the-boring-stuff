import pprint
tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
   for rows in range(len(table)):
       for columns in range(len(table)):
           print(table[rows][columns].rjust(10),end="")
       print('')

           
          
       

    


printTable(tableData)