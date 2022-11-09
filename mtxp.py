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
# [0, 2] [1,5,4,3] [2, 0] [3,1] [4,1] [5,1] [6,7] [7,6]

#          1— 2 ——— 3
#         /|   | \   |\
#        / |   |  \  | \
#       0  |   8   \ |  4
#        \ |  /|    \| /
#          7 — 6 ————5       


# [[w(0, 0), w(0, 1),w(0, 2),w(0, 3),w(0, 4),w(0, 5),w(0, 6),w(0, 7)],
#  [w(1, 0), w(1, 1),w(0, 2),w(1, 3),w(1, 4),w(1, 5),w(1, 6),w(1, 7)]
#  [w(2, 0), w(2, 1),w(0, 2),w(2, 3),w(2, 4),w(2, 5),w(2, 6),w(2, 7)]
#  [w(3, 0), w(3, 1),w(0, 2),w(3, 3),w(3, 4),w(3, 5),w(3, 6),w(3, 7)]
#  [w(4, 0), w(4, 1),w(0, 2),w(4, 3),w(4, 4),w(4, 5),w(4, 6),w(4, 7)]
#  [w(5, 0), w(5, 1),w(0, 2),w(5, 3),w(5, 4),w(5, 5),w(5, 6),w(5, 7)]
#  [w(6, 0), w(6, 1),w(0, 2),w(6, 3),w(6, 4),w(6, 5),w(6, 6),w(6, 7)]
#  [w(7, 0), w(7, 1),w(0, 2),w(7, 3),w(7, 4),w(7, 5),w(7, 6),w(7, 7)]]

# [[0, 4, 0, 0, 0, 0, 0, 8, 0] ,
#  [4, 0, 8, 0, 0, 0, 0, 11, 0],
#  [0, 8, 0, 7, 0, 4, 0, 0, 2] ,
#  [0, 0, 7, 0, 9, 14, 0, 0, 0],
#  [0, 0, 0, 9, 0, 10, 0, 0, 0],
#  [0, 0, 4, 14, 10, 0, 2, 0, 0],
#  [0, 0, 0, 0, 0, 2, 0, 1, 6],
#  [8, 11, 0, 0, 0, 0, 1, 0, 7],
#  [0, 0, 2, 0, 0, 0, 6, 7, 0]
#  ]
# {ix: , node_key: }

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
            res[i][j] = get_weight(graph, i, j)
    return res


#   6 — 7
#   0 — 2
#         1
#       / | \
#      /  |  \
#     5   4   3

# [0, 2] [1,5,4,3] [2, 0] [3,1] [4,1] [5,1] [6,7] [7,6]

# def cant_sub_grafos(graph)
    # para cada nodo con sus nodos ady los agrupo con los otros que los contengan
        # la cant de conj que armo son los grafos disj

# [0, 2] [2, 0] || [1,5,4,3] [3,1] [4,1] [5,1] || [6,7] [7,6] = 3 

def count_sub_graphs(graph):
    mins = []
    for node in graph:
        if min(node) not in mins:
            mins.append(min(node))
    return len(mins)

def min_distance(graph, dist, shortest_path):
    min = float("inf")

    for v in range(len(graph)):
        if dist[v] < min and shortest_path[v] == False:
            min = dist[v]
            min_index = v
    return min_index

def dijkstra(graph, src):
    dist = float("inf") * graph
    dist[src] = 0
    shortest_path = [False] * graph

    for cout in range(graph):
        u = min_distance(graph, dist, shortest_path)
        shortest_path[u] = True

        for v in range (graph):
            if (graph[u][v] > 0 and shortest_path[v] == False and dist[v] > dist[u] + graph[u][v]):
                dist[v] = dist[u] + graph[u][v]
    return dist