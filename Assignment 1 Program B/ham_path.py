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

# Using DFS and backtracking, find a hamiltonian path and returns the path if found
# Else, returns None
def ham_path(g, pos, num_vertices, path=[]):
    if pos not in set(path): # ensure each vertex in path is unique
        path.append(pos) # appends position into path if unexplored

        # if the length of path is equal to num_vertices, hamiltonian path found
        if len(path) == num_vertices:
            return path

        # assess each neighbour of the current vertex
        for newPos in g.graph.get(pos, []):
            if newPos not in path: # ensure uniqueness of each vertex
                curr_path = [i for i in path] # deep copy of path
                new_path = ham_path(g, newPos, num_vertices, curr_path) # try new path using position
                if new_path is not None: # not None for new path means Hamiltonian Path found
                    return new_path

        # Return None if Hamiltonian Path not found
        return None


def distinct_paths(g, start, end, path, distinct_path):
    if start not in path:
        path.append(start)
    if start == end:
        distinct_path.append(path)
        return
    for new_start in g.graph.get(start, []):
        if new_start not in path:
            curr_path = [i for i in path]
            distinct_paths(g, new_start, end, curr_path, distinct_path)

    return


def maximal_cliques(g, pos, shared_vertices, clique, distinct_cliques):
    if pos not in clique:
        clique.add(pos)
    shared_vertices = set(g.graph.get(pos, [])).intersection(shared_vertices)
    n = len(shared_vertices)
    if n == 0:
        distinct_cliques.append(clique)
        return
    for new_pos in shared_vertices:
        if new_pos not in clique:
            curr_clique = set(i for i in clique)
            maximal_cliques(g, new_pos, shared_vertices, curr_clique, distinct_cliques)

    return


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

    # Maximal Cliques Problem
    '''
    distinct_cliques = []
    
    for v in g.graph.keys():
        maximal_cliques(g, v, g.graph.get(v, []), set(), distinct_cliques)
        

    for c in distinct_cliques:
    if c not in solution:
        solution.append(c)

    for c in solution:
        print(c)
    '''


    # Distinct Simple Paths Problem
    '''
    distinct_path = []
    distinct_paths(g, 1 , 6, [], distinct_path)

    for p in distinct_path:
        print(p)
    '''


