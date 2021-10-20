valor = float(input("Digite um número: "))

if valor < 0:
    novoValor = valor * (-1)
    print("O novo valor positivo é: ", novoValor)
else:
    print(valor)
