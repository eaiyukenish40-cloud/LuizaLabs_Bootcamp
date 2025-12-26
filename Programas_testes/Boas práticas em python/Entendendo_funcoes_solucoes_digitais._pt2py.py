def identificar_categoria_gadget(codigo):
    """
    Recebe uma string 'codigo' e retorna a categoria associada:
    - 'T': tablet
    - 'P': phone
    - 'N': notebook
    Se não corresponder, retorna 'unknown'.
    """
    if codigo[0] == 'T':
        return 'tablet'
    elif codigo[0] == 'P':
        return 'phone'
    elif codigo[0] == 'N':
        return 'notebook'
    else:
        return 'unknown'
    # TODO: Implemente a lógica para identificar a categoria do gadget
    # Dica: Verifique a primeira letra do código para determinar a categoria
    # Tipo esperado: 'codigo' é uma string não vazia

    pass  # Remova este pass ao implementar a solução

# Leitura da entrada (espera-se uma string representando o código do gadget)
codigo_gadget = input().strip()

# Chamada da função e saída do resultado
categoria = identificar_categoria_gadget(codigo_gadget)

print(categoria)  # Deve imprimir uma das categorias ou 'unknown'