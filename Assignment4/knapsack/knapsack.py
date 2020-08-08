'''
Abby Seibel and Justin Ho
CSCE 310
Assignment 4 Knapsack Dynamic Programing
'''

import sys

# takes in a file, pareses it, and creates a matrix that is n+1 x weight+1 and fills it with empty zeros
#returns a triple of the empty matrix, an array of weights, and an array of values
#the index in the value and weight array corrospond to the object
def table_setup(fileName):
    f = open(fileName, 'r')
    num_and_weight = f.readline().strip().split(' ')
    numObjects = int(num_and_weight[0])
    capacity = int(num_and_weight[1])
    weights = [int(x) for x in f.readline().strip().split(' ')]
    values = [int(x) for x in f.readline().strip().split(' ')]

    table=[]
    for i in range(numObjects+1):
        table.append([])
        for j in range(capacity+1):
            table[i].append(0)
    f.close()

    return (table, weights, values)


#given a table, and the list of items and their weights and values it creates a
#table, and then outputs the set of a optimal solution
def dynamic_knapsack(table, weights, values):
    optimal = set()
    for i in range(len(table)):
        for j in range(len(table[i])):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif j - weights[i-1] < 0:
                table[i][j] = table[i-1][j]
            else:
                takeItem = table[i-1][j-weights[i-1]] + values[i-1]
                leaveItem = table[i-1][j]
                table[i][j] = max(takeItem, leaveItem)


    i = len(table)-1
    j = len(table[i])-1

    print("Tableau:")
    for t in table:
        print(t)

    og_knapsack = set()
    for element in range(1, len(weights) + 1):
        og_knapsack.add((element, weights[element-1], values[element-1]))

## this section explores the code to find what items to steal
    optimal_weight = 0
    while i >= 1 and j >= 1:
        while i >= 1 and table[i][j] == table[i-1][j]:
            i -=1
        if(i>=1):
            optimal.add((i,values[i-1], weights[i-1]))
            optimal_weight += weights[i-1]
            j = j - weights[i-1]
            i-=1

    print("Maximum Capacity: W = %d" % len(table[0]))
    print("Optimal Weight: %.2f" % optimal_weight)
    print("Optimal Value: %.2f" %table[len(table)-1][len(table[0])-1])
    print("Original Knapsack Items: " + str(og_knapsack))
    print("Optimal Knapsack Items: " + str(optimal))

if __name__ == "__main__":
    filename = "input001.txt"
    prepared_table = table_setup(filename)
    table = prepared_table[0]
    weight_array = prepared_table[1]
    value_array = prepared_table[2]

    dynamic_knapsack(table, weight_array, value_array)


