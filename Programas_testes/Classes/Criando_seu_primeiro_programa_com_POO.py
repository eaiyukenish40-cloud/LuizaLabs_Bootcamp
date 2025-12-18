class bicicleta:
    def __init__(self,cor,modelo,ano,valor,estado = 'parada'): # definicação das características da bicicleta
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor_venda = valor


    def buzinar(self):
        print('ding-dong')
        self.estado = 'buzinando'
    

    def parar(self):
        print('Bicicleta está parada')
        self.estado = 'parada'
    
    def correr(self):
        print('Bicicleta está correndo')
        self.estado = 'correndo'

    def obter_cor(self):
        return self.cor

bike_1 = bicicleta('azul','nike',1999,1000)
print(bike_1.obter_cor())