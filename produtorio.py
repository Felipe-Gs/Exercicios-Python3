# Produtorio
import math


def produtorio(x, y):
    lista = []
    b = len(lista)
    for c in range(x):
        if x == 1:
            break
        prod = y ** x 
        print(prod)
        lista.append(prod)
        x = x-1
    a = math.prod(lista)
    print(a*2)
    

x = int(input('digite um numero de x: '))
y = int(input('digite um numero de y: '))
produtorio(x, y)