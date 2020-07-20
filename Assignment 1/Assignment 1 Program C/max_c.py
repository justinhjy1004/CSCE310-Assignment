# Authors: Justin Ho and Abby Seibel
# Assignment 1C Max cliques

from copy import deepcopy
import sys

# Graph data structure
class Graph(object):
    def __init__(self, vertex_num):
        self.graph = {}  # graph is a dict, with the key as the vertex and the value as the edges in the form of a list
        self.vertex_num = vertex_num

    def add_vertex(self, v):
        if v not in self.graph.keys():
            self.graph[v] = []  # new vertex, avoid repeating vertex

    def add_edges(self, v, e):
        self.graph[v].append(e)

# Construct a graph given an input file with a specific format
def construct_graph(file):
    f = open(file, "r")
    num_lines = int(f.readline()) # reads the number of lines in the file

    g = Graph(num_lines)

    for n in range(num_lines):
        adj_list = f.readline().strip().split(' ')
        g.add_vertex(int(adj_list[0])) # adds the first number as vertex
        for i in range(1, len(adj_list)):
            g.add_edges(int(adj_list[0]), int(adj_list[i])) # adds subsequent numbers as edges

    return g


## max_clique is given a graph, and then returns a list of solutions of all the cliques in the Graph
def max_clique(g, original, subset, index, solutions):
    for i in range(index+1, len(original)):
        isClique = True
        deepCopy = deepcopy(subset)
        for v in deepCopy:
            #checks that the element of the graph that may be added has at least 1 edge that connects it to v
           if original[i] not in g.graph.get(v,[]) and v not in g.graph.get(original[i],[]) :
               isClique = False
        if isClique:
            deepCopy.append(original[i])
            solutions.append(deepCopy)
            max_clique(g, original, deepCopy, i, solutions)

    return



if __name__ == "__main__":
    file_name = sys.argv[1]

    g = construct_graph(file_name)

    solutions = []
    original = []
    for i in range(0, len(g.graph.keys())):
        original.append(i)

    max_clique(g, original, [], -1, solutions)

    max_solution = []

    #Finds the largest function within the solutions
    for k in range(0,len(solutions)):
        if len(solutions[k]) > len(max_solution):
            max_solution = solutions[k]

    print("Max Clique: %s" % max_solution)
    print("Clique size: %d" % len(max_solution))
