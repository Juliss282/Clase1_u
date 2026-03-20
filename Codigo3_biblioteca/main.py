from Models import *

# 1. PREPARACIÓN DE DATOS (Simulación de base de datos)
sucursal_centro = Sucursal(1, "Centro")
sucursal_norte = Sucursal(2, "Norte")

# Agregamos algunos libros iniciales
libro1 = Libro(101, "Física I", 2023, "Sears", "978-01", "Ciencia")
libro2 = Libro(102, "Python Básico", 2025, "Guido Van", "978-02", "Programación")
sucursal_centro.catalogo_local.append(libro1)
sucursal_norte.catalogo_local.append(libro2)

# Creamos al personal y usuarios
admin = Bibliotecario(1, "John Sebastian", "john@mail.com", "1234")
cliente = Usuario(2, "Maria", "maria@mail.com", "4321")

# El catálogo global que conoce ambas sucursales
biblioteca_global = Catalogo([sucursal_centro, sucursal_norte])

# 2. LÓGICA DEL MENÚ
def ejecutar_menu():
    print("--- BIENVENIDO AL SISTEMA DE BIBLIOTECA ---")
    
    while True:
        print("\nMOVIMIENTOS DISPONIBLES:")
        print("1. Buscar libro por Título")
        print("2. Buscar libros por Autor")
        print("3. Prestar libro (Solo Bibliotecario)")
        print("4. Ver mis préstamos (Usuario)")
        print("5. Salir")
        
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            titulo = input("Introduce el título a buscar: ")
            resultados = biblioteca_global.buscar_en_todas_sucursales(titulo)
            if resultados:
                for lib, suc in resultados:
                    estado = "Disponible" if lib.disponible else "Prestado"
                    print(f"Encontrado: {lib.titulo} en Sucursal {suc} ({estado})")
            else:
                print("No se encontró ese título.")

        elif opcion == "2":
            autor = input("Introduce el autor: ")
            resultados = biblioteca_global.buscar_por_autor(autor)
            if resultados:
                for lib, suc in resultados:
                    print(f"- {lib.titulo} (Autor: {lib.autor}) en Sucursal {suc}")
            else:
                print("No se encontraron libros de ese autor.")

        elif opcion == "3":
            # Simulamos que el bibliotecario hace el proceso
            print(f"Atendiendo bibliotecario: {admin.nombre}")
            # Usaremos el libro1 de la sucursal_centro para el ejemplo
            admin.gestionar_prestamo(libro1, cliente, sucursal_centro)

            #multa = Penalizacion(cliente)
            #monto_total = multa.calcular_multa(prestamo_anterior)

            #if multa.aplicar_bloqueo():
             #   print("No se puede realizar el préstamo. Favor de pasar a caja.")
            #else:
             #   admin.gestionar_prestamo(libro_nuevo, cliente, sucursal_centro)

        elif opcion == "4":
            cliente.listar_prestamos()

        elif opcion == "5":
            print("Saliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    ejecutar_menu()