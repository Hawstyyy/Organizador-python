import os
import time
import shutil as sh
from tkinter import *
from tkinter import filedialog

root = Tk()
root.withdraw()
path = filedialog.askdirectory()
exten = []

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

for arquivo in os.listdir(path):
  arq_path = os.path.abspath(f"{path}/{arquivo}")
  if os.path.isfile(arq_path) == True:
    caminho, tipo = os.path.splitext(arq_path)
    sh.move(arq_path, f"{path}/{tipo}")

print("Finalizando...")
time.sleep(3)
print("Pronto!")