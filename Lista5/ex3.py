# 3. Para o exercício 2, crie uma função chamada mostrarCidades(lista) que deve receber uma lista por
# parâmetro. Este método deve exibir o nome das cidades, uma a uma e uma embaixo da outra.

def main(list = [1,2,3]):
    for cidade in list:
        print(f'{cidade}')

if __name__ == "__main__":
    main()
