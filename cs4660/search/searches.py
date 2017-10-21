"""
Searches module defines all different search algorithms
"""

from graph import graph as g
from queue import Queue
from queue import PriorityQueue
import math


def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    q = Queue()
    current_node = initial_node

    q.put(current_node)
    path = []
    parents = {current_node: None}
    while not q.empty():

        current_node = q.get()

        if current_node == dest_node:
            print("Found node.")
            break

        for nextnode in graph.neighbors(current_node):
            q.put(nextnode)
            if nextnode not in parents:
                parents[nextnode] = current_node

    path.append(current_node)

    while initial_node not in path:
        current_node = parents[current_node]
        path.append(current_node)

    path.reverse()
    edgeList = []
    for x in range(len(path) - 1):
        edgeList.append(g.Edge(path[x], path[x+1], graph.distance(path[x], path[x+1])))

    return edgeList


def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    stack = []
    visited = []
    stack.append(initial_node)

    while stack:
        current_node = stack[-1]
        if current_node == dest_node:
            break

        if graph.neighbors(current_node):
            if graph.neighbors(current_node)[-1] not in visited:
                for neighbor in graph.neighbors(current_node):
                    if neighbor not in visited:
                        stack.append(neighbor)
                        visited.append(neighbor)
                        break
        else:
            stack.pop()

    path = stack
    edgeList = []
    for x in range(len(path) - 1):
        edgeList.append(g.Edge(path[x], path[x + 1], graph.distance(path[x], path[x + 1])))

    return edgeList


def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """

    parents = {initial_node: None}
    values = {initial_node: 0}
    q = {initial_node: 0}
    visited = []

    while q:
        current_node = list(q.keys())[0]
        q.pop(current_node)
        visited.append(current_node)

        if current_node == dest_node:
            break

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                newdist = graph.distance(current_node, neighbor) + values[current_node]
                if newdist is None:
                    newdist = 1
                q[neighbor] = newdist
                if neighbor not in values or newdist < values[neighbor]:
                    parents[neighbor] = current_node
                    values[neighbor] = newdist
                    q[neighbor] = newdist
        # q.pop(current_node)
        sorted(q.values())

    path = [current_node]
    while initial_node not in path:
        current_node = parents[current_node]
        path.append(current_node)

    path.reverse()
    edgeList = []
    for x in range(len(path) - 1):
        edgeList.append(g.Edge(path[x], path[x + 1], graph.distance(path[x], path[x + 1])))

    return edgeList


def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """

    parents = {initial_node: None}
    values = {initial_node: 0}
    q = {initial_node: 0}
    visited = []
    heuristcs = []

    while q:
        current_node = list(q.keys())[0]
        q.pop(current_node)
        visited.append(current_node)

        if current_node == dest_node:
            break

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                newdist = graph.distance(current_node, neighbor) + values[current_node]
                if newdist is None:
                    newdist = 1
                q[neighbor] = newdist
                if neighbor not in values or newdist < values[neighbor]:
                    parents[neighbor] = current_node
                    values[neighbor] = newdist
                    q[neighbor] = newdist
        # q.pop(current_node)
        sorted(q.values())

    path = [current_node]
    while initial_node not in path:
        current_node = parents[current_node]
        path.append(current_node)

    path.reverse()
    edgeList = []
    for x in range(len(path) - 1):
        edgeList.append(g.Edge(path[x], path[x + 1], graph.distance(path[x], path[x + 1])))

    return edgeList

    pass


def heuristic(from_node,to_node):
    x1 = from_node.data.x
    x2 = to_node.data.x
    y1 = from_node.data.y
    y2 = to_node.data.y
    return math.sqrt(math.pow((x2-x1), 2)+math.pow((y2-y1), 2))
