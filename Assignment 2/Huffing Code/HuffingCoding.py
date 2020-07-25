# Abby Seibel and Justin Ho
#CSCE 310
# Assigment 2 problem C
# Huffing coding
import sys

import heapq as hq

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

    def getChar(self):
        return self.charVal



# The tree class holds a root of the tree
class Tree(object):
    def __init__(self):
        self.root = Node(None, 0)

    #this function sets the root of the tree
    def setRoot(self,root):
        self.root = root

    def getRootWeight(self):
        return self.root.getWeight()

    def setRootWeight(self, weight):
        self.root.weight = weight

    def __eq__(self, other):
        if self.root.getWeight() == other.root.getWeight():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.root.getWeight() < other.root.getWeight():
            return True
        else:
            return False

    def __le__(self, other):
        if self.root.getWeight() <= other.root.getWeight():
            return True
        else:
            return False

    def getRoot(self):
        return self.root



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


def construct_tree(frequency):

    heap = []

    for key in frequency:
        singleNodeTree = Tree()
        singleNodeTree.setRoot(Node(frequency[key], key))
        hq.heappush(heap, singleNodeTree)

    while len(heap) > 1:

        T_r = Tree()
        a = hq.heappop(heap)
        b = hq.heappop(heap)
        T_r.root.setLeftChild(a.getRoot())
        T_r.root.setRightChild(b.getRoot())
        T_r.setRootWeight(a.getRootWeight() + b.getRootWeight())
        hq.heappush(heap, T_r)

    return hq.heappop(heap)


def tree_walk(codeTree):
    stack = []
    stackString = []
    codeWords = {}
    current = codeTree.getRoot()


    while len(stack)>0 or current is not None:
        if current is not None and current.getChar() == 0:
            stack.append(current)
            current = current.getLeftChild()
            stackString.append(0)
        else:

            if current.getChar() != 0:
                tempString = ""
                for i in range (len(stackString)):
                    tempString = tempString + str(stackString[i])
                codeWords[current.getChar()] = tempString
            if len(stack)>0:
                current = stack.pop()
            if stackString[len(stackString)-1]  == 1 and len(stackString) > 1:
                stackString.pop()
                stackString.pop()
            else:
                stackString.pop()
            current = current.getRightChild()
            stackString.append(1)
    return codeWords




if __name__ == "__main__":

    frequency = parse_text(sys.argv[1])

    print(frequency)



    codeTree = construct_tree(frequency)
    codeWords = tree_walk(codeTree)

    print(codeWords)
