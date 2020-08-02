# Abby Seibel and Justin Ho
# CSCE310
# Assignment 2 Problem C
# Huffman Coding

import sys
import heapq as hq

# This class holds the node of a tree, and has the ways to access the node and the nodes connected to it
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


# The tree class holds a root of a Huffman Tree
class Tree(object):
    def __init__(self):
        self.root = Node(None, 0)

    # this function sets the root of the tree
    def setRoot(self,root):
        self.root = root

    def getRootWeight(self):
        return self.root.getWeight()

    def setRootWeight(self, weight):
        self.root.weight = weight

    # comparator operators
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
# returns a tuple containing frequency of characters and number of total characters
def parse_text(file):
    count = 0
    f = open(file, "r", encoding = "utf-8")

    dictionary = {}

    # counts the number of occurences of each character, and only puts present characters into the dictionary
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

    # calculates the frequency ratio of each element in the dictionary
    for key in dictionary:
        dictionary[key] = dictionary[key]/count

    return (dictionary, count)

# Input: dictionary containing letters and the relative frequency in the file
# Output: Huffman Tree
def construct_tree(frequency):

    heap = []

    # add single Node Huffman Tree into Heap
    for key in frequency:
        singleNodeTree = Tree()
        singleNodeTree.setRoot(Node(frequency[key], key))
        hq.heappush(heap, singleNodeTree)

    # combine Huffman Trees into a single Huffman tree
    while len(heap) > 1:
        T_r = Tree()
        a = hq.heappop(heap)
        b = hq.heappop(heap)
        T_r.root.setLeftChild(a.getRoot())
        T_r.root.setRightChild(b.getRoot())
        T_r.setRootWeight(a.getRootWeight() + b.getRootWeight())
        hq.heappush(heap, T_r)

    return hq.heappop(heap)

<<<<<<< HEAD
=======

>>>>>>> 582de321aae6f47f52385b105589b0e2abbccdd9
# Input: Huffman Tree
# Output: dictionary with code words
# Using a recursive call, perform in order traversal to obtain a dictionary of codewords
def code_builder(huffman_tree):
    codeWords = {}
    root = huffman_tree.getRoot()
    currentCode = ''

    code_builder_recursive(root, currentCode, codeWords)

    return codeWords

# Recursive algorithm to build dictionary of code word
def code_builder_recursive(root, currentCode, codeWords):
    if root == None:
        return

    if root.getChar() != None:
        codeWords[root.getChar()] = currentCode

    code_builder_recursive(root.getLeftChild(), currentCode + "0", codeWords)
    code_builder_recursive(root.getRightChild(), currentCode + "1", codeWords)

# INPUT: frequency dictionary, code words dictionary and number of total characters
# OUTPUT: prints compression information in standard output
def print_output(frequency, codeWords, num_char):
    headline = "Character".rjust(9) + "Codeword".rjust(25) + "Frequency".rjust(15)
    print(headline)

    avg_codeWord_len = 0

    for charVal in frequency.keys():
        charVal_formatted = repr(charVal).rjust(9)
        codeWords_formatted = str(codeWords[charVal]).rjust(25)
        freq_formatted = str(str(round(frequency[charVal]*100,4)) + '%').rjust(15)
        print(charVal_formatted + codeWords_formatted + freq_formatted)
        avg_codeWord_len = avg_codeWord_len + len(codeWords[charVal]) * frequency[charVal]

    og_size = num_char * 8
    encoded_size = num_char * avg_codeWord_len
    ratio = round((avg_codeWord_len/8)*100, 3)

    print()
    print("Average Codeword Length: %.3f bits" % avg_codeWord_len)
    print("Original Size (bits): %d " % og_size)
    print("Encoding Size (bits): %.0f" % encoded_size)
    print("Compression Ratio: %.3f" % ratio + "%")

if __name__ == "__main__":

    # parse text
    text_info = parse_text(sys.argv[1])

    # frequency dictionary
    frequency = text_info[0]

    # number of characters in text file
    num_char = text_info[1]

    # Obtain Huffman Tree
    codeTree = construct_tree(frequency)

    # codeword dictionary
    codeWords = code_builder(codeTree)

    print_output(frequency, codeWords, num_char)

