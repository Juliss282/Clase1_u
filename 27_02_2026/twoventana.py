import tkinter as tk

def ventana_principal():
    global ven1 #hacemos la variable ven1 global para todo el entorno

#transformar a la ventana una función, aplicar tabulación

    ven1=tk.Tk()
    ven1.title("Ventana principal")
    ven1.geometry("400x300")
    ven1.config(bg="lightblue")

    eti1=tk.Label(ven1, text="Esta es la ventana principal")
    eti1.pack()

    boton2=tk.Button(ven1, text="Ventana 2", command=ventana_2)
    boton2.pack(pady=20)

    boton3=tk.Button(ven1, text="Ventana 3", command=ventana_3)
    boton3.pack(pady=20)

    boton4=tk.Button(ven1, text="Ventana 4", command=ventana_4)
    boton4.pack(pady=20)

    boton5=tk.Button(ven1, text="Ventana 5", command=ventana_5)
    boton5.pack(pady=20)


    ven1.mainloop()


#función para destruir ventanas
def destruir_ventana(ventana_Actual):
    ventana_Actual.destroy()
    ventana_principal()



def ventana_2():

#transformar a la ventana una función, aplicar tabulación

    ven1.destroy()
    #destroy para eliminar la ventana anterior
    ven2=tk.Tk()
    ven2.title("Ventana secundaria")
    ven2.geometry("400x300")
    ven2.config(bg="black")

    eti2=tk.Label(ven2, text="Esta es la ventana 2")
    eti2.pack()

    boton22=tk.Button(ven2, text="Regresar a la ventana principal", command=lambda:destruir_ventana(ven2))
    boton22.pack(pady=20)


    ven2.mainloop()


def ventana_3():

#transformar a la ventana una función, aplicar tabulación

    ven1.destroy()
    #destroy para eliminar la ventana anterior
    ven3=tk.Tk()
    ven3.title("Ventana secundaria")
    ven3.geometry("400x300")
    ven3.config(bg="black")

    eti3=tk.Label(ven3, text="Esta es la ventana 2")
    eti3.pack()

    boton33=tk.Button(ven3, text="Regresar a la ventana principal", command=lambda:destruir_ventana(ven3))
    boton33.pack(pady=20)


    ven3.mainloop()


def ventana_4():

#transformar a la ventana una función, aplicar tabulación

    ven1.destroy()
    #destroy para eliminar la ventana anterior
    ven4=tk.Tk()
    ven4.title("Ventana secundaria")
    ven4.geometry("400x300")
    ven4.config(bg="black")

    eti4=tk.Label(ven4, text="Esta es la ventana 2")
    eti4.pack()

    boton44=tk.Button(ven4, text="Regresar a la ventana principal", command=lambda:destruir_ventana(ven4))
    boton44.pack(pady=20)


    ven4.mainloop()

def ventana_5():

#transformar a la ventana una función, aplicar tabulación

    ven1.destroy()
    #destroy para eliminar la ventana anterior
    ven5=tk.Tk()
    ven5.title("Ventana secundaria")
    ven5.geometry("400x300")
    ven5.config(bg="black")

    eti5=tk.Label(ven5, text="Esta es la ventana 4")
    eti5.pack()

    boton55=tk.Button(ven5, text="Regresar a la ventana principal", command=lambda:destruir_ventana(ven5))
    boton55.pack(pady=20)


    ven5.mainloop()


ventana_principal()