import mtxp

g = []

print('Selecciona una opción: ')
print('     1)Ingresar nodos.')
print('     2)Ingresar aristas bidireccionales.')
print('     3)Ingresar arista unidireccional.')
print('     4)Imprimir grafo.')
print('     5)Salir.')
o = input('Opción: ')
while o != '5':
    if o == '1':
        mtxp.insertar_nodos(g)
    elif o == '2':
        a = input('Vertice 1: ')
        b = input('Vertice 2: ')
        mtxp.agregar_arista_bidir(g, a, b)
    elif o == '3':
        a = input('Vertice 1: ')
        b = input('Vertice 2: ')
        mtxp.agregar_arista_unidir(g, a, b)
    elif o == '4':
        print(g)
    print('Selecciona una opción: ')
    print('     1)Ingresar nodos.')
    print('     2)Ingresar aristas bidireccionales.')
    print('     3)Ingresar arista unidireccional.')
    print('     4)Imprimir grafo.')
    print('     5)Salir.')
    o = input('Opción: ')