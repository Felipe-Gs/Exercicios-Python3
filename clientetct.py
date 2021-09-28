import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as erro:
        print("A conexao falhou!!!")
        print("erro: {}".format(erro))
        sys.exit()

    print("Socket criado com sucesso")

    hostAlvo = input("digite o host ou ip a ser conectado")
    portaAlvo = input("digite a porta a ser conectada")

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print("cliente TCP conectado com sucesso no host: " + hostAlvo + "e" + portaAlvo)
    except socket.error as erro:
        print("a conexao falhou!!!")
        print('Erro: {}'.format(erro))
        sys.exit()

if __name__ == "__main__":
    main()