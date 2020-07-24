# Abby Seibel and Justin Ho
#CSCE 310
# Assigment 2 problem C
# Huffing coding
import sys

from heapq import heapify, heappush, heappop

#This class holds the node of a tree, and has the ways to access the node and the nodes connected to it
class Node(object):
    def __init__(self, weight, charVal):
        self.left = None
        self.right= None
        self.parent = None
        self.weight = weight
        self.charVal = charVal

    def setRightChild(self, rightChild):
        self.right=rightChild

    def setLeftChild(self, leftChild):
        self.left = leftChild

    def setParent(self, parent):
        self.parent = parent

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def getParent(self):
        return self.parent

    def getWeight(self):
        return self.weight



# The tree class holds a root of the tree
class Tree(self):
    def __init__(self)

# this funciton opens the file, and then creates an dictionary that maps the characters with their frequecy in the file
def parse_text(file):
    count = 0
    f = open(file, "r")

    dictionary = {}
    #counts the number of occurances of each character, and only puts present characters into the dictionary
    while 1:
        c = f.read(1)
        if not c:
            break
        count += 1
        if dictionary.get(c) is not None:
            dictionary[c]+=1
        else:
            dictionary[c] = 1
    f.close()

    #calculautes the frequecy ratio of each element in the dictionary
    for key in dictionary:
        dictionary[key] = dictionary[key]/count

    return dictionary


if __name__ == "__main__":
    frequency = parse_text(sys.argv[1])
