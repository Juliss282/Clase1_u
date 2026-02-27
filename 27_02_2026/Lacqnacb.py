import tkinter as tk

#Crear ventana
root = tk.Tk()
root.title("Ejemplo de Grid")
root.geometry("500X200")
root.config(bg="blue")

#Crear etiquetas y cambios de entrada con grid
etiqueta1=tk.Label(root, text="Nombre:", bg="blue", fg='white', font=('Arial',16,'bold'))
etiqueta1.grid(row=0, colum=0, padx=5, pady=5, sticky="w")
entrada1=tk.Entry(root, width=60)
entrada1.grid(row=1, colum=1, padx=5, pady=5, sticky="w")


root.mainloop()