def exibirValor2Casas(valor):
    print("{:.2f}".format(valor))


def myApp():
    media = calcularMedia(8, 4)
    exibirValor2Casas(media)

    media2 = calcularMedia(10, 9)
    exibirValor2Casas(media2)

    exibirValor2Casas(calcularMedia(5, 9))

    val1temp = float(input("Digite o valor 1:"))
    val2temp = float(input("Digite o valor 2:"))
    exibirValor2Casas(calcularMedia(val1temp, val2temp))


def calcularMedia(valor1, valor2):
    return (valor1 + valor2) / 2.0


def main():
    myApp


if __name__ == "__main__":
    main()
