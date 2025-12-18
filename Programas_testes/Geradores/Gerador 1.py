def gerador(lista: list[int]):
    for numero in lista:
        yield numero*2

for valor in gerador(lista = [1,2,43]):
    print(valor)