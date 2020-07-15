'''
Defining Graph Data Structure
'''

class Vertex(object):
    def __init__(self, val):
        self.val = val

    def get_val(self):
        return self.val

    def __str__(self):
        return(self.get_val())

class Edge(object):
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination

class Digraph(object):
    def __init__(self):
        self.edges = {}

    def add_vertex(self, vertex):
        if vertex not in self.edges:
            self.edges[vertex] = []

    def add_edge(self, edge):
        if not (edge.get_source() in self.edges and edge.get_destination() in self.edges):
            raise ValueError('Vertices not in graph')
        self.edges[edge.get_source()].append(edge.get_destination())

    def children_of(self, vertex):
        return self.edges[vertex]

    def has_vertex(self, vertex):
        return vertex in self.edges

    def get_vertex(self, val):
        for v in self.edges:
            if v.get_val() == val:
                return v
        raise NameError(val)

    def get_all_vertices(self):
        return self.edges.keys()

    def get_all_edges(self):
        return self.edges.values()

class Graph(Digraph):
    def add_edge(self, edge):
        if not (edge.get_source() in self.edges and edge.get_destination() in self.edges):
            raise ValueError('Vertices not in graph')
        self.edges[edge.get_source()].append(edge.get_destination())




