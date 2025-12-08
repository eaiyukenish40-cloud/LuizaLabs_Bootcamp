print('Hello World') #Dentro do VSCode
a = 'batata'
print(a is 'batata')
print('a' in 'batata')

def sacar (valor):
    conta = 500
    if conta > valor:
        conta -= valor
        print(f'Seu saque foi realizado valor retirado \033[0:32mR${valor}\033[m')

sacar(100)