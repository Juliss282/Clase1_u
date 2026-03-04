#Crear una ventana donde aparezca el nombre de los animales en botones
#al hacer clic en cada boton, que aparezca el nombre del animal, su descripción y una imagen
#radio botton

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def ventana_principal():
    global menuu_1

    menuu_1=tk.Tk()
    menuu_1.title("Menú principal")
    menuu_1.geometry("800x600")
    menuu_1.config(bg="lightblue")

    et1=tk.Label(menuu_1, text="Animales", bg="gray", font=("Algerian",24,"bold"))
    et1.pack(pady=10)

    frame1=tk.Frame(menuu_1)
    frame1.pack(fill=tk.X, padx=10,pady=10)
    imagen1 = Image.open("C:/Users/LAB202/Documents/Progamacion_advanced/04_03_2026/Continuacion_ventanasanimales/animals_inicio.jpg")
    imagen1 = imagen1.resize((400,200))
    imagen_tk1 = ImageTk.PhotoImage(imagen1)
    label_imagen = tk.Label (frame1, image=imagen_tk1)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)
    frame2=tk.Frame(frame1)
    frame2.grid(row=0, column=1, padx=5, pady=5)
    

    var=tk.IntVar()

    def opcion():
        if var.get() == 1:
            ventana_2()
        elif var.get() == 2:
            ventana_3()
        elif var.get() == 3:
            ventana_4()
        elif var.get() == 4:
            ventana_5()
        elif var.get() == 5:
            ventana_6()
        else:
            messagebox.showinfo("Opcion elegida", "No seleccionaste nada")

    
    rad1=tk.Radiobutton(frame2, text="Elefante", variable=var,value=1)
    rad1.pack()
    rad2=tk.Radiobutton(frame2,text="Castor", variable=var,value=2)
    rad2.pack()
    rad3=tk.Radiobutton(frame2,text="Dodo", variable=var,value=3)
    rad3.pack()
    rad4=tk.Radiobutton(frame2,text="Jirafa", variable=var,value=4)
    rad4.pack()
    rad5=tk.Radiobutton(frame2,text="León", variable=var,value=5)
    rad5.pack()

    boton1=tk.Button(frame2, text="Saber más", command=opcion)
    boton1.pack()

    menuu_1.mainloop()


#función para destruir ventanas
def destruir_ventana(ventana_Actual):
    ventana_Actual.destroy()
    ventana_principal()



def ventana_2():

    global ven2
    menuu_1.destroy()
    
    ven2=tk.Tk()
    ven2.title("Elefante")
    ven2.geometry("700x500")
    ven2.config(bg="black")

    eti2=tk.Label(ven2, text="Elefante", bg="gray", font=("Algerian",24,"bold"))
    eti2.pack(pady=10)

    frame3=tk.Frame()
    frame3.pack(pady=20)
    imagen2 = Image.open("C:/Users/LAB202/Documents/Progamacion_advanced/04_03_2026/Continuacion_ventanasanimales/elefants.jpg")
    imagen2 = imagen2.resize((400,200))
    imagen_tk2 = ImageTk.PhotoImage(imagen2)
    label_imagen = tk.Label (frame3, image=imagen_tk2)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)
    infoelefante = tk.Label(frame3, text="son los mamíferos terrestres más grandes, conocidos por su trompa prensil," \
    " grandes orejas (que ayudan a regular la temperatura)" \
    ", colmillos (en la mayoría de los casos), y piel gruesa y arrugada, " \
    "viven en estructuras sociales matriarcales, son herbívoros" \
    " inteligentes y comunican emociones con sonidos como el barrito," \
    " además de tener la gestación más larga entre los mamíferos", wraplength=200, justify="left")
    infoelefante.grid(row=0, column=1, padx=5, pady=5)

    boton22=tk.Button(ven2, text="Regresar a la ventana principal", command=lambda:destruir_ventana(ven2))
    boton22.pack(pady=20)


    ven2.mainloop()


def ventana_3():

#transformar a la ventana una función, aplicar tabulación

    menuu_1.destroy()
    #destroy para eliminar la ventana anterior
    ven3=tk.Tk()
    ven3.title("Castor")
    ven3.geometry("400x300")
    ven3.config(bg="black")

    eti3=tk.Label(ven3, text="Castor", bg="gray", font=("Algerian",24,"bold"))
    eti3.pack(pady=20)

    frame4=tk.Frame()
    frame4.pack(pady=20)
    imagen3 = Image.open("C:/Users/LAB202/Documents/Progamacion_advanced/04_03_2026/Continuacion_ventanasanimales/elefants.jpg")
    imagen3 = imagen3.resize((400,200))
    imagen_tk3 = ImageTk.PhotoImage(imagen3)
    label_imagen = tk.Label (frame4, image=imagen_tk3)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)
    infoelefante = tk.Label(frame4, text="El castor es el roedor mas grande de Norteamérica. " \
    "Su alimentación es estrictamente herbívora y se basa principalmente" \
    " en la corteza interior de los árboles, brotes, yemas y vegetación acuática.", wraplength=200, justify="left")
    infoelefante.grid(row=0, column=1, padx=5, pady=5)

    boton33=tk.Button(ven3, text="Regresar a la ventana principal", command=lambda:destruir_ventana(ven3))
    boton33.pack(pady=20)


    ven3.mainloop()


def ventana_4():

#transformar a la ventana una función, aplicar tabulación

    menuu_1.destroy()
    #destroy para eliminar la ventana anterior
    ven4=tk.Tk()
    ven4.title("Dodo")
    ven4.geometry("400x300")
    ven4.config(bg="black")

    eti4=tk.Label(ven4, text="Dodo", bg="gray", font=("Algerian",24,"bold"))
    eti4.pack(pady=20)

    frame5=tk.Frame()
    frame5.pack(pady=20)
    imagen4 = Image.open("C:/Users/LAB202/Documents/Progamacion_advanced/04_03_2026/Continuacion_ventanasanimales/elefants.jpg")
    imagen4 = imagen4.resize((400,200))
    imagen_tk4 = ImageTk.PhotoImage(imagen4)
    label_imagen = tk.Label (frame5, image=imagen_tk4)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)
    infoelefante = tk.Label(frame5, text="El castor es el roedor mas grande de Norteamérica. " \
    "Su alimentación es estrictamente herbívora y se basa principalmente" \
    " en la corteza interior de los árboles, brotes, yemas y vegetación acuática.", wraplength=200, justify="left")
    infoelefante.grid(row=0, column=1, padx=5, pady=5)

    boton44=tk.Button(ven4, text="Regresar a la ventana principal", command=lambda:destruir_ventana(ven4))
    boton44.grid(row=4, column=0, padx=5, pady=5)

    ven4.mainloop()

def ventana_5():

#transformar a la ventana una función, aplicar tabulación

    menuu_1.destroy()
    #destroy para eliminar la ventana anterior
    ven5=tk.Tk()
    ven5.title("Jirafa")
    ven5.geometry("400x300")
    ven5.config(bg="black")

    eti5=tk.Label(ven5, text="Jirafa", bg="gray", font=("Algerian",24,"bold"))
    eti5.pack(pady=20)

    frame6=tk.Frame()
    frame6.pack(pady=20)
    imagen5 = Image.open("C:/Users/LAB202/Documents/Progamacion_advanced/04_03_2026/Continuacion_ventanasanimales/elefants.jpg")
    imagen5 = imagen5.resize((400,200))
    imagen_tk5 = ImageTk.PhotoImage(imagen5)
    label_imagen = tk.Label (frame6, image=imagen_tk5)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)
    infoelefante = tk.Label(frame6, text="El castor es el roedor mas grande de Norteamérica. " \
    "Su alimentación es estrictamente herbívora y se basa principalmente" \
    " en la corteza interior de los árboles, brotes, yemas y vegetación acuática.", wraplength=200, justify="left")
    infoelefante.grid(row=0, column=1, padx=5, pady=5)

    boton55=tk.Button(ven5, text="Regresar a la ventana principal", command=lambda:destruir_ventana(ven5))
    boton55.pack(pady=20)


    ven5.mainloop()

def ventana_6():

#transformar a la ventana una función, aplicar tabulación

    menuu_1.destroy()
    #destroy para eliminar la ventana anterior
    ven6=tk.Tk()
    ven6.title("León")
    ven6.geometry("400x300")
    ven6.config(bg="black")

    eti6=tk.Label(ven6, text="Esta es la ventana 6", bg="gray", font=("Algerian",24,"bold"))
    eti6.pack(pady=20)

    frame7=tk.Frame()
    frame7.pack(pady=20)
    imagen6 = Image.open("C:/Users/LAB202/Documents/Progamacion_advanced/04_03_2026/Continuacion_ventanasanimales/elefants.jpg")
    imagen6 = imagen6.resize((400,200))
    imagen_tk6 = ImageTk.PhotoImage(imagen6)
    label_imagen = tk.Label (frame7, image=imagen_tk6)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)
    infoelefante = tk.Label(frame7, text="El castor es el roedor mas grande de Norteamérica. " \
    "Su alimentación es estrictamente herbívora y se basa principalmente" \
    " en la corteza interior de los árboles, brotes, yemas y vegetación acuática.", wraplength=200, justify="left")
    infoelefante.grid(row=0, column=1, padx=5, pady=5)
    

    boton66=tk.Button(ven6, text="León", command=lambda:destruir_ventana(ven6))
    boton66.pack(pady=20)


    ven6.mainloop()


ventana_principal()