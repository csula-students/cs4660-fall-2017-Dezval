"""
quiz2!
Use path finding algorithm to find your way through dark dungeon!
Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9
TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import json
import codecs

# http lib import for Python 2 and 3: alternative 4
from queue import Queue

import graph

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"


def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)


def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.
    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)


def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    reader = codecs.getreader("utf-8")
    response = json.load(reader(urlopen(req, jsondataasbytes)))
    return response


def get_node(node_id):
    if node_id in nodes:
        return nodes[node_id]
    else:
        node = get_state(node_id)
        nodes[node_id] = node
        return node


def bfs(from_node_id, to_node_id):
    counter = 0
    q = Queue()
    current_node = get_node(from_node_id)
    # print("current node before loop: ", current_node)
    q.put(current_node)
    path = []
    parents = {current_node['id']: None}
    while not q.empty():
        counter += 1
        print("Please wait...",counter)
        # print("Gonna get q... q size before: ", q.qsize())
        current_node = q.get()
        # print("Current node counter: ", counter, " node: ", current_node)
        # print("Got q.......... q size after: ",q.qsize())
        # print("Got node ", counter)
        if current_node['id'] == to_node_id:
            print("Found node.")
            break
        counter2 = 0
        for nextnode in current_node['neighbors']:
            # print("for loop: ", counter, ", iteration: ", counter2)
            # print("next node: ", nextnode)
            q.put(get_node(nextnode['id']))
            if nextnode['id'] not in parents:
                parents[nextnode['id']] = current_node['id']
            counter2 += 1

    # print("Parents: ", parents)
    path.append(current_node['id'])
    # print("Appended id: ", current_node['id'])

    # loopcounter = 0
    current_node = current_node['id']
    while from_node_id not in path:
        # print("loop counter: ", loopcounter)
        current_node = parents[current_node]
        # print("Appended id: ", current_node)
        path.append(current_node)
        # loopcounter += 1

    path.reverse()
    for x in range(len(path) - 1):
        edges[path[x]] = path[x + 1]

    return path


def dijkstras(from_node_id, to_node_id):
    visited = []
    unvisited = [from_node_id]

    tentative_distances = {from_node_id:0}

    current_node = get_node(from_node_id)

    table = {from_node_id: [0, None]}

    for neighbor in get_neighbors(current_node['id']):
        table[neighbor['id']] = [getweight(current_node['id'], neighbor['id']), current_node['id']]
        unvisited.append(neighbor['id'])

    visited.append(current_node['id'])




def get_neighbors(node_id):
    return get_node(node_id)['neighbors']


def getweight(from_id, to_id):
    return transition_state(from_id, to_id)['event']['effect']


""" 
visited{[1,None][2,1][3,1][4,2][5,2]}
target = 5
path.append(current_node = 5,visited[5] = 2,visited[2] = 1)

"""


if __name__ == "__main__":
    # Your code starts here
    nodes = {}
    edges = {}

    # path = bfs('7f3dc077574c013d98b2de8f735058b4', 'f1f131f647621a4be7c71292e79613f9')
    #
    # for i in range(len(path)-1):
    #     print(get_node(path[i])['location']['name'],"(",path[i],") :",get_node(path[i+1])['location']['name'],"(",path[i+1],") : ", getweight(path[i],path[i+1]))

    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    # for neighbor in empty_room['neighbors']:
    #     print(neighbor)
    print("empty_room neighbors: ", get_neighbors(empty_room['id']))
    # print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))