# 7. Crie uma função que seja capaz de solicitar ao usuário uma nova chave e um novo valor para um
# dicionário. Esta função deve receber um dicionário e garantir que as “modificações” realizadas na
# função sejam aplicadas ao dicionário na função que invocou este procedimento.

def mudarDicionario(dict = {}):
    chave = str(input('Digite a chave: '))
    valor = str(input('Digite o valor: '))
    dict[chave] = valor
    return dict