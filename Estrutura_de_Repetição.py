usuario = input("digite seu nome:")
senha = input("digite sua senha:")
while usuario == senha:
    print("Invalido, nome e senha não podem ser iguais..... digite novamente:")
    usuario = str(input("digite seu nome:"))
    senha = str(input("digite sua senha:"))
    break

print("Cadastro efetuado com succeso!")

    
   
    
