'''Separar as funções existentes de saque, depósito e extrato em funções dedicadas.
Novas Funções:
Criar uma nova função para cadastrar usuário (cliente).
Criar uma nova função para cadastrar conta bancária'''

from funcoes_modularizadas_desafio1 import saque,deposito,extrato_view, criar_cadastro #criar_conta_corrente
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
criar_cadastro = []

while True:

    opcao = str(input(menu)).strip().lower()

    if opcao == "d":
       resultado_deposito = deposito(saldo,extrato) # a função retorna um tupla
       saldo = resultado_deposito[0]
       extrato = resultado_deposito[1]
       print(f'Depósito concluído com sucesso. R${saldo}')
    

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES: # melhoria. Se o número de saque for excedido, não executa a função.
            resultado_saque = saque(limite=limite,saldo=saldo,numero_saques=numero_saques,limite_saques=LIMITE_SAQUES,extrato=extrato) # retorna extrato,saldo,numero_saques
            extrato = resultado_saque[0]
            saldo = resultado_saque[1]
            numero_saques = resultado_saque[2]
        else:
            print(f'Você atingiu o limite de saques por hoje. Volte amanhã')
        

    elif opcao == "e":
        extrato_view(extrato,saldo=saldo)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
