import os
import shutil as sh
print(os.getcwd())

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
    print("- Pasta já presente")

for arquivo in os.listdir(path):
  arq_path = os.path.abspath(f"{path}/{arquivo}")
  if os.path.isfile(arq_path) == True:
    caminho, tipo = os.path.splitext(arq_path)
    sh.move(arq_path, f"{path}/{tipo}")

print("Encerrando...")