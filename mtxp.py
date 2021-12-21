import array as ar

def insertar_nodos_ady(n):
    a = input('Ingresar nodo adyacente 1: ')
    b = input('Ingresar nodo adyacente 2: ')

    while a != 'x' or b !='x':
        if not n:
            n.append([a,b])
            n.append([b,a])
        else:
            estaA = False #indica si a esta en n[i][0]
            estaB = False #indica si a esta en n[i][0]
            i=0
            while (not estaA or not estaB) and i<len(n):
                if a == n[i][0]:
                    estaA = True
                    if b not in n[i]:
                        n[i].append(b)
                    i = i+1
                    while not estaB and i<len(n):
                        if b == n[i][0]: 
                            estaB = True
                            if a not in n[i]:
                                n[i].append(a)
                        i = i+1
                else:
                    if b == n[i][0]:
                        estaB = True
                        if a not in n[i]:
                            n[i].append(a)
                        i = i+1
                        while not estaA and i<len(n):
                            if a == n[i][0]: 
                                estaA = True
                                if b not in n[i]:
                                    n[i].append(b)
                            i = i+1
                    else: i=i+1
            if not estaB and estaA and i>=len(n):
                n.append([b,a])
            else:
                if not estaA and estaB and i>=len(n):
                    n.append([a,b])
                else: 
                    if not estaA and not estaB and i>=len(n):
                        n.append([a,b])
                        n.append([b,a])
            i = 0
        print(n)
        a = input('Ingresar nodo adyacente 1: ')
        b = input('Ingresar nodo adyacente 2: ')
