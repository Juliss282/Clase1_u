import tkinter as tk
from tkinter import messagebox

def opcion():
    if var.get() == 1:
        messagebox.showinfo("Opcion elegida", "Tienes buen gusto ¡Te gustan los tacos!")
    elif var.get() == 2:
        messagebox.showinfo("Opcion elegida", "Tienes buen gusto ¡Te gustan las chanclas!")
    elif var.get() == 3:
        messagebox.showinfo("Opcion elegida", "Tienes buen gusto ¡Te gusta la milanesa!")
    elif var.get() == 4:
        messagebox.showinfo("Opcion elegida", "Tienes buen gusto ¡Te gusta la pizza")
    elif var.get() == 5:
        messagebox.showinfo("Opcion elegida", "Tienes excelente gusto ¡Te gusta el esquite!")
    else:
        messagebox.showinfo("Opcion elegida", "No seleccionaste nada")


vtn1=tk.Tk()
vtn1.title("Uso del Radio Botton")
vtn1.geometry("500x500")

etiqueta1=tk.Label(vtn1, text=("¿Cuál es tu comida favorita?"))
etiqueta1.pack(pady=20)

var=tk.IntVar() #creamos variables para guardar la opción
rad1=tk.Radiobutton(vtn1,text="Tacos",variable=var,value=1)
rad1.pack()
rad2=tk.Radiobutton(vtn1,text="Chanclas",variable=var,value=2)
rad2.pack()
rad3=tk.Radiobutton(vtn1,text="Milanesa",variable=var,value=3)
rad3.pack()
rad4=tk.Radiobutton(vtn1,text="Pizza",variable=var,value=4)
rad4.pack()
rad5=tk.Radiobutton(vtn1,text="Esquite",variable=var,value=5)
rad5.pack()

boton1=tk.Button(vtn1, text="Verificar",command=opcion) 
#command, o sea ocuparemos una funcion
boton1.pack(pady=30)

vtn1.mainloop()