'''Separar as funções existentes de saque, depósito e extrato em funções dedicadas.
Novas Funções:
Criar uma nova função para cadastrar usuário (cliente).
Criar uma nova função para cadastrar conta bancária'''

from funcoes_modularizadas_desafio1 import saque,deposito,extrato_view, criar_cadastro,criar_conta_corrente,cpf_check
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
cadastros_clientes = []
contas_cadastradas_final = []
AGENCIA = '0001'
conta_contador = 1

print('Seja bem vindo ao seu primeiro acesso')
conta_contador = criar_cadastro(cadastros_clientes,AGENCIA,conta_contador,contas_cadastradas_final) #recebe o valor de retorno do próximo número da conta a ser retornada.


while True:

    opcao = str(input(menu)).strip().lower()

    if opcao == "d":
       saldo, extrato = deposito(saldo,extrato) # a função retorna um tupla
       print(f'Depósito concluído com sucesso. R${saldo}')
    

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES: # melhoria. Se o número de saque for excedido, não executa a função.
            extrato, saldo, numero_saques = saque(limite=limite,saldo=saldo,numero_saques=numero_saques,limite_saques=LIMITE_SAQUES,extrato=extrato) # retorna extrato,saldo,numero_saques
            

        else:
            print(f'Você atingiu o limite de saques por hoje. Volte amanhã')
        

    elif opcao == "e":
        extrato_view(extrato,saldo=saldo)

    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

