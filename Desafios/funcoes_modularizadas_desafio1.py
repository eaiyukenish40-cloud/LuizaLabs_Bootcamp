def saque(*,limite,saldo,numero_saques,limite_saques,extrato):

    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite


    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return extrato,saldo,numero_saques, valor
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return extrato,saldo,numero_saques, valor
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f'Saque de R${valor} realizado com sucesso. Saldo restante R${saldo}. Você pode sacar mais {limite_saques - numero_saques} vez(es)')
        return extrato,saldo,numero_saques

    else:
        print("Operação falhou! O valor informado é inválido.")

def deposito(saldo,extrato):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")


def extrato_view(extrato,/,*,saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

#def criar_cadastro():

#def criar_conta_corrente():