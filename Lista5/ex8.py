# 8. Crie um dicionário contendo o nome de um conjunto de frutas e os seus respectivos Preços. Ao final,
# exiba da seguinte forma (sem a borda)


listaFrutas = {"banana": 2, "maçã": 5, "morango": 3, "abacaxi": 10, "abacate": 8, "abobora tamanho ferrari": 999}

def main():
    for fruta, preco in listaFrutas.items():
        print(f'fruta R${(preco)}')

if __name__ == "__main__":
    main()