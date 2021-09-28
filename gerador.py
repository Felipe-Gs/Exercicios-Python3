import itertools

senha = input("String a ser permutada: ")
resultado = itertools.permutations(senha, len(senha))

for i in resultado:
    print(''.join(i))