#  Numero perfeito
def perfeito():
    print("Determina se um número n é perfeito\n")
    lista = []
    while len(lista) != 5:
        soma = 0
        if len(lista) == 5:
            break
        n = int(input("Digite o valor de n: "))
        for c in range(1,n):
            if n % c == 0:
                soma += c 

        if n == soma:
            print("O numero %d é perfeito" %(n))
            lista.append(soma)
        else: 
            print("O numero %d nao é perfeito\n" %(n))
  
    print('os 5 primeiros numeros perfeitos digitados foram: ', lista)
perfeito()