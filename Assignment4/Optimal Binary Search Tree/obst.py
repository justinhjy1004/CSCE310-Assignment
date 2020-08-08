'''
Abby Seibel and Justin Ho
CSCE 310
Assignment 4 Optimal Binary Search Tree
'''

import sys

# Node Construction for OBST
class Node(object):
    def __init__(self, key, probability):
        self.key = key
        self.prob = probability
        self.parent = None
        self.left = None
        self.right = None

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.right = right

    def get_right(self):
        return self.right

    def get_key(self):
        return self.key

    def get_probability(self):
        return self.prob

# Class that contains all information pertaining to OBST
class obst_tableu(object):
    def __init__(self, n, dict, node_list):
        self.tableu = []
        self.root_tableu = []
        self.n = n
        self.dict = dict
        self.node_list = node_list

        for i in range(n+1):
            self.tableu.append([])
            for j in range(n+1):
                self.tableu[i].append(None)

        for i in range(n):
            self.root_tableu.append([])
            for j in range(n):
                self.root_tableu[i].append(None)

        for i in range(1, n+2):
            self.set_cost(i, i - 1, 0)

        for i in range(1, n+1):
            self.set_cost(i, i, dict[i][1])

        for i in range(1,n+1):
            self.set_root(i, i, i)

    def set_cost(self, i, j, value):
        self.tableu[i-1][j] = value

    def get_cost(self, i, j):
        return self.tableu[i-1][j]

    def get_root(self, i, j):
        return self.root_tableu[i-1][j-1]

    def set_root(self, i, j, value):
        self.root_tableu[i-1][j-1] = value

    def calc_table(self):
        for d in range(1,self.n):
            for i in range(1, self.n + 1 - d):
                j = i + d
                min = float('inf')
                sum = 0
                for k in range(i, j+1):
                    q = self.get_cost(i, k - 1) + self.get_cost(k + 1, j)
                    sum += self.dict[k][1]
                    if q < min:
                        min = q
                        self.set_root(i,j,k)
                self.set_cost(i, j, min + sum)

    def print_cost(self):
        print('Cost Tableu')
        for r in self.tableu:
            print("[", end='')
            for e in r:
                if e is None:
                    print(None, end = '  ')
                else:
                    print("%.3f" % e, end = ' ')
            print("]", end='')
            print()
        print()

    def print_root(self):
        print('Root Tableu')
        for r in self.root_tableu:
            print("[", end='')
            for e in r:
                if e is None:
                    print(None, end='  ')
                else:
                    print("%4d" % e, end='  ')
            print("]", end='')
            print()
        print()

    def tree_construction(self):
        root = self.node_list[self.get_root(1,n)]
        stack = []
        stack.append((root, 1, self.n))
        while len(stack) != 0:
            data = stack.pop()
            u = data[0]
            i = data[1]
            j = data[2]
            k = self.get_root(i,j)
            if k < j:
                v = self.node_list[self.get_root(k+1,j)]
                u.set_right(v)
                v.set_parent(u)
                stack.append((v,k+1,j))
            if i < k:
                v = self.node_list[self.get_root(i,k-1)]
                u.set_left(v)
                v.set_parent(u)
                stack.append((v,i,k-1))
        return root

# parse file according to requirements
def parse_file(file):
    f = open(file, "r")

    dict = {}

    order_list = []

    num_elem = int(f.readline().strip())

    for i in range(num_elem):
        data = f.readline().split()
        order_list.append((data[0].strip(), float(data[1].strip())))

    order_list = sorted(order_list)

    for i in range(num_elem):
        dict[i+1] = order_list[i]

    return (dict, int(num_elem))

if __name__ == "__main__":
    file = sys.argv[1]

    data = parse_file(file)
    dict = data[0]
    n = data[1]

    node_list = {}

    for i in range(1,n+1):
        node = Node(dict[i][0], dict[i][1])
        node_list[i] = node

    tab = obst_tableu(n, dict, node_list)
    tab.calc_table()
    root = tab.tree_construction()
    tab.print_cost()
    tab.print_root()

    for i in range(1, n+1):
        print("Node")
        node = node_list[i]
        print("\tKey: %s" % node.get_key())
        print("\tProbability: %.1f%s" % (node.get_probability()*100, "%"))

        if node.get_parent() == None:
            print("\tParent: %s" % None)
        else:
            print("\tParent: %s" % node.get_parent().get_key())

        if node.get_left() == None:
            print("\tLeft Child: %s" % None)
        else:
            print("\tLeft Child: %s" % node.get_left().get_key())

        if node.get_right() == None:
            print("\tRight Child: %s" % None)
        else:
            print("\tRight Child: %s" % node.get_right().get_key())


