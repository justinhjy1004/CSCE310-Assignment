'''
Abby Seibel and Justin Ho
CSCE 310
Assignment 4 Non-Contiguous Palindrome Dynamic Programing
'''

import sys

def parse_file(file):

    f = open(file, "r")

    sequence = f.readline().strip()

    tableu = []
    for i in range(len(sequence)):
        tableu.append([])
        for j in range(len(sequence)):
            tableu[i].append(1) # initialize tableu with 0

    return (tableu, sequence)

def dynamic_tableu(tableu, sequence):
    n = len(sequence)
    # fills the table diagonally
    for elem in range(0,n):
        i = 0
        j = elem + 1
        while j < n: # iterate the values diagonally
            if sequence[i] == sequence[j]: # if a repeated character is found
                if j + 1 - i == 2: # if left bottom diagonal value is 1 set to 2
                    tableu[i][j] = 2
                else: # add 2 to the existing palindrome subsolution
                    tableu[i][j] = tableu[i+1][j-1] + 2
            else: # if not the same, choose the max between the bottom or top cell
                tableu[i][j] = max(tableu[i][j-1], tableu[i+1][j])
            i += 1
            j += 1

    return tableu

def construct_palindrome(sequence, tableu):
    n = len(sequence)
    palindrome_beginning = []
    palindrome_end = []

    value = tableu[0][n-1]
    for i in range(n-1):
        j = tableu[i].index(value)
        if tableu[i][j] != tableu[i+1][j]:
            value = tableu[i+1][j-1]

            diff = tableu[i][j] - value
            if diff == 2:
                palindrome_beginning.append(sequence[j])
                palindrome_end.insert(0,sequence[j])
                if tableu[i][j] == 3:
                    palindrome_beginning.append(sequence[j-1])
            if diff == 1:
                palindrome_beginning.append(sequence[j])
                if tableu[i][j] == 2:
                    palindrome_end.insert(0, sequence[j])

            if value == 1:
                break

    palindrome_list = palindrome_beginning + palindrome_end

    palindrome = ''

    for p in palindrome_list:
        palindrome += p

    return palindrome

if __name__ == "__main__":
    file = sys.argv[1]

    output = parse_file(file)

    tableu = output[0]
    sequence = output[1]

    tableu = dynamic_tableu(tableu, sequence)

    palindrome = construct_palindrome(sequence, tableu)

    print("Original Word: " + sequence)
    print("Palindrome: " + palindrome)
    print("Length: %d" % len(palindrome))



