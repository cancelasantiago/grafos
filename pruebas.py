import math

array = [0,4,9,7,8,1]
MEM = [0,0,0,0,0,0]
aux = 0
j = 6
i = 0
max = 0
while (j>0):
    while (i<6):
        if aux <= array[i]:
            if max == 0:
                aux = array[i]
            if array[i] < MEM[max-1]:
                print (aux, ' ', MEM[max-1])
                aux = array[i]
        i = i+1
    MEM[6-j] = aux
    max = max + 1
    aux = 0
    j = j-1
    i = 0
print(MEM)