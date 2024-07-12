import os
import shutil as sh


exten = []
pastas = []
path = input(r"- Insira o diretório: ")

try:
  dir_pasta = os.mkdir(f"{path}/Pastas")
  print("Executando...")
except:
  print("Executando...")

for arquivo in os.listdir(path):
  arq_path = os.path.abspath(f"{path}/{arquivo}")
  if os.path.isfile(arq_path) == True:
    caminho, tipo = os.path.splitext(arq_path)
    exten.append(tipo)

for nome in exten:
  if nome not in os.listdir(path):
    os.mkdir(f"{path}/{nome}")
  else:
    print("ja tem")

for arquivo in os.listdir(path):
  arq_path = os.path.abspath(f"{path}/{arquivo}")
  if os.path.isfile(arq_path) == True:
    caminho, tipo = os.path.splitext(arq_path)
    sh.move(arq_path, f"{path}/{tipo}")

# for pasta in os.listdir(path):
#   pasta_path = os.path.abspath(f"{path}/{pasta}")
#   if os.path.isdir(pasta_path) == True:
#     nome = os.path.basename(pasta_path)
#     banco_de_dados = open("extensoes.txt", "r")
#     print(banco_de_dados.readlines())
#     if nome in banco_de_dados.readlines():
#       continue
#     else:
#       sh.move(pasta_path, f"{path}/Pasta")
#       banco_de_dados.close()