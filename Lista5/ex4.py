# 4. Crie uma função que recebe a lista de cidades do exercício 2 e que exibe somente as cidades com mais
# de 7 letras na composição do seu nome.

def exercicio4(cidades):
    for cidade in cidades:
        if(len(cidade) >= 7):
            print(cidade)