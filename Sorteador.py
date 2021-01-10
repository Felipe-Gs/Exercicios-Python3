import random
while True:
    usuario = int(input(' Tente acertar o numero que a maquina pensou! Digite um valor entre 0 e 5:'))
    maqui = random.randint(0, 5)
    if usuario == maqui:
        print(f'parabens! voce acertou... a maquina realmente pensou no numero {maqui}')
    else:
        print(f'voce errou a maquina pensou no numero {maqui}  e voce digitou {usuario}')
        