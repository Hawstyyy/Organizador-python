import os
import shutil as sh
import customtkinter as ctk
from tkinter import messagebox,filedialog

exten = []

def diretorio():
  global folder_selected
  folder_selected = filedialog.askdirectory()
  folder_label.configure(text=folder_selected)

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

root = ctk.CTk()

root.title("Python Organizer")
root.geometry("400x300")
root.resizable(False, False)

texto = ctk.CTkLabel(root, text="Pasta selecionada:", font=("Arial",20, "bold"), text_color="white")
texto.place(relx=0.5, rely=0.2, anchor="center")
folder_label = ctk.CTkLabel(root, font=("Arial", 10), text="Nenhuma")
folder_label.place(relx=0.5, rely=0.35, anchor="center")

btn1 = ctk.CTkButton(root, text="Selecionar pasta", command=diretorio, width=250, height=35)
btn1.place(relx=0.5, rely=0.5, anchor="center")

btn2 = ctk.CTkButton(root, text="Organizar pasta", command=organizar, width=250, height=35)
btn2.place(relx=0.5, rely=0.65, anchor="center")

root.mainloop()