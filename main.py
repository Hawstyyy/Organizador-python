import os
import shutil as sh
import customtkinter
from customtkinter import filedialog
from tkinter import messagebox

exten = []

def diretorio():
  global folder_selected
  folder_selected = filedialog.askdirectory()
  folder_label.config(text=folder_selected)

def organizar():
  for arquivo in os.listdir(folder_selected):
    arq_path = os.path.abspath(f"{folder_selected}/{arquivo}")
    if os.path.isfile(arq_path) == True:
      caminho, tipo = os.path.splitext(arq_path)
      exten.append(tipo)

  for nome in exten:
    if nome not in os.listdir(folder_selected):
      print(f"Criando pasta: {nome}")
      os.mkdir(f"{folder_selected}/{nome}")
    else:
      print(f"Pasta {nome} já presente")

  for arquivo in os.listdir(folder_selected):
    arq_path = os.path.abspath(f"{folder_selected}/{arquivo}")
    if os.path.isfile(arq_path) == True:
      caminho, tipo = os.path.splitext(arq_path)
      sh.move(arq_path, f"{folder_selected}/{tipo}")

  messagebox.showinfo("Concluído", "Pasta organizada!")

