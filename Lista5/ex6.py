# 6. Crie uma lista contendo 20 números inteiros. Após isso, crie uma função que será responsável por
# retornar uma lista contendo apenas os valores pares da lista original. Ao final exiba esta lista.

def main():
    listaNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    listaNumPar = []

    for num in listaNum:

        if num % 2 == 0:
            listaNumPar.append(num)

    print(listaNumPar)


if __name__ == "__main__":
    main()
