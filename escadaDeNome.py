# escada de nome
def nome(nome):
    nome = str(input('Digite o seu nome: ')).upper()
    for i in range(0, len(nome)+1):
        print(nome[:i])
nome(nome)

#==========================================

# Escada de nomes invertida
def nome(nome):
    nome = str(input('Digite o seu nome: ')).upper()
    for i in range(0, len(nome)+1):
        print(nome[i:])
nome(nome)
