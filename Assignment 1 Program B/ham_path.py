import sys
class Graph(object):
    def __init__(self, vertex_num):
        self.graph = {}
        self.vertex_num = vertex_num

    def add_vertex(self,v):
        if v not in self.graph.keys():
            self.graph[v] = []

    def add_edges(self, v, e):
        self.graph[v].append(e)

    '''
    def __str__(self):
        for v in self.graph.keys():
            for e in self.graph[v]:
                print(f'{v} -> {e}', end = ' ')
            print()
            '''

def construct_graph(file):
    f = open(file, "r")
    num_lines = int(f.readline())

    g = Graph(num_lines)

    for n in range(num_lines):
        adj_list = f.readline().strip().split(' ')
        g.add_vertex(int(adj_list[0]))
        for i in range(1,len(adj_list)):
            g.add_edges(int(adj_list[0]), int(adj_list[i]))

    return g

def ham_path(g, pos, length, path=[]):
    if pos not in set(path):
        path.append(pos)

        '''
        print("Path Explored", end=" -> ")
        for p in path:
            print(p.__str__(), end=" ")
        print()
        '''

        if len(path) == length:
            return path

        for newPos in g.graph.get(pos, []):
            if newPos not in path:
                curr_path = [i for i in path]
                new_path = ham_path(g, newPos, length, curr_path)
                if new_path is not None:
                    return new_path

        return None

def distinct_paths(g, start, end, path, distinct_path):
    if start not in path:
        path.append(start)
    if start == end:
        distinct_path.append(path)
        return
    for new_start in g.graph.get(start,[]):
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
    file_name = 'input001.txt'

    g = construct_graph(file_name)
    distinct_cliques = []
    for v in g.graph.keys():
        maximal_cliques(g, v, g.graph.get(v, []), set(), distinct_cliques)

    solution = []

    for c in distinct_cliques:
        if c not in solution:
            solution.append(c)

    for c in solution:
        print(c)
    '''
     distinct_path = []
    distinct_paths(g, 1 , 6, [], distinct_path)

    for p in distinct_path:
        print(p)
    '''

    '''
        for v in g.graph.keys():
        solution = ham_path(g, v, g.vertex_num, path = [])
        if solution is not None:
            break

    if solution is None:
        print("No Hamiltonian Paths")
    else:
        print(solution)
    '''



