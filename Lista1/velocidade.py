
velocidadeInicial = float(input("Digite a velocidade inicial: "))
deltaS = float(input("Digite a distância percorrida: "))
aceleracao = float(input("Digite a aceleração do objeto: "))

velocidadefinal = (velocidadeInicial ** 2 + 2 * aceleracao * deltaS) ** (1/2)

print("A velocidade final é de: ", velocidadefinal)
