import os
import shutil as sh
from tkinter import *
from tkinter import ttk,filedialog,messagebox

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

root = Tk()

root.title("Python Organizer")
root.geometry("400x300")
root.resizable(False, False)

ttk.Label(root, text="Pasta selecionada:", font=("Arial",20, "bold")).place(relx=0.5, rely=0.2, anchor=CENTER)
folder_label = ttk.Label(root, font=("Arial", 10))
folder_label.place(relx=0.5, rely=0.35, anchor=CENTER)

btn1 = ttk.Button(root, text="Selecionar pasta", command=diretorio, )
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)

btn2 = ttk.Button(root, text="Organizar pasta", command=organizar)
btn2.place(relx=0.5, rely=0.65, anchor=CENTER)

root.mainloop()