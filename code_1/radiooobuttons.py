import tkinter as tk
from tkinter import messagebox

def opcion():
    if var.get() == 1:
        messagebox.showinfo("Ventana de muestro información", "Easy showinfo")
    elif var.get() == 2:
        messagebox.showwarning("Ventana de advertencia", "Ojito, showwarning")
    elif var.get() == 3:
        messagebox.showerror("Ventana de error", "Ya valió, showerror")
    elif var.get() == 4:
        respuesta=messagebox.askyesno("Ventana de sí o no", "¿Te gusta esta clase?")
        if respuesta:
            messagebox.showinfo("Ventana de respuesta", "Más te vale")
        else:
            messagebox.showinfo("Ventana de respuesta", "Por eso vas a reprobar")
    elif var.get() == 5:
        respuesta=messagebox.askokcancel("Ventana de opcion (aceptar o denegar)", "¿Das tu alma a esta clase?")
        if respuesta:
            messagebox.showinfo("Ventana de opcion aceptar", "Nice")
        else:
            messagebox.showinfo("Ventana de opcion negar", "Bad")
            
        
    

vna1=tk.Tk()
vna1.title("Tipos de messagebox")
vna1.geometry("800x800")
vna1.config(bg="Lightblue")

var=tk.IntVar()
rad1=tk.Radiobutton(vna1,text="Estoy mostrando información",variable=var,value=1)
rad1.pack()

rad2=tk.Radiobutton(vna1, text="Esto es una advertencia", variable=var, value=2)
rad2.pack()

rad3=tk.Radiobutton(vna1, text="Esto es un error", variable=var, value=3)
rad3.pack()

rad4=tk.Radiobutton(vna1, text="Preguntar sí o no", variable=var, value=4)
rad4.pack()

rad5=tk.Radiobutton(vna1, text="Preguntar acepta o no acepta", variable=var, value=5)
rad5.pack()

boton1=tk.Button(vna1, text="Sacar ventana",command=opcion) 
boton1.pack(pady=30)

vna1.mainloop()