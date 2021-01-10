import random
while True:
    jogador1 = input('digte sua escolha, (cara ou coroa)')
    jogador2 = input('digite sua escolha, (cara ou coroa)')
    if jogador1 == jogador2:
        print('opceoes invalidas, os jogadores nao podem escolher a mesma opcoa:')
        continue

    opcoes = ['cara', 'coroa']
    maqui = random.choice(opcoes)
    if jogador1 == maqui:
        print('quem ganhou foi o jogador 1!')
    else:
        print('quem ganhou foi o jogador 2!')    

