import os
import time
import shutil as sh
from tkinter import *
from tkinter import filedialog

root = Tk()
root.withdraw()
path = filedialog.askdirectory()
exten = []

try:
  dir_pasta = os.mkdir(f"{path}/Pastas")
  print("Executando...")
  time.sleep(3)
except:
  print("Executando...")
  time.sleep(3)

for arquivo in os.listdir(path):
  arq_path = os.path.abspath(f"{path}/{arquivo}")
  if os.path.isfile(arq_path) == True:
    caminho, tipo = os.path.splitext(arq_path)
    exten.append(tipo)

for nome in exten:
  if nome not in os.listdir(path):
    print(f"Criando pasta: {nome}")
    time.sleep(2)
    os.mkdir(f"{path}/{nome}")
  else:
    print(f"Pasta {nome} já presente")

for arquivo in os.listdir(path):
  arq_path = os.path.abspath(f"{path}/{arquivo}")
  if os.path.isfile(arq_path) == True:
    caminho, tipo = os.path.splitext(arq_path)
    sh.move(arq_path, f"{path}/{tipo}")

print("Finalizando...")
time.sleep(3)
print("Pronto!")