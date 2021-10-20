# 13) Escreva um programa que leia o raio de um círculo e faça duas funções:
# uma função chamada área que calcula e retorna a área do círculo e outra
# função chamada perímetro que calcula e retorna o perímetro do círculo.

PI = 3.14159265359


def main():
    raio = float(input("Escreve o raio da circunferência: "))
    calculaArea(raio)
    calculaPerimetro(raio)


def calculaArea(raio):
    area = PI * (raio ** 2)
    print(area)


def calculaPerimetro(raio):
    perimetro = 2 * PI * raio
    print(perimetro)


if __name__ == "__main__":
    main()
