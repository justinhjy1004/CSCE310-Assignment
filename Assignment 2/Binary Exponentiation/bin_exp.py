#Abby Seibel and Justin Ho
# CSCE 310 Summer course
# Program A

import sys

def bin_exp(a, n, m):
    # return corner case where n = 0
    if n == 0:
        return 1

    bit_str_n = "{0:b}".format(n)

    # initialize term
    term = a
    solution = 1

    if bit_str_n[len(bit_str_n) - 1] == '1':
        solution = a

    # traverse from the second last to the first bit string
    for i in range(len(bit_str_n)-1):
        term = (term * term) % m
        if bit_str_n[len(bit_str_n) - 2 - i] == '1': # if bit value is 1, multiply to the solution
            solution = (solution * term) %m

    return solution

def bin_exp_2(a,n,m):
    term = a
    if(n&1):
        solution =a
    else:
        solution = 1

    while n > 0:
        n = n >> 1
        term = (term * term) % m
        if (n & 1):
            solution = (solution * term) % m

    return solution

if __name__ == "__main__":

    a = int(sys.argv[1])
    n = int(sys.argv[3])
    m = int(sys.argv[2])

    # print(bin_exp_2(a,n,m))

    print(bin_exp(a,n,m))
