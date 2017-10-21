"""
utils package is for some quick utility methods

such as parsing
"""
from io import open
from . import graph as g


class Tile(object):
    """Node represents basic unit of graph"""
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

    def __str__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)

    def __repr__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.symbol == other.symbol
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self.x) + "," + str(self.y) + self.symbol)


def parse_grid_file(graph, file_path):
    """
    ParseGridFile parses the grid file implementation from the file path line
    by line and construct the nodes & edges to be added to graph

    Returns graph object
    """
    # TODO: read the filepaht line by line to construct nodes & edges

    # TODO: for each node/edge above, add it to graph

    with open(file_path) as f:
        lines = f.readlines()
        lines.pop(0)
        str = []
        grid = []
        for i in range(len(lines) - 1):
            lines[i] = lines[i][1:-2]
            for j in range(0, len(lines)-1, 2):
                tile = lines[i][j] + lines[i][j+1]
                str.append(tile)
            grid.append(str)
            str = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                tile = Tile(i, j, grid[i][j])
                graph.add_node(tile)
                if j < (len(grid[i])-1) and grid[i][j+1] != '##':
                    graph.add_edge(g.Edge(tile, Tile(i, j+1, grid[i][j+1]), 1))
                    graph.add_edge(g.Edge(Tile(i, j + 1, grid[i][j + 1]), tile, 1))
                if i < (len(grid)-1) and grid [i+1][j] != '##':
                    graph.add_edge(g.Edge(tile, Tile(i + 1, j, grid[i + 1][j]), 1))
                    graph.add_edge(g.Edge(Tile(i + 1, j, grid[i + 1][j]), tile, 1))

    return graph


def convert_edge_to_grid_actions(edges):
    """
    Convert a list of edges to a string of actions in the grid base tile

    e.g. Edge(Node(Tile(1, 2), Tile(2, 2), 1)) => "S"
    """
    actions = []
    for edge in edges:
        if edge.to_node.data.x - edge.from_node.data.x == 1:
            actions.append('E')
        elif edge.to_node.data.x - edge.from_node.data.x == -1:
            actions.append('W')
        elif edge.to_node.data.y - edge.from_node.data.y == 1:
            actions.append('S')
        elif edge.to_node.data.y - edge.from_node.data.y == -1:
            actions.append('N')
    return "".join(actions)
