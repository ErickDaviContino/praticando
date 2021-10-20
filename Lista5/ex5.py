# 5. Crie uma coleção que armazenará apenas as notas de alunos de uma turma. Após isso, crie algumas
#	funções que permitirão (i) cadastrar notas dos alunos (ii) exibir todas as notas (iii) calcular a média das
#	notas, retornando o valor da média e (iv) exiba a média.

notasAlunos = []

def cadastrarNota():
  notasAlunos.append(float(input()))
  
def exibirNotas():
    for indice in range(len(notasAlunos)):
        print("Nota" + str(indice+1) +": " + str(notasAlunos[indice]))
    
def calcularMedia():
  	media = 0.0
  	for nota in notasAlunos:
  	    media += nota
  	media /= len(notasAlunos)
  	return media
  
def exibirMedia():
  	print("Média = " + str(calcularMedia()))

cadastrarNota()
cadastrarNota()
cadastrarNota()

exibirNotas()

exibirMedia()