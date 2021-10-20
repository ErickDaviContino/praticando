aresta = float(input("Digite o valor da aresta: "))

PI = 3.14
areaQuadrado = aresta * aresta
areaTriangulo = ((aresta ** 2) * 1.7320508075688772) / 4
areaCirculo = PI * (aresta ** 2)

cond = areaCirculo >= areaQuadrado

print("A área do círculo é {:.2f} e a área do quadrado é {:.2f}. O círculo possuí área maior que a do quadrado?? {}".format(areaCirculo, areaQuadrado, cond))
