import array as ar

n = []

a = input('ingresar nodo1')
b = input('ingresar nodo2')

while a != 'x' or b !='x':
    if not n:
        n.append([a,b])
        n.append([b,a])
        print(n)
    else:
        estaA = False
        estaB = False
        i=0
        while estaA == False and estaB == False and i<=len(n):
            if a == n[i][0] and b not in n[i]:
                estaA = True
                n[i].append(b)
                print(n)
            else:
                if b == n[i][0]:
                    estaB = True
                else:
                    i = i+1
    a = input('ingresar nodo adyacente 1: ')
    b = input('ingresar nodo adyacente 2: ')
