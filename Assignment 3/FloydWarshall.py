# Abby Seibel and Justin Ho
# CSCE310
# Assignment 3
# Graph Algorithms
# Floyd-Warshall Shortest Path Algorithm

import graph_representation as gr

'''
Given graph, sets up an adjacency matrix of the given graph
'''
def matrix_setup(graph:gr.Graph):
    n = graph.num_vertices()
    adj_matrix = []
    # Each element in matrix is initialized with empty list
    for i in range(n):
        adj_matrix.append([])
        for j in range(n):
            adj_matrix[i].append([])

    # diagonal of matrix initialized with edge to self
    for i in range(n):
        e = gr.Edge(graph.get_node(i),graph.get_node(i),0)
        adj_matrix[i][i].append(e)

    # direct paths are initialized
    for e in graph.get_edge_list():
        adj_matrix[e.get_nodes()[0].get_value()][e.get_nodes()[1].get_value()].append(e)
        adj_matrix[e.get_nodes()[1].get_value()][e.get_nodes()[0].get_value()].append(e)

    return adj_matrix

'''
Print output of the all shortest paths solution
'''
def build_path(adj_matrix, graph:gr.Graph):
    n = len(adj_matrix)

    for i in range(n):
        for j in range(i,n):
            if i == j:
                continue
            else:
                total_weight = 0
                print("%d --> %d:" % (i,j))
                print("\t", end = " ")
                if len(adj_matrix[i][j]) != 0:
                    print(adj_matrix[i][j][0], end = '')
                    total_weight = total_weight + adj_matrix[i][j][0].get_weight()
                    if len(adj_matrix[i][j]) > 1:
                        for k in range(1,len(adj_matrix[i][j])):
                            print(" -> ", end = '')
                            total_weight = total_weight + adj_matrix[i][j][k].get_weight()
                            print(adj_matrix[i][j][k].__str__(), end = '')
                else:
                    print(None, end='')
                print()
                print("\tPath weight: %.2f" % (total_weight))
                print()

'''
Implementation of Floyd-Warshall Algorithm using an adjacency matrix and improving 
the path given graph
'''
def floyd_warshall(adj_matrix, graph:gr.Graph):

    n = len(adj_matrix)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                # consider first path
                path1 = None
                if len(adj_matrix[i][k]) == 0:
                    if graph.get_edge(i,k) is not None:
                        weight1 = graph.get_edge(i,k).get_weight()
                        path1 = graph.get_edge(i,k)
                    else:
                        weight1 = None
                else:
                    path1 = adj_matrix[i][k]
                    weight1 = 0
                    for e in adj_matrix[i][k]:
                        weight1 = weight1 + e.get_weight()

                # consider second path
                path2 = None
                if len(adj_matrix[k][j]) == 0:
                    if graph.get_edge(k,j) is not None:
                        path2 = graph.get_edge(k,j)
                        weight2 = graph.get_edge(j,k).get_weight()
                    else:
                        weight2 = None
                else:
                    path2 = adj_matrix[k][j]
                    weight2 = 0
                    for e in adj_matrix[k][j]:
                        weight2 = weight2 + e.get_weight()

                # original weight
                og_weight = 0
                for e in adj_matrix[i][j]:
                    og_weight = og_weight + e.get_weight()

                # update path if better path found
                if weight1 and weight2 is not None:
                    weight = weight1 + weight2
                    if isinstance(path1, gr.Edge) and isinstance(path2, gr.Edge):
                        path = [path1, path2]
                    else:
                        path = path1 + path2
                    if len(adj_matrix[i][j]) == 0:
                        adj_matrix[i][j] = path
                    elif og_weight > weight:
                        adj_matrix[i][j] = path

    return adj_matrix

if __name__ == "__main__":
    graph = gr.parse_graph("input_given.txt")
    m = matrix_setup(graph)
    for n in m:
        for l in n:
            if len(l) == 0:
                print(None, end=', ')
            else:
                for e in l:
                    print("[", end='')
                    print(e.__str__() ,end="], ")
        print()
    print()

    m = floyd_warshall(m,graph)
    for n in m:
        for l in n:
            if len(l) == 0:
                print(None, end=', ')
            else:
                print("[", end='')
                for e in l:
                    print(e.__str__(), end="")
                print("]", end=', ')

        print()
    print()

    build_path(m,graph)