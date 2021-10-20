def main():
    pergunta_nota()

    calcula_media()

    exibe_media()


def pergunta_nota(nota1, nota2, nota3, nota4):
    print("Digite suas 4 notas, Ex. (nota1 nota2 nota3 nota4: ")

    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    nota4 = float(input())


def calcula_media(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return media


def exibe_media(media):
    print(media)
    return media


if __name__ == "__main__":
    main()