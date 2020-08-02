class Node(object):
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.processed = False
        self.time_visited = None
        self.time_processed = None

    def get_value(self):
        return self.value

    def is_visited(self):
        return self.visited

    def is_processed(self):
        return self.processed

    def visit(self):
        self.visited = True

    def process(self):
        self.processed = True

    def set_time_processed(self, time):
        self.time_processed = time

    def set_time_visited(self, time):
        self.time_visited = time

    def get_time_visited(self):
        return self.time_visited

    def get_time_processed(self):
        return self.time_processed

    def reset(self):
        self.visited = False
        self.processed = False
        self.time_visited = None
        self.time_processed = None

    def __le__(self, other):
        if self.value <= other.value:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.value >= other.value:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.value < other.value:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        else:
            return False


class Edge(object):
    def __init__(self, node_1, node_2, weight):
        self.node_1 = node_1
        self.node_2 = node_2
        self.weight = weight
        self.included = False

    def get_nodes(self):
        return (self.node_1, self.node_2)

    def get_weight(self):
        return self.weight

    def is_included(self):
        return False

    def include(self):
        self.included = True

    def reset(self):
        self.included = False

    def __eq__(self, other):
        if self.weight == other.weight:
            return True
        else:
            return False

    def __le__(self, other):
        if self.weight <= other.weight:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.weight >= other.weight:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.weight < other.weight:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.weight > other.weight:
            return True
        else:
            return False

class Graph(object):
    def __init__(self, num_vertices):
        self.nodes = []
        self.adj_list = {}
        for i in range(num_vertices):
            node = Node(i)
            self.nodes.append(node)
            self.adj_list[node] = []
        self.edges = []

    def num_vertices(self):
        return len(self.nodes)

    def get_node_list(self):
        return self.nodes

    def get_edge_list(self):
        return self.edges

    def get_node(self, value):
        for n in self.nodes:
            if n.get_value() == value:
                return n

    def add_edge(self, v1, v2, weight):
        node1 = self.get_node(v1)
        node2 = self.get_node(v2)
        e = Edge(node1,node2,weight)
        self.edges.append(e)
        self.adj_list[node1].append((node2, weight))
        self.adj_list[node2].append((node1, weight))

    def get_edges(self, v1):
        node = self.get_node(v1)
        edges = []
        for e in self.edges:
            if node == e.get_nodes()[0] or node == e.get_nodes()[1]:
                edges.append(e)

        return edges

    def neighbour(self, v):
        node = self.get_node(v)
        neighbour_node = []
        for n in self.adj_list[node]:
            neighbour_node.append(n[0])

        return neighbour_node

    def reset(self):
        for n in self.nodes:
            n.reset()
        for e in self.edges:
            e.reset()

    def print(self):
        for u in self.nodes:
            print("%d --> " % u.get_value(), end = '')
            for v in self.adj_list[u]:
                print("%d" % v[0].get_value(), end = ' ')
            print()

def parse_graph(file):
    f = open(file, "r")
    num_vertices = int(f.readline().strip())

    g = Graph(num_vertices)

    line = f.readline()

    while line != '':
        data = line.split(' ')
        g.add_edge(int(data[0].strip()), int(data[1].strip()), float(data[2].strip()))
        line = f.readline()

    return g

if __name__ == "__main__":
    g = parse_graph("input001.txt")
    g.print()