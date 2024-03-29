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
        g.add_vertex(int(adj_list[0]))  # adds the first number as vertex

    f = open(file, "r")
    num_lines = int(f.readline()) # reads the number of lines in the file

    for n in range(num_lines):
        adj_list = f.readline().strip().split(' ')
        for i in range(1, len(adj_list)):
            g.add_edges(int(adj_list[0]), int(adj_list[i])) # adds subsequent numbers as edges
            g.add_edges(int(adj_list[i]), int(adj_list[0]))

    return g

# Using DFS and backtracking, find a hamiltonian path and returns the path if found
# Else, returns None
def ham_path(g, pos, num_vertices, path=[]):
    if pos not in set(path): # ensure each vertex in path is unique
        path.append(pos) # appends position into path if unexplored

        # if the length of path is equal to num_vertices, hamiltonian path found
        if len(path) == num_vertices:
            return path

        # assess each neighbour of the current vertex
        for newPos in g.graph.get_cost(pos, []):
            if newPos not in path: # ensure uniqueness of each vertex
                curr_path = [i for i in path] # deep copy of path
                new_path = ham_path(g, newPos, num_vertices, curr_path) # try new path using position
                if new_path is not None: # not None for new path means Hamiltonian Path found
                    return new_path

        # Return None if Hamiltonian Path not found
        return None

if __name__ == "__main__":
    file_name = sys.argv[1]

    g = construct_graph(file_name)

    # iterate through every vertex as the first position in path
    for v in g.graph.keys():
        solution = ham_path(g, v, g.vertex_num, path=[])
        if solution is not None: # breaks once solution is found
            break

    if solution is None:
        print("No Hamiltonian Paths")
    else:
        print(solution)
