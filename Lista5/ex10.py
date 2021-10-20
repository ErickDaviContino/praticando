# 10. Considere o seguinte dicionário:
# dicio = {"name": "César Lattes", "country": "Brasil", "born": 1924, "role": "Físico"}
# Crie uma função que receba este dicionário e imprima a seguinte saída (sem a borda ao redor):

# Nome do Pesquisador: César Lattes
# País: Brasil
# Ano de Nascimento: 1924 – Profissão: Físico

dicio = {"name": "César Lattes", "country": "Brasil",
         "born": 1924, "role": "Físico"}

print("Nome do Pesquisador:", dicio["name"])
print("País: ", dicio["country"])
print("Ano de Nascimento:", dicio["born"], "-", "Profissão:", dicio["role"])
