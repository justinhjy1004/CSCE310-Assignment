import graph_representation as gr

# Returns list according to the visit order of the graph using BFS given graph
# Visits the edge in the order of least weight
def BFS_Main(graph:gr.Graph):
    graph.reset()
    count = [0]
    tree_num = 0
    visit_order = []
    for n in graph.get_node_list():
        if not n.is_visited() and not n.is_processed():
            tree_num = tree_num + 1
            BFS(graph, n, count, visit_order)

    return visit_order

def BFS(graph: gr.Graph, n:gr.Node, count, visit_order):
    count[0] = count[0] + 1
    queue = []
    n.visit()
    visit_order.append(n)
    n.set_time_visited(count[0])
    queue.append(n)

    while len(queue) != 0:
        x = queue[0]
        x_edges = sorted(graph.get_edges(x.get_value()))
        for e in x_edges:
            y = e.get_nodes()[0]
            if y == x:
                y = e.get_nodes()[1]
            if not y.is_visited() and not y.is_processed():
                count[0] = count[0] + 1
                y.visit()
                visit_order.append(y)
                y.set_time_visited(count[0])
                queue.append(y)

        z = queue.pop(0)
        count[0] = count[0] + 1
        z.process()
        z.set_time_processed(count[0])

if __name__ == "__main__":
    g = gr.parse_graph("input_given.txt")
    visit_order = BFS_Main(g)

    results = []
    for v in visit_order:
        results.append(v.get_value())

    print("Breadth First Traversal (lowest-weight-next):")
    print(results)