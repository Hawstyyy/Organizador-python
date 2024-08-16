import os
import shutil as sh
from tkinter import *
from tkinter import ttk,filedialog

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

  top= Toplevel(root)
  top.geometry("200x100")
  top.title("Popup")
  Label(top, text= "Pasta organizada!", font=("Arial", 12)).place(relx=0.5, rely=0.4, anchor=CENTER)
  Button(top, text= "Close", command=top.destroy, font=("Arial", 12)).place(relx=0.5, rely=0.7, anchor=CENTER)

root = Tk()

root.title("Python Organizer")
root.geometry("400x300")
root.resizable(False, False)

ttk.Label(root, text="Pasta selecionada:", font=("Arial",20, "bold")).place(relx=0.5, rely=0.2, anchor=CENTER)
folder_label = ttk.Label(root, font=("Arial", 10))
folder_label.place(relx=0.5, rely=0.35, anchor=CENTER)

btn1 = Button(root, text="Selecionar pasta", command=diretorio, height=2, width=20)
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)
btn1.config(background="green", foreground="white", font=("Arial", 10))

btn2 = Button(root, text="Organizar pasta", command=organizar, height=2, width=20)
btn2.place(relx=0.5, rely=0.65, anchor=CENTER)
btn2.config(background="green", foreground="white", font=("Arial", 10))

root.mainloop()