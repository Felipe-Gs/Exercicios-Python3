import random
from time import sleep
def tempo():
    print('PEDRA')
    sleep(1)
    print('PAPELL')
    sleep(1)
    print('TESOURA!!!')


def continuar():
    opcao = input('quer continuar S/N:').upper()
    if opcao == 'N':
        print('vc saiu do jogo!!!')
        exit()



while True:
    jogador = input('Digite : pedra, papel ou tesoura: ')
    tempo()
    lista = ['pedra', 'papel', 'tesoura']
    comp = random.choice(lista)
    while True:
        if jogador == 'pedra' and comp == 'papel':
            print('voce perdeu! papel ganha de pedra! hehe')
            continuar()
            break
        elif jogador == 'pedra' and comp == 'tesoura':
            print('voce ganhou! pedra ganha de tesoura!')
            continuar()
            break
        elif jogador == 'pedra' and comp == 'pedra':
            print('deu empate! pedra com pedra')
            continuar()
            break
        elif jogador == 'papel' and comp == 'pedra':
            print('voce ganhou! papel ganha de pedra!')
            continuar()
            break
        elif jogador == 'papel' and comp == 'tesoura':
            print('voce perdeu! papel perde para tesoura!')
            continuar()
            break
        elif jogador == 'papel' and comp == 'papel':
            print('empatou ! papel empata com papel!')
            continuar()
            break
        elif jogador == 'tesoura' and comp == 'papel':
            print('voce ganhou! tesoura ganha de papel!')
            continuar()
            break
        elif jogador == 'tesoura' and comp == 'pedra':
            print('voce perdeu! tesoura perde para pedra!')
            continuar()
            break
        elif jogador == 'tesoura' and comp == 'tesoura':
            print('empatou! tesoura empata com tesoura!')
            continuar()
            break