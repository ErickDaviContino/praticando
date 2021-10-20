# 16) Escreva um programa que solicita um valor inteiro ao usuário e exibe a tabuada do número lido.

def lerNumero():
    return int(input("Qual número gostaria de saber a tabuada? "))


def tabuada():
    numero = lerNumero()
    cont = 0
    while cont <= 10:
        print("{0} x {1} = {2}".format(cont, numero, (cont * numero)))
        cont += 1


def main():
    tabuada()


if __name__ == "__main__":
    main()
