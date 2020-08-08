# Authors: Justin Ho and Abby Seibel
# Assignment 1B Brute Force Hamiltonian Path

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

# A recursive algorithm to generate the cliques starting with each vertex of the graph
def maximal_clique(g, position, max_clique, clique, solution):
    #absolute base case
    for v in clique:
        if position not in g.graph.get_cost(v, []) and v not in g.graph.get_cost(position, []): # Return if vertex is not a neighbour of one of the clique vertex
            return

    # add vertex to clique
    clique.append(position)
    position = position + 1

    # if all vertices are traversed, maximal clique
    if len(clique) == len(g.graph.keys()):
        max_clique = clique
        return

    # update maximal clique if larger clique found
    if len(clique) > len(max_clique):
        max_clique = clique
        solution.append(max_clique)

    new_clique = [i for i in clique]
    # based on the index of the position, iterate the rest of the values in the list
    for v in range(position, len(g.graph.keys())):
        if v not in new_clique:
            maximal_clique(g, v, max_clique, new_clique, solution)


if __name__ == "__main__":
    file_name = 'input001.txt'

    g = construct_graph(file_name)

    # maximal clique starting from a given vertex
    max_clique = []

    # list of cliques from each maximal clique of a given starting index
    solution = []

    for vertex in g.graph.keys():
        maximal_clique(g, vertex, max_clique, [], solution)

    # initialize largest maximal clique
    largest_clique = solution[0]

    # obtain the largest clique within the solutions
    for s in solution:
        if len(s) > len(largest_clique):
            largest_clique = s

    print("Maximal Clique Size: %d" % len(largest_clique))
    print("Clique: %s" % largest_clique)