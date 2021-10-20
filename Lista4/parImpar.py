# 12) Faça uma função que recebe um número inteiro por parâmetro e retorna
# verdadeiro se for par e falso se for ímpar

def distingueParImpar(valor):
    valor = valor % 2
    if valor == 0:
        valor = True
    else:
        valor = False
    print(valor)


def main():
    distingueParImpar(7)


if __name__ == "__main__":
    main()
