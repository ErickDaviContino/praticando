# Crie uma função que receba como parâmetro um valor, verifique se este valor é negativo, e
# neste caso converta ele para positivo retornando-o ao usuário


def convertePositEmNegat(valor):
    if(valor < 0):
        return valor * -1
    return valor


print(convertePositEmNegat(8))
