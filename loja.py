'''quantidade = int(input('quantos produtos o senhor comprou?'))
preco = quantidade * 1.99
print(preco)'''
print("====TABELA DE PREÇOS====")
for c in range(1, 51):
    print(c, "- R$", c * 1.99)

quantidade = int(input('quantos produtos o senhor comprou?')) 
preco = quantidade * 1.99
print(preco, " é o preço que voce tem que pagar!") 
dinheiro = float(input('com quanto dinheiro vc pretende pagar?')) 
if dinheiro <= preco:
    print('dinheiro insuficiente')
else:
    troco = dinheiro - preco
    print("obrigado, esse é seu troco:",troco )
