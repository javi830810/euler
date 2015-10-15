import math

class Edge(object):

    def __init__(self, weight):
        self.weight = weight

class Node(object):

    def __init__(self, value=None, nodes=None):
        self.nodes = nodes or []
        self.value = value
        self.visited = False

    def add_neighboor(self, node, edge):
        # TODO: Check node doesnt exists already...
        edge_value = Edge(edge)
        self.nodes.append((node, edge_value))
        node.nodes.append((self, edge_value))


class Graph(object):

    def __init__(self, nodes=[]):
        self.nodes = nodes

    def prim(self):
        visited = [self.nodes[0]]
        visited[0].visited = True
        edges = []

        while len(visited) != len(self.nodes):
            node1, edge, node2 = self.minimun_exit(visited)
            

            edges.append((node1, edge, node2))
            node2.visited = True
            visited.append(node2)
        return edges

    def minimun_exit(self, nodes):
        MAX = 100000
        def node_key(node1, node2):
            return "%s_%s" % (node1.value, node2.value)

        exit_node = None
        min_edge = MAX
        min_node = None

        for node in nodes:
            for node_edge in node.nodes:
                if node_edge[0].visited:
                    continue

                if node_edge[1].weight < min_edge:
                    min_edge = node_edge[1]
                    min_node = node_edge[0]
                    exit_node = node

        return (exit_node, min_edge, min_node)





        return pairs.values()

node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')

node_a.add_neighboor(node_b, 3)
node_a.add_neighboor(node_d, 1)
node_b.add_neighboor(node_c, 1)
node_c.add_neighboor(node_d, 1)

graph = Graph(nodes=[node_a,node_b, node_c, node_d])

for pair in graph.prim():
    print "Node1: %s" % pair[0].value
    print "Weight: %s" % pair[1].weight
    print "Node2: %s" % pair[2].value
