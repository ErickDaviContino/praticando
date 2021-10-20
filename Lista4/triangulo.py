# 15) Faça uma função que receba como parâmetro o número de lados de um polígono e:
# - Se o número de lados for igual a 3, escrever TRIÂNGULO.
# - Se o número de lados for igual a 4, escrever QUADRADO.
# - Se o número de lados for igual a 5, escrever PENTÁGONO.
# - Se o número de lados for diferente de 3, 4 ou 5, escrever VALOR INVÁLIDO.

def exibeTipoPoligono(qtdLados: int):
    if qtdLados == 3:
        print("TRIÂNGULO")
    elif qtdLados == 4:
        print("QUADRADO")
    elif qtdLados == 5:
        print("PENTÁGONO")
    else:
        print("VALOR INVÁLIDO")


def main():
    exibeTipoPoligono(3)


if __name__ == "__main__":
    main()
