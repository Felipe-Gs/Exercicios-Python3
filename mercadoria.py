class Mercadoria:

    def __init__(self, preco, marca):
        self.preco = preco
        self.marca = marca

    def Mudar_preco(self, Mudar):
        opcao = input('deseja mudar o preco do produto?(s/n)')
        if opcao == 's':
            self.preco += Mudar
            print('o novo valor é',self.preco)



arroz = Mercadoria(12.50, 'pai_joão')        
print('a marca do arroz é', arroz.marca)
print('o preço do arroz é ', arroz.preco)
arroz.Mudar_preco(2.0)

macarrao = Mercadoria(3.50, 'tijubano')
print('o preco do macarrão é', macarrao.preco)
print('a marca do macarrão é', macarrao.marca)
macarrao.Mudar_preco(23)


       
