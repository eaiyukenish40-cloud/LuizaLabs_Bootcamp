class pessoas:
    def __init__(self,nome,sobrenome,idade,saldo_init):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.conta_bancaria = saldo_init
        print(f'Seu nome completo é {self.nome} {self.sobrenome}, e possui {self.idade} anos ')

    def qtd_dinheiro(self,valor):
        self.conta_bancaria += valor
        print('Você tem que pagar imposto de renda' if self.conta_bancaria > 5000 else 'Você não precisa pagar IR' )
        
               
        
    def maior_idade(self):
        if self.idade < 18:
           return False
        else:
            print('É maior de idade')
            return True
        
    def emitir_cnh(self):
        verificacao = self.maior_idade()
        if verificacao:
            print('Pode emitir CNH')
        else:
            print('Não pode emitir CNH')

carlos = pessoas('Carlos','Soares',25,6000)
carlos.qtd_dinheiro(3000)
carlos.maior_idade()