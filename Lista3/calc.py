while True:
    print("Digite a nota da sua primeira avaliação: ")
    nota1 = float(input())

    print("Digite a nota da sua segunda avaliação: ")
    nota2 = float(input())

    print("Digite a nota da sua terceira  avaliação: ")
    nota3 = float(input())

    print("Digite a nota da sua quarta avaliação: ")
    nota4 = float(input())

    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 6:
        print(
            "Parabéns, você passou de ano. Sua média é de: {:.2f}".format(media))
    else:
        print("Você é um bosta. Sua média é de: {:.2f}".format(media))
