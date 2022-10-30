
class node:
    def __init__(self, name, coords = None):
        self.name = name
        if coords is None:
            self.coords = []
        else:
            self.coords = coords
        #self.node_canvas = node_canvas
        self.adjacent = []
    def add_adj(self, node):
        self.adjacent.append(node)
        
class edge:
    def __init__(self, weight, x1, y1, x2, y2, nodes):
        self.weight = weight
        self.coords_edge = [[x1, y1, x2, y2]]
        self.nodes_conectados = nodes

def print_graph(g):
    for i in range(len(g)):
        print(g[i][0].name, '|(', g[i][0].coords[0], ',', g[i][0].coords[1], ')')
        for j in range(1, len(g[i])):
            if j == len(g[i])-1:
                print(g[i][j].name, end='')
            else:
                print(g[i][j].name,'-', end='')
        print()

def camino_menor_costo(g, a, b):
    return 0

def camino_mas_largo(g, a, b):
    return 0

def valor_aristas_uno(g):
    return 0

def cambiar_valor_arista(g, a, b):
    return 0

def insertar_nodos_ady(g):
    a = input('Ingresar nodo adyacente 1: ')
    b = input('Ingresar nodo adyacente 2: ')

    while a != 'x' or b !='x':
        if not g:
            g.append([a,b])
            g.append([b,a])
        else:
            estaA = False #indica si a esta en g[i][0]
            estaB = False #indica si a esta en g[i][0]
            i=0
            while (not estaA or not estaB) and i<len(g):
                if a == g[i][0]:
                    estaA = True
                    if b not in g[i]:
                        g[i].append(b)
                    i = i+1
                    while not estaB and i<len(g):
                        if b == g[i][0]: 
                            estaB = True
                            if a not in g[i]:
                                g[i].append(a)
                        i = i+1
                else:
                    if b == g[i][0]:
                        estaB = True
                        if a not in g[i]:
                            g[i].append(a)
                        i = i+1
                        while not estaA and i<len(g):
                            if a == g[i][0]: 
                                estaA = True
                                if b not in g[i]:
                                    g[i].append(b)
                            i = i+1
                    else: i=i+1
            if not estaB and estaA and i>=len(g):
                g.append([b,a])
            else:
                if not estaA and estaB and i>=len(g):
                    g.append([a,b])
                else: 
                    if not estaA and not estaB and i>=len(g):
                        g.append([a,b])
                        g.append([b,a])
            i = 0
        print(g)
        a = input('Ingresar nodo adyacente 1: ')
        b = input('Ingresar nodo adyacente 2: ')

def insertar_nodo(g, n):
    g.append(n)

def agregar_arista_bidir(g, a, b):
    l = len(g)
    estaA = False
    estaB = False
    for i in range(l):
        if a == g[i][0]:
            estaA = True
            aix = i
        if b == g[i][0]:
            estaB = True
            bix = i
    if estaA and estaB:
        g[aix].append(b)
        g[bix].append(a)
    else:
        print('Uno de los nodos no se encuentra.')

def agregar_arista_unidir(g, a, b):
    l = len(g)
    estaA = False
    estaB = False
    for i in range(l):
        if a == g[i][0]:
            estaA = True
            aix = i
        if b == g[i][0]:
            estaB = True
            bix = i
    if estaA and estaB:
        g[aix].append(b)
    else:
        print('Uno de los nodos no se encuentra.')