import math
import sys

class matrix(object):
    def __init__(self, row , col):
        self.grid = []
        # initialize matrix with 0 as values
        for i in range(row):
            self.grid.append([])
            for j in range(col):
                self.grid[i].append(0)

    # given row and column, input value would be set
    def set(self, row, col, val):
        self.grid[row][col] = val

    # gets value from given row and column
    def get(self, row, col):
        return(self.grid[row][col])

    # obtains the whole row for elementary row operations
    def get_row(self, row):
        return(self.grid[row])

    # sets the whole row for elementary row operations
    def set_row(self, row, val):
        self.grid[row] = val

    # returns the dimension of the matrix (augmented included)
    def dim(self):
        return(len(self.grid), len(self.grid[0]))

    # returns the augmented column of the matrix
    def aug_col(self):
        aug_col = []
        for i in self.grid:
            aug_col.append(i[self.dim()[1] - 1])

        return aug_col

    # print the matrix for visualization
    def print(self):
        for i in range(len(self.grid)):
            for j in self.grid[i]:
                print("%.3f" % j, end = '\t')
            print()

# construct matrix given input file
def construct_matrix(file):
    f = open(file, 'r')

    # get dimensions for initialization
    dimensions = int(f.readline().strip())

    # additional column for augmented matrix
    m = matrix(dimensions,dimensions+1)

    # set values for matrix
    for i in range(dimensions):
        row = f.readline().strip().split(' ')
        for r in range(len(row)):
            m.set(i, r, float(row[r]))

    aug_col = f.readline().strip().split(' ')

    # set values for augmented column
    for i in range(len(aug_col)):
        m.set(i, dimensions, float(aug_col[i]))

    return m

def upper_triangularization(matrix):

    for i in range(matrix.dim()[0]-1):
        # set pivot value to be larger values
        pivot_row = i
        for j in range(i,matrix.dim()[1]-1):
            if math.fabs(matrix.get(j,i)) > math.fabs(matrix.get(pivot_row, i)):
                pivot_row = j

        # exchange rows for matrix
        temp_row = matrix.get_row(i)
        matrix.set_row(i, matrix.get_row(pivot_row))
        matrix.set_row(pivot_row, temp_row)

        # row reductions
        for j in range(i,matrix.dim()[0]-1):
            # obtain coefficient for row reduction
            if matrix.get(i,i) == 0:
                coeff = 0
            else:
                a = matrix.get(j+1,i)
                b = matrix.get(i,i)
                coeff = a / b

            # compute row reduced values
            for k in range(i, matrix.dim()[1]):
                new_val = matrix.get(j+1,k) - matrix.get(i,k)*coeff
                matrix.set(j+1,k,new_val)

    return matrix

# perform backward substitution on upper triangularized matrix
def backward_substitution(matrix):
    for i in range(matrix.dim()[0]):
        # get the pivot and augmented value starting from the last row
        pivot = matrix.get(matrix.dim()[0] - i - 1, matrix.dim()[0] - i - 1)
        aug_val = matrix.get(matrix.dim()[0] - i - 1, matrix.dim()[1] - 1)
        # Assessment of the type of solution
        if pivot == 0:
            if aug_val == 0: # Infinitely many solutions
                print("This linear system has infinitely many solutions!")
                return 1
            else: # inconsistent linear system
                print("This linear system has no solutions!")
                return 1

        # normalize values
        matrix.set(matrix.dim()[0] - i - 1, matrix.dim()[0] - i - 1, 1)
        norm_aug_val = aug_val / pivot
        matrix.set(matrix.dim()[0] - i - 1, matrix.dim()[1] - 1, norm_aug_val)

        # perform backward substitution starting from the pivot value of the last row
        for j in range(matrix.dim()[0] - 1 - i):
            coeff = matrix.get(j, matrix.dim()[0] - i - 1)
            matrix.set(j, matrix.dim()[0] - i - 1, 0)
            new_aug_val = matrix.get(j, matrix.dim()[1] - 1) - norm_aug_val*coeff
            matrix.set(j, matrix.dim()[1] - 1, new_aug_val)

    return matrix

# Perform Gaussian Elimination with two-step process
# 1. Upper Triangularization
# 2. Backward Substitution
# Return 1 if unsuccessful in obtaining a solution
def gauss_elim(matrix):

    upper_triangularization(matrix)
    flag = backward_substitution(matrix)

    if flag != 1:
        flag = 0

    return flag


if __name__ == "__main__":
    file = sys.argv[1]

    matrix = construct_matrix(file)

    if gauss_elim(matrix) == 0:
        for i in matrix.aug_col():
            print("%.3f" % i, end = ' ')