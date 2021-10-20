nota1 = float(input("Digite a nota da N1: "))
nota2 = float(input("Digite a nota da N2: "))
escolha = int(
    input("Escolha 1 para calcular a média ponderada e 2 para média aritimética: "))

if escolha == 1:
    ponderada = (nota1 * 4 + nota2 * 6) / 10
    print("Sua média é: {}".format(ponderada))
elif escolha == 2:
    aritimetica = (nota1 + nota2) / 2
    print("Sua média é: {}".format(aritimetica))
else:
    print("Opção inválida!")