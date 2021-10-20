# 14) Escreva um programa para ler as notas de duas provas. Faça uma função que
# receba as duas notas por parâmetro e calcula a média destes valores. Depois
# disso o programa deve exibir a mensagem “Você foi Aprovado!” ou “Você foi Reprovado!”.
# Esta operação de escrita também deve estar em uma função.
# Considere 6.0 a média mínima para aprovação.

def main():
    media = calculaMedia(6, 6)
    mensagemReprovadoAprovado(media)


def calculaMedia(nota1, nota2):
    return (nota1 + nota2) / 2


def mensagemReprovadoAprovado(media):
    if media < 6:
        print("Você foi Reprovado!")
    else:
        print("Você foi Aprovado!")


if __name__ == "__main__":
    main()
