import tkinter as tk
from tkinter import messagebox

def nuevo_archivo():
    messagebox.showinfo("información", "creaste un nuevo archivo")

def abrir_archivo():
    messagebox.showinfo("información", "abriste un archivo")

def guardar_archivo():
    messagebox.showinfo("información", "guardaste un archivo")

def cortar_a():
    messagebox.showinfo("información", "cortaste un texto")

def pegar_a():
    messagebox.showinfo("información", "pegaste un texto")

ven1=tk.Tk()
ven1.title("Uso de menus")
ven1.geometry("500x400")

barra_menu=tk.Menu(ven1)

menu_archivo = tk.Menu(barra_menu,tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", command=guardar_archivo)

menu_edicion=tk.Menu(barra_menu,tearoff=0)
menu_edicion.add_command(label="Cortar", command=cortar_a)
menu_edicion.add_command(label="Pegar", command=pegar_a)

barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_menu.add_cascade(label="Edición", menu=menu_edicion)
ven1.config(menu=barra_menu)

ven1.mainloop()