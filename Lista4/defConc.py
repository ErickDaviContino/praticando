
# 10) Crie uma função main(). E chame no main as funções do exercício
# 5 e 6, testando com valores que não exijam interação com o usuário

def main():
    print(concatenaNomes("Erick Davi", "Contino"))
    concatenaNomesPrint("Gustavo Debeus", "Souza")


def concatenaNomes(nome, sobrenome):
    return nome + " " + sobrenome


def concatenaNomesPrint(nome, sobrenome):
    print(nome + " " + sobrenome)


if __name__ == "__main__":
    main()
