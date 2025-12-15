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

def ler_nascimento():
    from datetime import datetime
    
    while True: #loop forçar a entrada correta de data de nascimento
        try:
            data_nasc = str(input('Digite a sua data de nascimento (ex: 01/12/1999): '))
            data_transformada = datetime.strptime(data_nasc,'%d/%m/%Y') # força o usuário a digitar no formato correto. Indo ao tratamento de erro.
            data_atual = datetime.now()
            if data_transformada > data_atual:
                print('A data não pode ser no futuro.')
                continue
            else:
                return data_transformada #fim da função com a condição atingida.
        except ValueError:
            print('Você digitou em um formato incorreto. Tente novamente.')

def check_estado(sigla): #função para conferir a existência do Estado.
    siglas_uf = (
        'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 
        'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 
        'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
    )
    while sigla not in siglas_uf:
        sigla = str(input('Estado incorreto, digite novamente: ').upper().strip()[0:2])
    return sigla

def cpf_check(): # função validadora do formato do cpf 
    while True:
        try:
            cpf = int(str(input('Digite seu cpf: '))[0:11]) #seleciona apenas 11 dígitos do cpf e transforma em número inteiro.
        except ValueError: #tratamento de erro para input de formato incorreto
            print('Print você digitou formato errado, tente novamente.')
        else:
            return cpf

def criar_cadastro(cadastros_clientes,AGENCIA,conta_contador,contas_cadastradas_final):
    usuario = []
    cpf = cpf_check() #chama a função cpf para conferir a data de nascimento
    for item in cadastros_clientes: # confere,a lista de informações em cada cliente cadastrado, confirmando se há ou não se o campo CPF tem informações únicas
        while cpf in item: #loop para impedir o usuário de cadastrar um cpf já existente no banco
            print('CPF já cadastrado. Tente novamente')
            cpf = cpf_check()
   
    # lower().capitalize().strip() é padronização do formato do input.
    nome = str(input('Digite seu nome: ')).lower().capitalize().strip()
    nascimento = ler_nascimento() #chama a função para conferir a data de nascimento
    estado = check_estado(str(input('Digite o Estado onde mora (sigla): ')).upper().strip()[0:2]) #função conferir a existência de um Estado
    cidade = str(input('Digite a cidade onde mora: ')).lower().capitalize().strip()
    rua = str(input('Digite apenas o nome da rua onde mora: ')).lower().capitalize().strip()
    n = int(input('Digite o número da sua residência: '))
    bairro = str(input('Digite o bairro onde mora: ')).lower().capitalize().strip()
    endereço = f'{rua},{n} - bairro:{bairro} - {cidade}/{estado}.'
    usuario = [nome,nascimento,cpf,endereço]
    cadastros_clientes.append(usuario[:]) #adiciona o novo usuário na lista antes de chamar

    #adição de funcionalidadeas
    
    if str(input('Deseja criar uma conta? \n[S].\n[N].\n')).strip().upper()[0] == 'S':
        print('Criando conta...')
        conta_contador = criar_conta_corrente(AGENCIA,conta_contador,contas_cadastradas_final,usuario) # associa o novo usuário a uma nova conta
    
    print('Cadastro finalizado com sucesso!')
    usuario.clear() #limpa a lista temporária do usuário momentaneo após salvar no cadastro permanente   

    return conta_contador, cpf


def criar_conta_corrente(AGENCIA,conta_contador,contas_cadastradas_final,usuario):
    contas_cadastradas_final.append([usuario[:],conta_contador,AGENCIA])
    conta_contador += 1 #numero da conta cadastrada do usuário 
    print('Conta criada com sucesso')
    return conta_contador
    