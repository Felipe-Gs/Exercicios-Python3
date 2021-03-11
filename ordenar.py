#10 Ordenar
def ordenar():
    lista = []
    for c in range(20):
        lista.append(int(input('diga um valor: ')))
    lista.sort()
    print(lista)

ordenar()