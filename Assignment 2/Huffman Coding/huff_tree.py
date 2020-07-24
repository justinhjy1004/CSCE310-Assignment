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
