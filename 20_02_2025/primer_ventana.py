import tkinter as tk
ven1=tk.Tk()
ven1.title("Ejemplo")
ven1.geometry("1600x500")

etiqueta = tk.Label(ven1,text="¡hola facultad de ciencias de la compu!",
    font=("Arial", 14, "bold"), fg="black", bg="yellow",padx=20, pady=10)
etiqueta.pack()


#etiqueta.place(x=50, y=200)   ubica en un lugar especifico
#.pack lo centra

etiqueta2 = tk.Label(ven1,text="Mi nombre es Julissa",
    font=("Helvetica", 14, "bold"), fg="black", bg="yellow",padx=20, pady=10)
etiqueta2.pack()

etiqueta3 = tk.Label(ven1,text="Estudio ingeniería en ciencias de la computación",
    font=("Georgia", 14, "bold"), fg="black", bg="yellow",padx=20, pady=10)
etiqueta3.pack()

etiqueta4 = tk.Label(ven1,text="Mi comida favorita es el mole dulce",
    font=("Times New Roman", 14, "bold"), fg="black", bg="yellow",padx=20, pady=10)
etiqueta4.pack()




ven1.mainloop()
#nombrecarreracomida