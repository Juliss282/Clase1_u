import tkinter as tk
from tkinter import messagebox
#message me crea una ventana emergente y manda una noti

def estatus():
    if var.get() == 1: #.get me regresa el valor que tiene
        messagebox.showinfo("Estado sii", "Checkbutton seleccionado")
    else: #don't forget last:
        messagebox.showinfo("Estado oh noo", "Checkbutton no esta seleccionado")

#recuerda iniciar la ventana con --=tk.Tk()
ven1=tk.Tk()
ven1.title("Uso del checkbotton")
ven1.geometry("400x500")

etiqueta1=tk.Label(ven1,text="Aquí va un checkbutton")
#pady pa'l default style
etiqueta1.pack(pady=20)

#este es para crear un ckeck, si o no en cuadrito
var=tk.IntVar() 
#variable donde queda el 0 o 1 del button
#crear checkbutton, el ven1, de donde quiero que aparezca
bcheck=tk.Checkbutton(ven1, text="Elegir opción", variable=var)
#falta el pack para que aparezca
bcheck.pack(pady=19)

#este es para que la frase este dentro del boton
#no escribir estatus=tk.IntVar porque por algo esta la funcion del inicio, en este caso con
#funcion command
boton1=tk.Button(ven1, text="Verificar Estatus", command=estatus)
#para un boton que no haga nada, quitar command
boton1.pack()

#note: este siempre va al final de todo y es para que aparezca es necesario ---.mainloop()
ven1.mainloop()