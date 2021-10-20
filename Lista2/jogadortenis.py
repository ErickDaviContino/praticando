idade = int(input("Digite sua idade: "))

if idade >= 5 and idade <= 7:
    print("Categoria Infantil 1")
elif idade >= 8 and idade <= 11:
    print("Categoria Infantil 2")
elif idade >= 12 and idade <= 14:
    print("categoria Juvenil 1")
elif idade >= 15 and idade <= 17:
    print("categoria Juvenil 2")
elif idade >= 18:
    print("categoria Adulto")
else:
    print("Idade insuficiente")
