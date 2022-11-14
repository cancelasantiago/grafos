import sys


class node:
    def __init__(self, key, canvas, edges = None, coords = None, adjacents = None):
        self.key = key
        self.canvas = canvas
        self.edges = edges
        if edges is None:
            self.edges = []
        else:
            self.edges = edges
        if coords is None:
            self.coords = []
        else:
            self.coords = coords
        self.adjacents = adjacents
    def add_adj_edge(self, edge):
        self.edges.append(edge)
    def add_adj_node(self, node):
        self.adjacents.append(node)
    def get_adjacents(self):
        res = []
        for node in self.adjacents:
            res.append([node["node"].key, node["weight"]])
        return res
        
        
class edge:
    def __init__(self, weight, x1, y1, x2, y2, canvas, nodes):
        self.weight = weight
        self.coords_edge = [[x1, y1, x2, y2]]
        self.canvas = canvas
        self.nodes_conectados = nodes

def print_graph(g):
    for node in g:
        print ("key: ", node.key, "-> ", node.edges, node.get_adjacents())

def graph_mtx_simplified(graph):
    res = []
    for node in graph:
        res.append([node.key])
        ix = len(res) - 1
        for adj in node.adjacents:
            res[ix].append(adj["node"].key)
    return res

def get_weight(graph, ix1, ix2): #return the weight between node on index ix1 and node on index ix2
        res = 0
        source_node = graph[ix1]
        adj_aux = graph[ix2]
        for adj in source_node.adjacents:
            if adj["node"].key == adj_aux.key:
                res = adj["weight"]
        return res

def graph_to_mtx(graph): #return the adjacent matrix from the canvas graph
    res = [[0 for column in range(len(graph))] for row in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            res[i][j] = int(get_weight(graph, i, j))
    return res

def count_sub_graphs(graph):
    mins = []
    for node in graph:
        if min(node) not in mins:
            mins.append(min(node))
    return len(mins)

def min_distance(graph, dist, shortest_path):
    min = sys.maxsize

    for v in range(len(graph)):
        if dist[v] < min and shortest_path[v] == False:
            min = dist[v]
            min_index = v
    return min_index

def dijkstra(graph, src):
    dist = [sys.maxsize] * len(graph)
    dist[src] = 0
    shortest_path = [False] * len(graph)
    for cout in range(len(graph)):
        u = min_distance(graph, dist, shortest_path)
        shortest_path[u] = True
        for v in range (len(graph)):
            if (graph[u][v] > 0 and shortest_path[v] == False and dist[v] > dist[u] + graph[u][v]):
                dist[v] = dist[u] + graph[u][v]
    paths = []
    path = [] 
    for i in range(len(graph)):
        if graph[0][i] != 0:
            paths.append({"path": [0, i], "value": dist[i]})
    for j in range(1, len(graph)):
        for k in range (j, len(graph)):
            if graph[j][k] != 0:
                for l in range(len(paths)):
                    if j == paths[l]["path"][-1]:
                        paths.append(paths[l])
                        paths[-1]["path"].append(k)
                        paths[-1]["value"] += graph[j][k]
    print(paths)
    return dist

def printSolution(dist, graph):
        print("Vertex \tDistance from Source")
        for node in range(len(graph)):
            print(node, "\t", dist[node])