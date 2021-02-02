signos = ['macaco', 'galo', 'cão', 'porco', 'rato', 'boi', 'tigre', 'coelho', 'dragão', 'serpente','cavalo', 'carneiro']
aux = int(input('diga seu ano:'))
aux = aux % 12
print(signos[aux])