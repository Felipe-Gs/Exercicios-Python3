# Uniao de listas
def vetores():
    lista = []
    lista2 = []
    for c in range(10):
        lista.append(float(input('diga um valor: ')))
    print('aqui começa os valores da lista 2')
    for c in range(10):
        lista2.append(float(input('diga um valor: ')))
    uniao = lista + lista2
    print('a união das duas listas é: ', uniao)
vetores()