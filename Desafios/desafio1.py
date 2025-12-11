'''Separar as funções existentes de saque, depósito e extrato em funções dedicadas.
Novas Funções:
Criar uma nova função para cadastrar usuário (cliente).
Criar uma nova função para cadastrar conta bancária'''

from funcoes_modularizadas_desafio1 import saque,deposito
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

while True:

    opcao = str(input(menu)).strip().lower()

    if opcao == "d":
       resultado_deposito = deposito(saldo,extrato) # a função retorna um tupla
       saldo = resultado_deposito[0]
       extrato = resultado_deposito[1]
       print(f'Depósito concluído com sucesso. R${saldo}')
    

    elif opcao == "s":
        resultado_saque = saque(limite,saldo,numero_saques,LIMITE_SAQUES,extrato) # retorna extrato,saldo,numero_saques, valor
        extrato = resultado_saque[0]
        saldo = resultado_saque[1]
        numero_saques = resultado_saque[2]
        valor_saque = resultado_saque[3]
        print(f'Saque de R${valor_saque} realizado com sucesso. Você pode sacar mais {LIMITE_SAQUES - numero_saques} vez(es)')

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
