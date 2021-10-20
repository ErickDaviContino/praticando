# 2. Crie uma coleção que suportará nomes de cidades. Após isso, interaja com o usuário questionando-o a
# respeito de quantos elementos deseja inserir nesta lista. Em sequência, adicione nomes de cidades
# tantas quanto o número informado pelo usuário. Ao final, exiba a lista de cidades.

def main():
    cidades = []

    qtdCidades = int(input("Quantas cidades adicionará na lista? "))

    cont = 0
    while(cont < qtdCidades):
        novaCidade = input("Didite o nome da cidade: ")
        cidades.append(novaCidade)
        qtdCidades -= 1
    print(cidades)


if __name__ == "__main__":
    main()
