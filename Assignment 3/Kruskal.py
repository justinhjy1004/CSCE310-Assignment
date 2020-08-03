import graph_representation as gr

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

# Edge representation for Graph
# Since it is undirected, node_1 and node_2 are not arranged in any order
# Holds a weight value and sorts by weight
# Holds metadata for included (Kruskal, Prim and Djikstra's?)
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

# Graph representation
# Undirected but weighted
# Contains list of nodes and list of edges
# Primary representation using adjacency list
# Node values are assumed to be integers
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

    # given value of node, locate the address of the node holding the value
    def get_node(self, value):
        for n in self.nodes:
            if n.get_value() == value:
                return n

    def add_edge(self, value_1, value_2, weight):
        node1 = self.get_node(value_1)
        node2 = self.get_node(value_2)
        e = Edge(node1,node2,weight)
        self.edges.append(e)
        self.adj_list[node1].append((node2, weight))
        self.adj_list[node2].append((node1, weight))

    # given node value, get node address and returns all edges of the node
    def get_edges(self, value):
        node = self.get_node(value)
        edges = []
        for e in self.edges:
            if node == e.get_nodes()[0] or node == e.get_nodes()[1]:
                edges.append(e)

        return edges

    # gets neighbours of node given node value
    def neighbour(self, value):
        node = self.get_node(value)
        neighbour_node = []
        for n in self.adj_list[node]:
            neighbour_node.append(n[0])

        return neighbour_node

    def reset(self):
        for n in self.nodes:
            n.reset()
        for e in self.edges:
            e.reset()

    # prints adjacency list of graph
    def print(self):
        for u in self.nodes:
            print("%d --> " % u.get_value(), end = '')
            for v in self.adj_list[u]:
                print("%d" % v[0].get_value(), end = ' ')
            print()

def cycle_detection(edge, cycle_set):

    u = edge.get_nodes()[0].get_value()
    v = edge.get_nodes()[1].get_value()
    if not(u in cycle_set and v in cycle_set):
        cycle_set.add(u)
        cycle_set.add(v)
        return False
    else:
        return True



def Kruskal(graph:gr.Graph):
    edge_list = sorted(graph.get_edge_list())
    weight = 0
    k = 1
    x = edge_list[0].get_nodes()[0].get_value()
    y = edge_list[0].get_nodes()[1].get_value()
    w = edge_list[0].get_weight()
    cycle_set ={x,y}
    edge_set = {(x,y,w)}
    weight = w
    while len(edge_set)< graph.num_vertices() - 1:
        u = edge_list[k].get_nodes()[0].get_value()
        v = edge_list[k].get_nodes()[1].get_value()
        w = edge_list[k].get_weight()
        if not cycle_detection(edge_list[k], cycle_set):
            edge_set.add((u,v,w))
            weight += w
        k += 1

    return (weight, edge_set)

if __name__ == "__main__":
    g = gr.parse_graph("input002.txt")
    k = Kruskal(g)
    print(k)
