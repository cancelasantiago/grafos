import array as ar

class nodo:
    def __init__(self, name, coords = None):
        self.name = name
        if coords is None:
            coords = {}
        else:
            self.coords = coords
        self.aristas = []
    def get_atr(self):
        return [self.name, self.coords]
class arista:
    def __init__(self, val, x1, y1, x2, y2, nodos):
        self.val = val
        self.coords_arista = [[x1, y1, x2, y2]]
        self.nodos_conectados = nodos

def imprimir_grafo(g):
    for i in range(len(g)):
        print('Nombre de nodo:', g[i][0].name)
        print('Coord x: ', g[i][0].coords[0], ', Coord y: ', g[i][0].coords[1])
        for j in range(len(g[i])):
            print('(',g[i][j].name,')', end=''),
        print()

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