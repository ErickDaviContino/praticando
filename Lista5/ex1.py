# 1. Crie uma coleção que suportará números inteiros. Após isso, adicione a esta lista cinco valores inteiros.
# Em sequência, exiba estes valores. Por fim, ordene os valores e remove o elemento da posição 3. Exiba
# novamente a lista.

def exercicio1():
    lista = [2, 1, 3, 4, 0]
    print(lista)
    listaOrdenada = sorted(lista)
    listaCortada = listaOrdenada.pop(2)
    print(listaCortada)
