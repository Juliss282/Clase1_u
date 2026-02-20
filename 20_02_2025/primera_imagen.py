import tkinter as tk
from PIL import Image, ImageTk

def boton_clic():
    print("Hiciste click!")

def actualizar_etiqueta():
    nuevo_texto = entrada.get()
    etiqueta.config(text=nuevo_texto)


#imagen

root = tk.Tk()
root.title("Imagen en Tkinter")
#Cargar la imagen
imagen = Image.open("universe.jpg")
imagen=imagen.resize((400, 200)) #Redimensionar si es necesario
imagen_tk=ImageTk.PhotoImage(imagen)
label_imagen=tk.Label(root, image=imagen_tk)
label_imagen.pack(pady=20)

#boton1

boton = tk.Button(root, text="HAZ CLIC AQUÍ", command=boton_clic,
                  font=("Comic Sans",30))
boton.pack(pady=20)


#boton generador

entrada = tk.Entry(root,width=60)
entrada.pack(pady=10)

boton2 = tk.Button(root, text="Actualizar", command = actualizar_etiqueta)
boton2.pack()

etiqueta = tk.Label(root, text = "Texto inicial", font=("Arial", 12))
etiqueta.pack(pady=10)

root.mainloop()

#para resolver, cambiar la direccion
#ecribir en terminal cd "dentro de esta comillas la direccion de la imagen"