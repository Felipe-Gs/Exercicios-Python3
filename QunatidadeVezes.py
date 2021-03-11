#20.Crie uma função que recebe uma string A e um caractere B, 
# e retorna um inteiro representando a quantidade de vezes que B aparece em A

def numero(a,):
    lista = []
    frase = []
    op = str(input('qual caractere: '))
    for c in a:
        lista.append(c)
    for b in lista:
        if b == op:
            frase.append(b)


    print(lista)
    print(len(frase))



a = input('diga uma frase, ou algo do tipo: ')
numero(a,)