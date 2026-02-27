#Crear una ventana donde aparezca el nombre de los animales en botones
#al hacer clic en cada boton, que aparezca el nombre del animal, su descripción y una imagen
#radio botton

import tkinter as tk
from tkinter import messagebox

def ventana_principal():
    global menuu_1


    menuu_1=tk.Tk()
    menuu_1.title("Menú principal")
    menuu_1.geometry("800x600")
    menuu_1.config(bg="lightblue")

    et1=tk.Label(menuu_1, text="Animales")
    et1.grid(row=2, column=0, padx=5, pady=5)

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

    
    rad1=tk.Radiobutton(menuu_1, text="Elefante", variable=var,value=1)
    rad1.grid(row=5, column=0, padx=5, pady=5)
    rad2=tk.Radiobutton(menuu_1,text="Castor", variable=var,value=2)
    rad2.grid(row=7, column=0, padx=5, pady=5)
    rad3=tk.Radiobutton(menuu_1,text="Dodo", variable=var,value=3)
    rad3.grid(row=9, column=0, padx=5, pady=5)
    rad4=tk.Radiobutton(menuu_1,text="Jirafa", variable=var,value=4)
    rad4.grid(row=10, column=0, padx=5, pady=5)
    rad5=tk.Radiobutton(menuu_1,text="León", variable=var,value=5)
    rad5.grid(row=13, column=0, padx=5, pady=5)

    boton1=tk.Button(menuu_1, text="Saber más", command=opcion)
    boton1.grid(row=15, column=0, padx=5, pady=5)


    menuu_1.mainloop()


#función para destruir ventanas
def destruir_ventana(ventana_Actual):
    ventana_Actual.destroy()
    ventana_principal()



def ventana_2():


    menuu_1.destroy()
    
    ven2=tk.Tk()
    ven2.title("Elefante")
    ven2.geometry("400x300")
    ven2.config(bg="black")

    eti2=tk.Label(ven2, text="Elefante")
    eti2.grid(row=2, column=0, padx=5, pady=5)

    boton22=tk.Button(ven2, text="Regresar a la ventana principal", command=lambda:destruir_ventana(ven2))
    boton22.grid(row=4, column=0, padx=5, pady=5)


    ven2.mainloop()


def ventana_3():

#transformar a la ventana una función, aplicar tabulación

    menuu_1.destroy()
    #destroy para eliminar la ventana anterior
    ven3=tk.Tk()
    ven3.title("Castor")
    ven3.geometry("400x300")
    ven3.config(bg="black")

    eti3=tk.Label(ven3, text="Castor")
    eti3.grid(row=2, column=0, padx=5, pady=5)

    boton33=tk.Button(ven3, text="Regresar a la ventana principal", command=lambda:destruir_ventana(ven3))
    boton33.grid(row=4, column=0, padx=5, pady=5)


    ven3.mainloop()


def ventana_4():

#transformar a la ventana una función, aplicar tabulación

    menuu_1.destroy()
    #destroy para eliminar la ventana anterior
    ven4=tk.Tk()
    ven4.title("Dodo")
    ven4.geometry("400x300")
    ven4.config(bg="black")

    eti4=tk.Label(ven4, text="Dodo")
    eti4.grid(row=2, column=0, padx=5, pady=5)

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

    eti5=tk.Label(ven5, text="Jirafa")
    eti5.grid(row=2, column=0, padx=5, pady=5)

    boton55=tk.Button(ven5, text="Regresar a la ventana principal", command=lambda:destruir_ventana(ven5))
    boton55.grid(row=4, column=0, padx=5, pady=5)


    ven5.mainloop()

def ventana_6():

#transformar a la ventana una función, aplicar tabulación

    menuu_1.destroy()
    #destroy para eliminar la ventana anterior
    ven6=tk.Tk()
    ven6.title("León")
    ven6.geometry("400x300")
    ven6.config(bg="black")

    eti5=tk.Label(ven6, text="Esta es la ventana 6")
    eti5.grid(row=2, column=0, padx=5, pady=5)

    boton55=tk.Button(ven6, text="León", command=lambda:destruir_ventana(ven6))
    boton55.grid(row=4, column=0, padx=5, pady=5)


    ven6.mainloop()


ventana_principal()