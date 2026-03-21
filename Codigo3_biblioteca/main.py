from Models import *

#Creación de objetos usuarios
u1=Usuario(101,"Barbara Roberts", "barbie.roberts@gmail.com","pink123")
u2=Usuario(102,"Kenia Carson","ken.carson@hotmail.com","beach99")
u3=Usuario(103,"Allan Sherwood", "allan.s@gmail.com","allan123")
u4=Usuario(104,"Norma Elizondo","norm@gmail.com","password")
u5=Usuario(105,"Midge Hadley","midge.h@gmail.com","midge88")
u6=Usuario(106,"Sasha Jones","sasha.j@gmail.com","sasha_2024")
u7=Usuario(107,"Gloria Estefan","gloria.e@gmail.com", "gloria1")
u8=Usuario(108,"Juan Reyes","ren2@gmail.com","juren")
u9=Usuario(109,"Ruth Handler", "ruth.h@gmail.com", "creator1")
u10=Usuario(110,"Sara Elizondo","saritaelz@gmail.com", "sarlita123")

usuarios = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10]
for u in usuarios:
    (u.mostrarDetalle())

print(u1.login(101, "1234"))        
print(u1.login(101, "pink123"))  

u1.listar_prestamos()


#creación de libros
libro1 = Libro(1, "Todo sobre el amor", 1999, "bell hooks", "978-8412143164", "Ensayo")
libro2 = Libro(2, "1984", 1949, "George Orwell", "978-0451524935", "Distopía")
libro3 = Libro(3, "El Principito", 1943, "Antoine de Saint-Exupéry", "978-0156012195", "Infantil")
libro4 = Libro(4, "Don Quijote de la Mancha", 1605, "Miguel de Cervantes", "978-8424116012", "Novela")
libro5 = Libro(5, "Rayuela", 1963, "Julio Cortázar", "978-8466331906", "Surrealismo")
libro6 = Libro(6, "Rebelión en la granja", 1945, "George Orwell", "978-8420633114", "Alegoría")
libro7 = Libro(7, "Pedro Páramo", 1955, "Juan Rulfo", "978-8437601656", "Realismo Mágico")
libro8 = Libro(8, "La tregua", 1960, "Mario Benedetti", "978-8420658827", "Novela")
libro9 = Libro(9, "Frankenstein o el moderno Prometeo", 1818, "Mary Shelley", "978-1400034956", "Novela")
libro10 = Libro(10, "Fahrenheit 451", 1953, "Ray Bradbury", "978-1451673319", "Ciencia Ficción")


#creación de material digitas
digital1 = MaterialDigital(101, "Guía Python v3", 2023, "Guido Van Rossum", "PDF", "http://biblio.com/dl/p3", 15.5)
digital2 = MaterialDigital(102, "AI for Everyone", 2022, "Andrew Ng", "EPUB", "http://biblio.com/dl/ai", 8.2)
digital3 = MaterialDigital(103, "Clean Code", 2008, "Robert C. Martin", "PDF", "http://biblio.com/dl/cc", 12.0)
digital4 = MaterialDigital(104, "Design Patterns", 1994, "Gang of Four", "PDF", "http://biblio.com/dl/dp", 20.1)
digital5 = MaterialDigital(105, "Refactoring", 1999, "Martin Fowler", "MOBI", "http://biblio.com/dl/rf", 10.4)
digital6 = MaterialDigital(106, "Test Driven Development", 2002, "Kent Beck", "PDF", "http://biblio.com/dl/tdd", 5.7)
digital7 = MaterialDigital(107, "Soft Skills", 2014, "John Sonmez", "EPUB", "http://biblio.com/dl/ss", 7.3)
digital8 = MaterialDigital(108, "The Pragmatic Programmer", 1999, "Andy Hunt", "PDF", "http://biblio.com/dl/pp", 11.2)
digital9 = MaterialDigital(109, "Introduction to Algorithms", 2009, "Cormen et al.", "PDF", "http://biblio.com/dl/algo", 45.8)
digital10 = MaterialDigital(110, "Domain Driven Design", 2003, "Eric Evans", "PDF", "http://biblio.com/dl/ddd", 18.9)



#creación de revistas
revista1 = Revista(201, "National Geographic", 2024, "NG Staff", "Ed. 505", "Mensual")
revista2 = Revista(202, "Time Magazine", 2024, "Time USA", "Vol. 203", "Semanal")
revista3 = Revista(203, "Scientific American", 2023, "Springer Nature", "Ed. 12", "Mensual")
revista4 = Revista(204, "Forbes", 2024, "Forbes Media", "Ed. Millonarios", "Mensual")
revista5 = Revista(205, "Vogue", 2024, "Condé Nast", "Primavera", "Mensual")
revista6 = Revista(206, "The Economist", 2024, "Economist Group", "No. 9380", "Semanal")
revista7 = Revista(207, "Wired", 2023, "Condé Nast", "Tech Review", "Bimensual")
revista8 = Revista(208, "Nature", 2024, "Nature Portfolio", "Vol. 625", "Semanal")
revista9 = Revista(209, "Muy Interesante", 2024, "Zinet Media", "No. 490", "Mensual")
revista10 = Revista(210, "Rolling Stone", 2024, "Penske Media", "Especial Rock", "Mensual")

#cración de sucursales
suc1 = Sucursal(1, "Biblioteca del Monasterio de Strahov")
suc2 = Sucursal(2, "Antigua Biblioteca del Trinity College")
suc3 = Sucursal(3, "Biblioteca Vasconcelos")
suc4 = Sucursal(4, "Real Gabinete Portugués de Lectura")
suc5 = Sucursal(5, "Biblioteca Hachioji")
suc6 = Sucursal(6, "Biblioteca George Peabody")
suc7 = Sucursal(7, "Biblioteca del monasterio de Wiblingen")
suc8 = Sucursal(8, "Biblioteca Raza")
suc9 = Sucursal(9, "Biblioteca del Monasterio de St. Gallen")
suc10 = Sucursal(10, "Biblioteca del monasterio de Admont")


# Distribuir materiales en sucursales
suc1.catalogo_local.extend([libro1, libro2, revista1])
suc2.catalogo_local.extend([libro3, libro4, revista2])
suc3.catalogo_local.extend([libro5, libro6, revista3])
suc4.catalogo_local.extend([libro7, libro8, revista4])
suc5.catalogo_local.extend([libro9, libro10, revista5])
suc1.catalogo_local.append(digital1)
suc2.catalogo_local.append(digital2)

#creación de catálogo
cat_general = Catalogo([suc1, suc2, suc3, suc4, suc5, suc6, suc7, suc8, suc9, suc10])

#creación de bibliotecarios
b1=Bibliotecario(501,"Olive Smith", "osmith@univ.edu", "olive1")
b2=Bibliotecario(502,"Adam Carlsen", "acarlsen@univ.edu", "adam2")
b3=Bibliotecario(503,"Anh Pham", "apham@univ.edu", "anh3")
b4=Bibliotecario(504,"Malcolm Jenkins", "mjenkins@univ.edu", "malcolm4")
b5=Bibliotecario(505,"Tom Benton", "tbenton@univ.edu", "tom5")
b6=Bibliotecario(506,"Holden Rodriguez", "hrodriguez@univ.edu", "holden6")
b7=Bibliotecario(507,"Becca Miller", "bmiller@univ.edu", "becca7")
b8=Bibliotecario(508,"Jeremy Jones", "jjones@univ.edu", "jeremy8")
b9=Bibliotecario(509,"Rodriguez", "rrodriguez@univ.edu", "dr9")
b10=Bibliotecario(510,"Aslan", "aslan@univ.edu", "aslan10")

bibliotecarios = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]
for b in bibliotecarios:
    (b.mostrarDetalle())

b9.transferir_material(libro7, suc1, suc2)
b9.transferir_material(libro7, suc4, suc9)

# Menú principal
def ejecutar_menu():
    print("--- BIENVENIDO AL SISTEMA DE BIBLIOTECA ---")
    
    while True:
        print("\nMOVIMIENTOS DISPONIBLES:")
        print("1. Iniciar sesión como usuario")
        print("2. Iniciar sesión como bibliotecario")
        print("3. Salir")
        
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            id_buscado = int(input("Ingrese su ID de Usuario: "))
            password = input("Ingrese su contraseña: ")
            usuario_logueado = next((u for u in usuarios if u.login(id_buscado, password)), None)
            if usuario_logueado:
                menu_usuario(usuario_logueado)
            else:
                print("Credenciales incorrectas.")
        
        elif opcion == "2":
            id_buscado = int(input("Ingrese su ID de Bibliotecario: "))
            password = input("Ingrese su contraseña: ")

            biblio_logueado = next((b for b in bibliotecarios if b.login(id_buscado, password)), None)
            if biblio_logueado:
                menu_bibliotecario(biblio_logueado)
            else:
                print("Credenciales incorrectas.")

        elif opcion == "3":
            print("«Un lector vive mil vidas antes de morir. Aquel que nunca lee vive solo una». — George R. R. Martin.")
            break


     

def menu_usuario(usuario):
    while True:
        print(f"\n--- BIENVENIDO {usuario.nombre.upper()} ---")
        print("1. Ver Lista de prestamos activos")
        print("2. Consultar disponibilidad de material")
        print("3. Devolver libro")
        print("4. Cerrar Sesión")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--------- Prestamos activos ---------")
            usuario.listar_prestamos()

        elif opcion == "2":
            print("\n_____ Consulta de material disponible_____")
            print("Elegir una forma de búsqueda")
            print("1. Buscar por autor")
            print("2. Buscar en todas las scursales (por título)")

            option = input("Seleccione una opción:  ")
            if option == "1":

                autor = input("Autor: ")
                resultados = cat_general.buscar_por_autor(autor)
                if resultados:
                    for libro, sucursal in resultados:
                        estado = "Disponible" if libro.disponible else "No disponible"
                        print(f"{libro.titulo} - {sucursal} ({estado})")
                else:
                    print("No se encontraron resultados")

            elif option== "2":
                titulo = input("Título: ")
                resultados = cat_general.buscar_en_todas_sucursales(titulo)
                if resultados:
                    for libro, sucursal in resultados:
                        estado = "Disponible" if libro.disponible else "No disponible"
                        print(f"{libro.titulo} - {sucursal} ({estado})")
                else:
                    print("No se encontraron resultados")

        elif opcion == "3":
            if not usuario.prestamos:
                print("No tienes préstamos activos")
                continue

            print("\n--- préstamos ---")
            for i, p in enumerate(usuario.prestamos):
                estado = "Activo" if p.activo else "Devuelto"
                print(f"{i+1}. {p.material.titulo} ({estado})")
            i = int(input("Selecciona el préstamo a devolver: ")) - 1
            if i < 0 or i >= len(usuario.prestamos):
                print("Opción inválida")
                continue
            prestamo = usuario.prestamos[i]
            if not prestamo.activo:
                print("Ese libro ya fue devuelto")
                continue
            # Buscar sucursal porque la clase lo necesita
            sucursal = None
            for s in cat_general.sucursales:
                if prestamo.material not in s.catalogo_local:
                    sucursal = s
                    break

            if sucursal:
                usuario.devolver_libro(prestamo, sucursal)
                penalizacion = Penalizacion(usuario)
                multa = penalizacion.calcular_multa(prestamo)
                if multa > 0:
                    print(f"Tienes una multa de ${multa}")
                    penalizacion.bloquear_usuario()
                else:
                    print("Devolución sin penalización")
            else:
                print("Error al localizar sucursal")
        elif opcion=="4":
            usuario.logout()
            break


def menu_bibliotecario(bibliotecario):
    while True:
        print(f"\n--- BIBLIOTECARIO {bibliotecario.nombre.upper()} ---")
        print("1. Realizar préstamo")
        print("2. Transferir material")
        print("3. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_usuario = int(input("ID usuario: "))
            usuario = next((u for u in usuarios if u.idPersona == id_usuario), None)
            if not usuario:
                print("Usuario no encontrado")
                continue

            titulo = input("Título del libro: ")
            resultados = cat_general.buscar_en_todas_sucursales(titulo)
            if resultados:
                libro, nombre_sucursal = resultados[0]
                sucursal = next(s for s in cat_general.sucursales if s.nombre == nombre_sucursal)
                bibliotecario.gestionar_prestamo(libro, usuario, sucursal)
            else:
                print("Libro no encontrado")

        elif opcion == "2":
            titulo = input("Título del libro: ")
            resultados = cat_general.buscar_en_todas_sucursales(titulo)
            if resultados:
                libro, nombre_sucursal = resultados[0]
                sucursal_origen = next(s for s in cat_general.sucursales if s.nombre == nombre_sucursal)
                id_destino = int(input("ID sucursal destino: "))
                sucursal_destino = next((s for s in cat_general.sucursales if s.id_sucursal == id_destino), None)

                if sucursal_destino:
                    bibliotecario.transferir_material(libro, sucursal_origen, sucursal_destino)
                else:
                    print("Sucursal destino inválida")

        elif opcion == "3":
            bibliotecario.logout()
            break


ejecutar_menu()