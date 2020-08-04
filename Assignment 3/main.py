import sys
import graph_representation as gr
import BFS
import DFS
import Kruskal
import FloydWarshall as fw

if __name__ == "__main__":
    graph = gr.parse_graph(sys.argv[1])

    print("Graph:")
    for e in graph.get_edge_list():
        print(e)
    print()

    visit_order = DFS.DFS_main(graph)
    print("Depth First Traversal (vertex visited order):")
    print(visit_order)
    print()

    visit_order = BFS.BFS_Main(graph)

    results = []
    for v in visit_order:
        results.append(v.get_value())

    print("Breadth First Traversal (lowest-weight-next):")
    print(results)
    print()

    print("Minimum Spanning Tree:")
    g = Kruskal.Kruskal(graph)
    g.print_edges()
    if len(g.get_edge_list()) == g.num_vertices()-1:
        print("Type: Full Spanning Tree")
    else:
        print("Type: Minimum Spanning Forest")

    print()
    print("Shortest Path:")
    m = fw.matrix_setup(graph)
    m = fw.floyd_warshall(m, graph)
    fw.build_path(m, graph)