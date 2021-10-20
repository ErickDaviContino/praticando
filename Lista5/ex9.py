#	9. Crie um dicionário que seja capaz de armazenar as peças necessárias para montar um computador.
#	Considere que este computador precisa ter (i) placa-mãe (ii) processador (iii) memória ram (iv)
#	componente de armazenamento não volátil (hd ou ssd) (v) placa de vídeo (vi) fonte (vii) gabinete.
#	a - Para isso: solicite ao usuário as informações que serão utilizadas para preencher cada uma
#	das chaves.
#	b - Exiba o resultado do dicionário da seguinte forma (sem a borda):

#	Este é apenas um exemplo
#	Placa Mãe: ASUS Tuf Gaming x570-plus Processador: Ryzen 5 – 3600
#	Placa de Vídeo: Geforce Rtx 2060 Ventus – MSI Armazenamento: 512 GB - SSD
#	Fonte: Corsair 750W
#	Memória Ram: XPG 8GB 3000 MHz
#	Gabinete: RedDragon WheelJack

def montarComputador():
    computador = {"placaMae": input("Placa-mãe: "),
                  "processador": input("Processador: "),
                  "memoriaRam": input("Memória RAM: "),
                  "armazenamentoSecundario": input("Armazenamento secundário: "),
                  "placaVideo": input("Placa de vídeo: "),
                  "fonte": input("Fonte : "),
                  "gabinete": input("Gabinete: ")}
    return computador


def exibirComputador(computador):
    print("\nPlaca Mãe: " + str(computador["placaMae"]) +
          " Processador: " + str(computador["placaMae"]))
    print("Placa de video: " + str(computador["placaVideo"]) +
          " Armazenamento: " + str(computador["armazenamentoSecundario"]))
    print("Fonte: " + str(computador["fonte"]))
    print("Memória Ram: " + str(computador["memoriaRam"]))
    print("Gabinete: " + str(computador["gabinete"]))


print("Monte seu computador: ")
exibirComputador(montarComputador())
