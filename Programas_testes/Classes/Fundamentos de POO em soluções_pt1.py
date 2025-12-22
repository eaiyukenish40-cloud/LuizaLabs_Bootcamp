class Mensagem:
    def __init__(self, remetente, conteudo):
        # Inicializa os atributos da mensagem
        self._remetente = remetente
        self._conteudo = conteudo
    
 
    @property
    def remetente(self):
            return self._remetente
    
    @property  
    def conteudo(self):
        return self._conteudo
 
    
    def exibir(self):
        return f'{self.remetente}: {self.conteudo}'
        


# Lê o nome do remetente (primeira linha da entrada)
remetente = input('Digite seu nome: ')
# Lê o conteúdo da mensagem (segunda linha da entrada)
conteudo = input('Digite a mensagem que será enviada (até 69 caracteres): \n')[0:69]

# Cria o objeto Mensagem com os dados recebidos
mensagem = Mensagem(remetente, conteudo)

# Imprime a mensagem formatada pela função exibir (saída conforme especificação)
print(mensagem.exibir())

