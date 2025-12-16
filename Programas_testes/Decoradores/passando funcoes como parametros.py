def pessoa_caracteristica(funcao_1,funcao_2):
    nome = str(input('Digite o 1° nome: '))
    sobrenome = str(input('Digite o sobrenome: '))
    return f'o meu nome é {funcao_1(nome,sobrenome)}. Minha idade: {funcao_2('1999')}'
    

def nome_completo(nome,sobrenome):
    nome_pessoa = nome + ' ' + sobrenome
    return nome_pessoa

def idade_pessoa(ano):
    from datetime import datetime
    data_atual = 2025
    idade = int(data_atual) - int(ano)
    return idade

print(pessoa_caracteristica(nome_completo,idade_pessoa))