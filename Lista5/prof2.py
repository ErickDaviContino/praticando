def mostraCidade(listaCidades):
    for umaCidade in listaCidades:
        print(umaCidade)


def adicionarCidadeLista(listaCidades):
    cidade = input(
        "informe o nome da cidade que você deseja adicionar na coleção: ")
    listaCidades.append(cidade)


def main():
    listaCidades = []
    qtsCidades = int(input("informe quantas cidades você deseja adicionar: "))

    while(qtsCidades != len(listaCidades)):
        adicionarCidadeLista(listaCidades)

    mostraCidade(listaCidades)


if __name__ == "__main__":
    main()
