'''print('Hello World') #Dentro do VSCode
a = 'batata'
print(a is 'batata')
print('a' in 'batata')

def sacar (valor):
    conta = 500
    if conta > valor:
        conta -= valor
        print(f'Seu saque foi realizado valor retirado \033[0:32mR${valor}\033[m')

sacar(100)'''

nome = 'Guanavara'
print(nome[::-1])
print(nome[2:7:2])

lista = [1,2,3,4,5,6]
#lista.reverse()
print(lista)
print(lista[::-1])
print(sorted(lista,reverse=True))
print(lista)
teste = [range(10) ]
print(teste)
a= list('python')
print(a)
tupla = ('s','b','c')
a = input('Digite um valor: ')
tupla2 = (a,) #caso em que pode-se ocorrer um problema do interpretador não entender que é tupla
print(f'A tupla é {tupla2}')
a = input('Digite um valor: ')
print(f'A tupla é {tupla2}')
print(isinstance(tupla2,tuple))