#Crie uma função, que utilizando um desvio condicional retorne true se o valor 
# for negativo e falso se ele for positivo

def verificarValorNegativo(valor):
    if(valor < 0):
        return True
    else:
        return False

def exibeNomeCompleto(nome, sobrenome):
    print(nome + sobrenome)

verificarValorNegativo(-32)
#ou
resultado = verificarValorNegativo(-32)
#ou
print(verificarValorNegativo(-32))


resultado exibeNomeCompleto("André", "Santana")
