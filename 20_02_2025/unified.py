import tkinter as tk


root=tk.Tk()
root.title("Imagen en Tkinter")
root.geometry("1600x500")

etiqueta = tk.Label(root,text="¡hola facultad de ciencias de la compu!",
    font=("Arial", 14, "bold"), fg="black", bg="yellow",padx=20, pady=10)
etiqueta.pack()


#etiqueta.place(x=50, y=200)   ubica en un lugar especifico
#.pack lo centra

etiqueta2 = tk.Label(root,text="Mi nombre es Julissa",
    font=("Helvetica", 14, "bold"), fg="black", bg="yellow",padx=20, pady=10)
etiqueta2.pack()

etiqueta3 = tk.Label(root,text="Estudio ingeniería en ciencias de la computación",
    font=("Georgia", 14, "bold"), fg="black", bg="yellow",padx=20, pady=10)
etiqueta3.pack()

etiqueta4 = tk.Label(root,text="Mi comida favorita es el mole dulce",
    font=("Times New Roman", 14, "bold"), fg="black", bg="yellow",padx=20, pady=10)
etiqueta4.pack()

imagen = Image.open("universe.jpg")
imagen=imagen.resize((400, 200)) #Redimensionar si es necesario
imagen_tk=ImageTk.PhotoImage(imagen)
label_imagen=tk.Label(root, image=imagen_tk)
label_imagen.pack(pady=20)

boton = tk.Button(root, text="HAZ CLIC AQUÍ", command=boton_clic,
                  font=("Comic Sans",30))
boton.pack(pady=20)

root.mainloop()





ven1.mainloop()