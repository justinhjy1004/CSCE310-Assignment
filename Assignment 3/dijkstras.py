"""
Abby Seibel and Justin Ho
CSCE310 Assignment 3
shortest distance by implementing dijkstars algorithm
"""
import graph_representation as gr
import heapq as hq

class priorityQObject(object):
    def __init__(self,dv,pv,v):
        self.dv = dv
        self.pv=pv
        self.v = v
    def set_dv(self, dv):
        self.dv = dv
    def set_pv(self,pv):
        self.pv = pv
    def set_v(self,v):
        self.v = v
    def get_dv(self):
        return self.dv
    def get_pv(self):
        return self.pv
    def get_v(self):
        return self.v
    def __le__(self, other):
        if self.dv <= other.dv:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.dv >= other.dv:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.dv < other.dv:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.dv > other.dv:
            return True
        else:
            return False


def dijkstras(graph:gr.Graph, s:gr.Node):
    """
    Takes in a graph and a starting node, and builds a table that hold the shortest path from s to
    all other verticies
    """
    heap = []
    map = {}

    for v in graph.get_node_list():
        if v == s:
            triple = priorityQObject(0, None, v)
            hq.heappush(heap,triple)
            # this allows easy access to the vetex and its weight
            map[v] = triple
        else:
            triple = priorityQObject(float('inf'), None, v)
            map [v] = triple
            hq.heappush(heap, triple)
    Vt = set()
    for i in range(len(graph.get_node_list())):
        uPQObject = hq.heappop(heap)
        u = uPQObject.get_v()
        Vt.add(u)
        for v in graph.neighbour(u.get_value()):
            v_object = map[v]
            v_dv_val = map[v].get_dv()
            if v not in Vt:
                u_v_edge = graph.get_edge(u.get_value(), v.get_value())
                if uPQObject.get_dv() + u_v_edge.get_weight() < v_dv_val :
                    v_object.set_dv(uPQObject.get_dv() + u_v_edge.get_weight())
                    v_object.set_pv(u)
                    hq.heapify(heap)
    result = []
    for x in Vt:
        temp = map[x]
        vertex = temp.get_v()
        dv = temp.get_dv()
        pv = temp.get_pv()
        if pv != None:
            result.append((vertex.get_value(), dv, pv.get_value()))
        else:
            result.append((vertex.get_value(), dv, pv))


    return result


if __name__ == "__main__":
    g = gr.parse_graph("input001.txt")
    startNode= g.get_node(0)
    print(dijkstras(g,startNode))
