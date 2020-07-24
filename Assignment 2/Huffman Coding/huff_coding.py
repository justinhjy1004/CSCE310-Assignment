# Abby Seibel and Justin Ho
# CSCE 310 Summer course
# Program C

import sys
import heapq as hq

class Node(object):
    def __init__(self, value, parent=None, left_child=None, right_child=None):
        self.value = value
        self.parent = parent
        self.left = left_child
        self.right = right_child

    def is_root(self):
        if self.parent == None:
            return True
        else:
            False

    def has_left_child(self):
        if self.left == None:
            return False
        else:
            return True

    def has_right_child(self):
        if self.left == None:
            return False
        else:
            return True

    def get_left_child(self):
        if self.has_left_child():
            return self.left
        else:
            return None

    def get_right_child(self):
        if self.has_left_child():
            return self.left
        else:
            return None

    def get_parent(self):
        if not self.is_root():
            return self.parent
        else:
            return None

    def get_val(self):
        return self.value

    def set_val(self, value):
        self.value = value

    def set_parent(self, parent):
        self.parent = parent

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def __eq__(self, other):
        if self.get_val() == other.get_val():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.get_val() < other.get_val():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.get_val() > other.get_val():
            return True
        else:
            return False

    def __le__(self, other):
        if self.get_val() <= other.get_val():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.get_val() >= other.get_val():
            return True
        else:
            return False

class CodeNode(Node):
    def __init__(self, value, code, parent=None, left_child=None, right_child=None):
        self.value = value
        self.code = code
        self.parent = parent
        self.left = left_child
        self.right = right_child

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

class Huff_Tree(object):
    def __init__(self, root):
        self.root = root

    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def __eq__(self, other):
        if self.root.get_val() == other.root.get_val():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.root.get_val() < other.root.get_val():
            return True
        else:
            return False

    def __le__(self, other):
        if self.root.get_val() <= other.root.get_val():
            return True
        else:
            return False

    def get_leaves(self):

    def in_order_traversal(self, next_node, leaves = []):

def parse_text(file, char_composition):
    f = open(file, 'r', encoding="utf-8")

    num_char = 0

    while 1:

        # read by character
        char = f.read(1)

        if not char:
            break

        num_char = num_char + 1

        if char not in char_composition.keys():
            char_composition[char] = 1
        else:
            char_composition[char] = char_composition.get(char) + 1

    for char in char_composition.keys():
        char_composition[char] = char_composition.get(char)/num_char

    f.close()

    return num_char

def construct_huffman_tree(char_composition):
    heap = []

    for key, value in char_composition.items():
        node = CodeNode(value=value, code=key)
        tree = Huff_Tree(node)
        hq.heappush(heap, tree)

    while len(heap) > 1:
        a = hq.heappop(heap)
        b = hq.heappop(heap)

        wt_node = Node(value = a.get_root().get_val() + b.get_root().get_val(), left_child = a, right_child = b)
        a.get_root().set_parent(wt_node)
        b.get_root().set_parent(wt_node)

        new_tree = Huff_Tree(wt_node)
        hq.heappush(heap, new_tree)

    return hq.heappop(heap)

if __name__ == "__main__":

    char_composition = {}
    num_char = parse_text("input001.txt", char_composition)

    print(len(char_composition))

    huff_t = construct_huffman_tree(char_composition)

    print(huff_t.get_root().get_val())


