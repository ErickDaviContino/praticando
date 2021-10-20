ladoA = float(input("Digite o lado A do triângulo: "))
ladoB = float(input("Digite o lado B do triângulo: "))
ladoC = float(input("Digite o lado C do triângulo: "))

if (ladoA + ladoB < ladoC) or (ladoA + ladoC < ladoB) or (ladoB + ladoC < ladoA):
    print("Não é um triângulo")
elif ladoA == ladoB == ladoC:
    print("Seu tiângulo é equilatero")
elif (ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC):
    print("Seu triângulo é Isósceles")
else:
    print("Seu triangulo é Escaleno")
