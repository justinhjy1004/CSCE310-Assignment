import graph_representation as gr
import BFS as bfs

def cycle_detection(g_cycle:gr.Graph):
    g_cycle.reset()
    count = 1
    stack = []

    for n in g_cycle.get_node_list():
        if not n.is_visited() and not n.is_processed():
            start_node = g_cycle.get_node(n.get_value())
            stack.append(start_node)
            start_node.set_time_visited(count)
            start_node.visit()

            while len(stack) != 0:
                count = count + 1
                x = stack[-1]
                x_neighbours = sorted(g_cycle.neighbour(x.get_value()))
                y = None

                for n in x_neighbours:
                    if not n.is_visited() and not n.is_processed():
                        y = n
                    if y is not None:
                        break

                if y is None:
                    stack.pop()
                    x.process()
                    x.set_time_processed(count)
                else:
                    # detects any backedges
                    if len(stack) > 1:
                        for i in range(len(stack) - 1):
                            if stack[i] in g_cycle.neighbour(y.get_value()):
                                return True
                    stack.append(y)
                    y.visit()
                    y.set_time_visited(count)

    return False

def Kruskal(graph:gr.Graph):
    edge_list = sorted(graph.get_edge_list())
    g = gr.Graph(graph.num_vertices())
    k = 0
    while len(g.get_edge_list()) < g.num_vertices() - 1 and k < len(edge_list):
        x = edge_list[k].get_nodes()[0].get_value()
        y = edge_list[k].get_nodes()[1].get_value()
        w = edge_list[k].get_weight()
        g.add_edge(x,y,w)
        if cycle_detection(g):
            g.remove_edge(x,y,w)
        k = k + 1

    return g


if __name__ == "__main__":
    graph = gr.parse_graph("input004.txt")
    g = Kruskal(graph)
    g.print_edges()
    if len(g.get_edge_list()) == g.num_vertices()-1:
        print("Type: Full Spaning Tree")
    else:
        print("Type: Minimum Spanning Forest")
