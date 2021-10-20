# 17) Faça um programa para uma calculadora com as seguintes operações:
# adição, subtração, multiplicação e divisão. O programa começa apresentando
# ao usuário um menu de opções.

import os


def menu():
    while True:
        layout()
        escolha = recebeEscolha()

        if escolha == 1:
            adição()
            os.system("pause")
        elif escolha == 2:
            subtração()
            os.system("pause")
        elif escolha == 3:
            multiplicacao()
            os.system("pause")
        elif escolha == 4:
            divisão()
            os.system("pause")
        elif escolha == 5:
            print("\nPrograma finalizado!!")
            break
        else:
            print("\nOpção inválida! Favor digite um número de 1 a 5.")
            os.system("pause")


def layout():
    os.system('CLS')
    print("Bem-vindo ao menu calculadora!")
    print("Para prosseguir escolha um item de nosso menu (1 - 5): \n")
    print("1 - Adição;")
    print("2 - Subtração;")
    print("3 - Multiplicação;")
    print("4 - Divisão;")
    print("5 - Finaliza o programa;\n")


def recebeEscolha():
    return int(input("O que desejas fazer: "))


def recebeValor():
    # ??
    pass


def adição():
    valor1 = float(input("\nDigite o primeiro valor a ser somado: "))
    valor2 = float(input("Digite o segundo valor a ser somado: "))
    return print("\nO resultado da sua soma é: {:.2f}\n".format(valor1 + valor2))


def subtração():
    valor1 = float(input("\nDigite o primeiro valor a ser subtraido: "))
    valor2 = float(input("Digite o segundo valor a ser subtraido: "))
    return print("\nO resultado da sua subtração é: {:.2f}\n".format(valor1 - valor2))


def multiplicacao():
    valor1 = float(input("\nDigite o primeiro valor a ser multiplicado: "))
    valor2 = float(input("Digite o segundo valor a ser multiplicado: "))
    return print("\nO resultado da sua multiplicação é: {:.2f}\n".format(valor1 * valor2))


def divisão():
    valor1 = float(input("\nDigite o primeiro valor a ser dividido: "))
    valor2 = float(input("Digite o segundo valor a ser dividido: "))
    return print("\nO resultado da sua divisão é: {:.2f}\n".format(valor1 / valor2))


def main():
    menu()


if __name__ == "__main__":
    main()
