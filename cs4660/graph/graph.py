"""
graph module defines the knowledge representations files

A Graph has following methods:

* adjacent(node_1, node_2)
    - returns true if node_1 and node_2 are directly connected or false otherwise
* neighbors(node)
    - returns all nodes that is adjacency from node
* add_node(node)
    - adds a new node to its internal data structure.
    - returns true if the node is added and false if the node already exists
* remove_node
    - remove a node from its internal data structure
    - returns true if the node is removed and false if the node does not exist
* add_edge
    - adds a new edge to its internal data structure
    - returns true if the edge is added and false if the edge already existed
* remove_edge
    - remove an edge from its internal data structure
    - returns true if the edge is removed and false if the edge does not exist
"""

from io import open
from operator import itemgetter


def construct_graph_from_file(graph, file_path):
    """
    TODO: read content from file_path, then add nodes and edges to graph object
    
    note that graph object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented

    In example, you will need to do something similar to following:

    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph
    """

    # graph = AdjacencyList()
    with open(file_path) as f:
        info = f.readlines()
        num_of_nodes = int(info[0])
        info.pop(0)
    for i in range(num_of_nodes):
        graph.add_node(Node(i))

    for i in info:
        i = i.split(":")
        i[2] = i[2].split("\n")[0]
        e = Edge(Node(int(i[0])),Node(int(i[1])),int(i[2]))
        graph.add_edge(e)

    return graph


class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Node({})'.format(self.data)

    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)


class Edge(object):
    """Edge represents basic unit of graph connecting between two edges"""
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight))


class AdjacencyList(object):
    """
    AdjacencyList is one of the graph representation which uses adjacency list to
    store nodes and edges
    """
    def __init__(self):
        # adjacencyList should be a dictionary of node to edges
        self.adjacency_list = {}

    def adjacent(self, node_1, node_2):
        """
        * adjacent(node_1, node_2)
        - returns true if node_1 and node_2 are directly connected or false otherwise
        """
        if node_1 not in self.adjacency_list or node_2 not in self.adjacency_list:
            return False

        for x in self.adjacency_list[node_2]:
            if node_1 == x.to_node:
                return True
        for x in self.adjacency_list[node_1]:
            if node_2 == x.to_node:
                return True

        return False
        pass

    def neighbors(self, node):
        """
        * neighbors(node)
        - returns all nodes that is adjacent from node
        """
        neighbor_nodes = []
        for i in self.adjacency_list[node]:
            neighbor_nodes.append(i.to_node)
        return neighbor_nodes
        pass

    def add_node(self, node):
        """
        * add_node(node)
        - adds a new node to its internal data structure.
        - returns true if the node is added and false if the node already exists
        """
        if node in self.adjacency_list:
            return False

        self.adjacency_list[node] = []
        return True
        pass

    def remove_node(self, node):
        """
        * remove_node
        - remove a node from its internal data structure
        - returns true if the node is removed and false if the node does not exist
        """
        if node not in self.adjacency_list:
            return False
        else:
            del self.adjacency_list[node]
            for x in self.adjacency_list:
                for y in self.adjacency_list[x]:
                    if node == y.to_node:
                        self.adjacency_list[x].remove(y)
            return True
        pass

    def add_edge(self, edge):
        """
        * add_edge
            - adds a new edge to its internal data structure
            - returns true if the edge is added and false if the edge already existed
        """
        if edge.from_node not in self.adjacency_list or edge in self.adjacency_list[edge.from_node]:
            return False
        self.adjacency_list[edge.from_node].append(edge)
        return True
        # if edge.from_node in self.adjacency_list:
        #     if edge in \
        #             self.adjacency_list[edge.from_node]:
        #         return False
        #     else:
        #         self.adjacency_list[edge.from_node].append(edge)
        #         return True
        # return False
        # pass

    def remove_edge(self, edge):
        """
        * remove_edge
            - remove an edge from its internal data structure
            - returns true if the edge is removed and false if the edge does not exist
        """

        if edge.from_node in self.adjacency_list:
            if edge in \
                    self.adjacency_list[edge.from_node]:
                self.adjacency_list[edge.from_node].remove(edge)
                return True
        return False

        # if edge not in self.adjacency_list[edge.from_node] or edge.from_node not in self.adjacency_list:
        #     return False
        # else:
        #     self.adjacency_list[edge.from_node].remove(edge)
        #     return True
        pass

<<<<<<< HEAD
=======
    def distance(self, node_1, node_2):
        pass
>>>>>>> course/master

class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []

    def adjacent(self, node_1, node_2):
        """
        * adjacent(node_1, node_2)
            - returns true if node_1 and node_2 are
            directly connected or false otherwise
        """
        if node_1 not in self.nodes or node_2 not in self.nodes:
            return False
        node1index = self.nodes.index(node_1)
        node2index = self.nodes.index(node_2)


        if self.adjacency_matrix[node1index][node2index] > 0 \
        or \
        self.adjacency_matrix[node2index][node1index] != 0:
            return True
        return False
        pass

    def neighbors(self, node):
        """
        * neighbors(node)
        - returns all nodes that is adjacent from node
        """
        neighbor_nodes = []
        if node in self.nodes:
            index = self.nodes.index(node)
            for i in range(len(self.nodes)):
                if self.adjacency_matrix[index][i] > 0:
                    neighbor_nodes.append(self.nodes[i])

        return neighbor_nodes

        pass

    def add_node(self, node):
        """
        * add_node(node)
        - adds a new node to its internal data structure.
        - returns true if the node is added and false if the node already exists
        """
        if node in self.nodes:
            return False

        nodes = []
        for i in range(len(self.nodes)):
            nodes.append(0)

        self.adjacency_matrix.append(nodes)

        for i in range(len(self.adjacency_matrix)):
            self.adjacency_matrix[i].append(0)

        self.nodes.append(node)
        return True
        pass

    def remove_node(self, node):
        """
        * remove_node
            - remove a node from its internal data structure
            - returns true if the node is removed and false if the node does not exist
        """
        if node not in self.nodes:
            return False

        index = self.nodes.index(node)

        for i in range(len(self.adjacency_matrix)):
            self.adjacency_matrix[i].pop(index)

        self.nodes.remove(node)
        return True
        pass

    def add_edge(self, edge):
        """
        * add_edge
        - adds a new edge to its internal data structure
        - returns true if the edge is added and false if the edge already existed
        """
        if edge.from_node not in self.nodes or edge.to_node not in self.nodes:
            return False
        if self.adjacency_matrix[self.nodes.index(edge.from_node)][self.nodes.index(edge.to_node)] > 0:
            return False
        else:
            self.adjacency_matrix[self.nodes.index(edge.from_node)][self.nodes.index(edge.to_node)] = edge.weight
            return True
        pass

    def remove_edge(self, edge):
        """
        * remove_edge
        - remove an edge from its internal data structure
        - returns true if the edge is removed and false if the edge does not exist
        """
        if edge.from_node not in self.nodes or edge.to_node not in self.nodes:
            return False

        if not self.adjacency_matrix[self.nodes.index(edge.from_node)][self.nodes.index(edge.to_node)] > 0:
            return False
        else:
            self.adjacency_matrix[self.nodes.index(edge.from_node)][self.nodes.index(edge.to_node)] = 0
            return True
        pass

    def distance(self, node_1, node_2):
        pass

    def __get_node_index(self, node):
        """helper method to find node index"""
        if node in self.nodes:
            for i in range(len(self.nodes)):
                if self.nodes[i] == node:
                    return i
        return -1
        pass


class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    def adjacent(self, node_1, node_2):
        """
        * adjacent(node_1, node_2)
            - returns true if node_1 and node_2 are directly connected
            or false otherwise
        """
        for i in range(len(self.edges)):
            if self.edges[i].from_node == node_1 and self.edges[i].to_node == node_2:
                return True
            if self.edges[i].from_node == node_2 and self.edges[i].to_node == node_1:
                return True
        return False

        pass

    def neighbors(self, node):
        """
        * neighbors(node)
            - returns all nodes that is adjacency from node
        """
        neighbor_nodes = []
        if node in self.nodes:
            for i in range(len(self.edges)):
                if self.edges[i].from_node == node:
                    neighbor_nodes.append(self.edges[i].to_node)
                # if self.edges[i].to_node == node:
                #     neighbor_nodes.append(self.edges[i].from_node)
        return neighbor_nodes
        pass

    def add_node(self, node):
        """
        * add_node(node)
            - adds a new node to its internal data structure.
            - returns true if the node is added and false if the node already exists
        """
        if node in self.nodes:
            return False
        self.nodes.append(node)
        return True
        pass

    def remove_node(self, node):
        """
        * remove_node
            - remove a node from its internal data structure
            - returns true if the node is removed and false if the node does not exist
        """
        if node not in self.nodes:
            return False

        for edge in self.edges:
            if edge.from_node == node or edge.to_node == node:
                self.edges.remove(edge)

        self.nodes.remove(node)
        return True
        pass

    def add_edge(self, edge):
        """
        * add_edge
            - adds a new edge to its internal data structure
            - returns true if the edge is added and false if the edge already existed
        """
        if edge in self.edges:
            return False
        if edge.from_node in self.nodes and edge.to_node in self.nodes:
            self.edges.append(edge)
            return True
        return False
        pass

    def remove_edge(self, edge):
        """
        * remove_edge
            - remove an edge from its internal data structure
            - returns true if the edge is removed and false if the edge does not exist
        """
        if edge not in self.edges:
            return False
        self.edges.remove(edge)
        return True
        pass

<<<<<<< HEAD

=======
    def distance(self, node_1, node_2):
        pass
>>>>>>> course/master
