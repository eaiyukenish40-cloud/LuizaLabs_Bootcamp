def inner_function(z): # teste de funções internas
    print(f'função pai. O resultado depende do meu número {z} e dos meus filhos. ')
    def child_1(x):
        print(f'ola sou o primeiro filho, meu numero é {x}')
        return x*2
    def child_2(y):
        print(f'ola sou o segundo filho, meu numero é {y}')
        return child_1(y) #teste de retorno com função
    
    resultado = (child_1(5) + child_2(10))*z
    return resultado


def seletor():
    from random import randint
    return randint(int(input('Digite um número inicial: ')),int(input('Digite um número final: ')))


print(inner_function(seletor)) #teste de chamada de função por função