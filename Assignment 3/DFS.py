# Abby Seibel and Justin Ho
# CSCE310
# Assignment 3
# Graph Algorithms: DFS

import graph_representation as gr

# stack based implementation of DFS
# Returns list according to the visit order of the graph using DFS given graph
# Visits the next smallest node value
def DFS_stack(graph:gr.Graph):
    visit_order = []
    graph.reset()
    count = 1
    stack = []

    start_node = graph.get_node(0)
    stack.append(start_node)
    start_node.set_time_visited(count)
    start_node.visit()
    visit_order.append(start_node.get_value())

    while len(stack) != 0:
        count = count + 1
        x = stack[-1]
        x_neighbours = sorted(graph.neighbour(x.get_value()))
        y = None
        for n in x_neighbours:
            if not n.is_visited() and not n.is_processed():
                y = n
                break

        if y is None:
            stack.pop()
            x.process()
            x.set_time_processed(count)
        else:
            stack.append(y)
            y.visit()
            visit_order.append(y.get_value())
            y.set_time_visited(count)

    return visit_order

if __name__ == "__main__":
    graph = gr.parse_graph('input001.txt')
    visit_order = DFS_stack(graph)
    print("Depth First Traversal (vertex visited order):")
    print(visit_order)