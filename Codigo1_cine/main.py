from Models import *

print("----------Usuarios creados----------")
#creación de usuarios
u1 = Usuario(1011, "Olive Smith", "olive.smith@stanford.edu", "555011", "pumpkin-latte", 250)
u2 = Usuario(1012, "Adam Carlsen", "acarlsen@stanford.edu", "555012", "sunscreen-hater", 100)
u3 = Usuario(1013, "Anh Pham", "anh.pham@mail.com", "555013", "romcom-queen", 220)
u4 = Usuario(1014, "Malcolm Weiss", "m_weiss@mail.com", "555014", "biology-rules", 120)
u5 = Usuario(1015, "Tom Benton", "t.benton@harvard.edu", "555015", "valley-99", 10)
u6 = Usuario(2016, "Elizabeth Bennet", "lizzy.b@longbourn.com", "555016", "pemberley-vibes", 350)
u7 = Usuario(2017, "Fitzwilliam Darcy", "darcy@pemberley.com", "555017", "pride-prejudice", 400)
u8 = Usuario(2018, "Jo March", "jo_writer@orchard.com", "555018", "little-women", 20)
u9 = Usuario(2019, "Jay Gatsby", "great.gatsby@west-egg.com", "555019", "green-light", 100)
u10 = Usuario(2020, "Emma Woodhouse", "emma.w@highbury.com", "555020", "matchmaker", 280)

usuarios = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10]
for u in usuarios:
    print(f"ID: {u.idPersona} | Nombre: {u.nombre} | Correo: {u.email} | Puntos: {u.puntosFidelidad}")


print("----------Empleados creados----------")
#creación de empleados
#administradores
e1 = empleado(301, "Clara Bell", "c.bell@cine.com", "555901", "tinker-123", 11, Rol.ADMIN, "Mañana")
e2 = empleado(302, "Reina Clarion", "r.clarion@cine.com", "555902", "golden-pixie", 12, Rol.ADMIN, "Tarde")
e3 = empleado(303, "Milo Fairyary", "m.terence@cine.com", "555903", "dust-keeper", 13, Rol.ADMIN, "Noche")
#empleados en taquilla
e4 = empleado(304, "Rosy Huerta", "r.huerta@cine.com", "555904", "garden-flowers", 14, Rol.TAQUILLERO, "Mañana")
e5 = empleado(305, "Irídia Luz", "i.luz@cine.com", "555905", "glow-shimmer", 15, Rol.TAQUILLERO, "Tarde")
e6 = empleado(306, "Vidia Veloz", "v.veloz@cine.com", "555906", "fast-wind", 16, Rol.TAQUILLERO, "Noche")
#empleados de limpieza
e7 = empleado(307, "Fany Fauna", "f.fauna@cine.com", "555907", "animal-lover", 17, Rol.LIMPIEZA, "Mañana")
e8 = empleado(308, "Marina Ríos", "m.rios@cine.com", "555908", "water-drop", 18, Rol.LIMPIEZA, "Tarde")
e9 = empleado(309, "Bob Roble", "b.roble@cine.com", "555909", "hammer-time", 19, Rol.LIMPIEZA, "Mañana")
e10 = empleado(310, "Clive Espino", "c.espino@cine.com", "555910", "builder-pixie", 20, Rol.LIMPIEZA, "Noche")

empleados = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
for e in empleados:
    print(f"Emp: {e.nombre} | Rol: {e.rol.name}")


print("\n--- salas creadas ---")
#creación de salas
s1 = sala(101, "Sala 01 Tradicional", "Planta Baja", TipoSala.DOSD, 60, False)
s2 = sala(201, "Sala 02 Tradicional", "Planta Baja", TipoSala.DOSD, 60, False)
s3 = sala(301, "Sala 03 Tradicional", "Planta Baja", TipoSala.DOSD, 60, False)
s4 = sala(401, "Sala 04 Premium", "Nivel 2", TipoSala.DOSD, 20, True)
s5 = sala(501, "Sala 05 Premium", "Nivel 2", TipoSala.DOSD, 20, True)
s6 = sala(602, "Sala 06 IMAX", "Ala Norte", TipoSala.IMAX, 80, True)
s7 = sala(702, "Sala 07 IMAX", "Ala Norte", TipoSala.IMAX, 80, True)
s8 = sala(802, "Sala 08 IMAX", "Ala Sur", TipoSala.IMAX, 40, True)
s9 = sala(903, "Sala 09 Vivencia 3D", "Planta Baja", TipoSala.TRESD, 40, False)
s10 = sala(103, "Sala 10 Vivencia 3D", "Planta Alta", TipoSala.TRESD, 30, False)

#
salas = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
for s in salas:
    print(f"ID: {s.idEspacio} | Sala: {s.nombreEspacio} | Tipo: {s.tipoSala} | VIP: {s.esVip}")


print("----------- Zonas de comida -----------")
z1 = zonaComida(601, "Dulcería", "Planta Baja", ["Gomitas", "Paletas Miguelito", "MilkyWay"], {"Gomitas":10, "Paletas Miguelito":15, "MilkyWay":20})
z2 = zonaComida(602, "Candies and cake", "Planta Baja", ["Pastel de Red Velvet", "Pay de queso", "Pay de limon"], {"Pastel de Red Velvet": 8, "Pay de queso": 15, "Pay de limon": 9})
z3 = zonaComida(603, "Coffee & Bar VIP", "Nivel 2", ["Expresso", "Latte", "Margarita"], {"Expresso":5, "Latte":8, "Margarita": 10})
z4 = zonaComida(604, "Snack Express", "Ala Norte", ["Barras de cereal", "Chocolate Delice", "Manzana enchilada"], {"Barras de cereal": 20, "Chocolate Delice": 30, "Manzana enchilada": 15})
z5 = zonaComida(605, "Palomería Especializada", "Ala Sur", ["Palomitas Naturales", "Palomitas de caramelo", "Palomitas de chile con limon", "Palomitas de chiles y especias", "Palomitas de queso cheddar"], {"Palomitas Naturales": 15, "Palomitas de caramelo": 25, "Palomitas de chile con limon": 30, "Palomitas de chiles y especias": 28, "Palomitas de queso cheddar": 25})
z6 = zonaComida(606, "Crepería", "Planta Baja", ["Crepa Dulce", "Crepa Salada"], {"Crepa Dulce":20, "Crepa Salada":15})
z7 = zonaComida(607, "Subway", "Planta Baja", ["Sandwich", "Galleta"], {"Sandwich":30, "Galleta":50})
z8 = zonaComida(608, "Starbucks", "Terraza", ["Frappuccino", "Muffin"], {"Frappuccino":25, "Muffin":20})
z9 = zonaComida(609, "Helados y paletas", "Planta Baja", ["Cono Vainilla", "Paleta de Agua"], {"Cono Vainilla":20, "Paleta de Agua":30})
z10 = zonaComida(610, "Pizzería", "Ala Norte", ["Rebanada Pepperoni", "Refresco Familiar"], {"Rebanada Pepperoni":40, "Refresco Familiar":1})

lista_zonasdeComida = [z1,z2,z3,z4,z5,z6,z7,z8,z9,z10]
for z in lista_zonasdeComida:
    print(f"ID: {z.idEspacio} | Local: {z.nombreEspacio} | Ubicación: {z.ubicacion}")
    print(f"   Stock disponible: {z.stockActual}")


print("-------------pelis----------------")
p1 = pelicula("Barbie: La Princesa y la Plebeya", 85, "AA", "Musical", "Erika y Anneliese intercambian vidas.")
p2 = pelicula("Barbie y las 12 Princesas Bailarinas", 82, "AA", "Fantasía", "Princesas descubren un mundo mágico para bailar.")
p3 = pelicula("Oppenheimer", 180, "C", "Drama/Histórico", "El físico J. Robert Oppenheimer trabaja en el Proyecto Manhattan.")
p4 = pelicula("Interstellar", 169, "B", "Sci-Fi", "Un grupo de exploradores viaja a través de un agujero de gusano.")
p5 = pelicula("Blade Runner 2049", 164, "B15", "Sci-Fi", "Un oficial descubre un secreto que podría terminar con el caos.")
p6 = pelicula("The Love Hypothesis", 120, "B", "Romance", "Una científica finge una relación con un hombre misterioso.")
p7 = pelicula("Orgullo y Prejuicio", 129, "A", "Romance", "La vida de cinco hermanas cambia con la llegada de un joven rico.")
p8 = pelicula("About Time", 123, "B", "Romance/Fantasía", "Tim descubre que puede viajar en el tiempo para mejorar su amor.")
p9 = pelicula("2012", 158, "B", "Acción/Desastre", "El mundo se enfrenta a catástrofes naturales masivas.")
p10 = pelicula("Spider-Man: Across the Spider-Verse", 140, "A", "Animación", "Miles Morales viaja a través del multiverso.")

# 
lista_peliculas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
for p in lista_peliculas:
    print(f"Título: {p.titulo} | Clasificación: {p.clasificacion} | Duración: {p.duracion} min")

print("----------- Descuentos -----------")
pr1 = promocion("CineStudy", "Descuento con credencial de estudiante vigente", 0.20, "2026-12-31")
pr2 = promocion("INAPAMCin3", "Descuento para adultos mayores", 0.35, "2026-12-31")
pr3 = promocion("SemanaConCin3", "Lunes de combo: descuento en entradas al comprar palomitas", 0.15, "2026-06-30")
pr4 = promocion("BonneJourné3", "Descuento en funciones antes de las 2:00 PM", 0.25, "2026-08-15")
pr5 = promocion("FielCinefil0", "Exclusivo para miembros del club de fidelidad", 0.10, "2026-12-31")
pr6 = promocion("Acaramelado5", "Descuento en la compra de 2 boletos de romance", 0.30, "2026-02-28")
pr7 = promocion("CríticoNocturn0", "Funciones después de las 10:00 PM", 0.20, "2026-05-20")
pr8 = promocion("HappyCinemaBirthd4y", "Descuento especial el día de tu cumpleaños", 0.50, "2026-12-31")
pr9 = promocion("Reale5", "Descuento en la segunda entrada para IMAX", 0.15, "2026-07-30")
pr10 = promocion("AMediaFunción", "Precio especial de mitad de semana", 0.40, "2026-12-31")

lista_promos = [pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8, pr9, pr10]
for pr in lista_promos:
    print(f"Código es {pr.codigo} | Descripción {pr.descripcion} | Porcentaje(20%=0.2) -> {pr.porcentajeDescuento} | Vencimiento es {pr.fechaExpiracion}")


print("-------------Funciones | hora y sala -----------")

fun1 = funcion(401, p1, s9, "14:00", 70.0)
fun2 = funcion(402, p3, s6, "18:00", 150.0)
fun3 = funcion(403, p4, s7, "21:00", 140.0)
fun4 = funcion(404, p6, s4, "19:00", 180.0)
fun5 = funcion(405, p10, s1, "16:00", 85.0)
fun6 = funcion(406, p2, s10, "13:00", 65.0)
fun7 = funcion(407, p5, s8, "22:00", 110.0)
fun8 = funcion(408, p7, s2, "17:30", 80.0)
fun9 = funcion(409, p9, s3, "20:00", 80.0)
fun10 = funcion(410, p8, s5, "21:30", 180.0)

lista_funciones = [fun1, fun2, fun3, fun4, fun5, fun6, fun7, fun8, fun9, fun10]
for fun in lista_funciones:
    print(f"ID: {fun.idFuncion} | Peli: {fun.pelicula.titulo} | Horario: {fun.horarioInicio}")


#Para imprimir las reservas primero tenemos que apartar los lugares
fun8.reservarAsientos(["E5", "E6"])
fun2.reservarAsientos(["H10"])
fun1.reservarAsientos(["C1", "C2"])
fun3.reservarAsientos(["A1"])
fun5.reservarAsientos(["G7"])
fun10.reservarAsientos(["F12"])
fun9.reservarAsientos(["B4"])
fun6.reservarAsientos(["B1", "B2"])
fun4.reservarAsientos(["D8"])
fun7.reservarAsientos(["J1"])

print("--------------Resevas---------------")
res1 = reserva(1001, u7, fun8, ["E5", "E6"], fun8.precioBase * 2)
res2 = reserva(1002, u1, fun2, ["H10"], fun2.precioBase * 1)
res3 = reserva(1003, u2, fun1, ["C1", "C2"], fun1.precioBase * 2)
res4 = reserva(1004, u5, fun3, ["A1"], fun3.precioBase * 1)
res5 = reserva(1005, u6, fun5, ["G7"], fun5.precioBase * 1)
res6 = reserva(1006, u8, fun10, ["F12"], fun10.precioBase * 1)
res7 = reserva(1007, u1, fun9, ["B4"], fun9.precioBase * 1)
res8 = reserva(1008, u7, fun6, ["B1", "B2"], fun6.precioBase * 2)
res9 = reserva(1009, u2, fun4, ["D8"], fun4.precioBase * 1)
res10 = reserva(1010, u5, fun7, ["J1"], fun7.precioBase * 1)

lista_reservas = [res1, res2, res3, res4, res5, res6, res7, res8, res9, res10]
for res in lista_reservas:
    res.generarTicket()

def loginSistema():
    print("\n===== LOGIN =====")
    id_ingresado = int(input("ID persona: "))
    password = input("Contraseña: ")


    for u in usuarios:
        if u.login(id_ingresado, password):
            menuUsuario(u)
            return

    # buscar en empleados
    for e in empleados:
        if e.login(id_ingresado, password):
            menuEmpleado(e)
            return

    print("Credenciales incorrectas")


# Menu usuario
def menuUsuario(usuario):
    while True:
        print(f"\n--- Menú Usuario ({usuario.nombre}) ---")
        print("1. Ver funciones")
        print("2. Crear reserva")
        print("3. Ver promociones")
        print("4. Cancelar reserva")
        print("5. Cerrar sesión")

        op = input("Seleccione: ")

        if op == "1":
            for f in lista_funciones:
                print(f"{f.idFuncion} | {f.pelicula.titulo} | {f.horarioInicio}")

        elif op == "2":
            id_func = int(input("ID de función: "))
            asientos = input("Asientos separados por coma (ej. A1,B3): ").split(",")

            for f in lista_funciones:
                if f.idFuncion == id_func:
                    nueva = reserva(
                        len(lista_reservas) + 1000,
                        usuario,
                        f,
                        asientos,
                        f.precioBase * len(asientos)
                    )
                    usuario.crearReserva(nueva)
                    lista_reservas.append(nueva)

        elif op == "3":
            usuario.consultarPromociones(lista_promos)

        elif op == "4":

            print("\n--- Tus reservas ---")
            for r in usuario.historialReserva:
                print(f"ID Reserva: {r.idReserva} | Película: {r.funcion.pelicula.titulo} | Estado: {r.estado}")

            id_res = int(input("Ingrese el ID de la reserva a cancelar: "))
            usuario.cancelarReserva(id_res)

        elif op == "5":
            usuario.logout()
            break


# Menu empleado
def menuEmpleado(emp):
    while True:
        print(f"\n--- Menú Empleado ({emp.nombre}) ---")
        print("1. Marcar entrada")
        print("2. Ver funciones")
        print("3. Vender producto comida")
        print("4. Cerrar sesión")

        if emp.rol == Rol.ADMIN:
            print("5. Gestionar funciones")
            print("6. Agregar película")
            print("7. Agregar función")
            print("8. Agregar promoción")
            print("9. Ajustar aforo de sala")

        op = input("Seleccione: ")

        if op == "1":
            emp.marcarEntrada()

        elif op == "2":
            for f in lista_funciones:
                print(f"{f.idFuncion} | {f.pelicula.titulo} | {f.horarioInicio}")

        elif op == "3":
            for z in lista_zonasdeComida:
                print(f"{z.idEspacio} - {z.nombreEspacio}")

            id_zona = int(input("Zona: "))
            for z in lista_zonasdeComida:
                if z.idEspacio == id_zona:
                    z.venderProducto()

        elif op == "4":
            emp.logout()
            break

        elif op == "5" and emp.rol == Rol.ADMIN:
            emp.gestionarFunciones()

        elif op == "6" and emp.rol == Rol.ADMIN:

            titulo = input("Título: ")
            dur = int(input("Duración: "))
            clas = input("Clasificación: ")
            gen = input("Género: ")
            sin = input("Sinopsis: ")

            nueva = pelicula(titulo, dur, clas, gen, sin)
            emp.agregarPelicula(lista_peliculas, nueva)
        
        elif op == "7" and emp.rol == Rol.ADMIN:

            idf = int(input("ID función: "))

            for i,p in enumerate(lista_peliculas):
                print(i, p.titulo)

            peli = lista_peliculas[int(input("Seleccionar película: "))]

            for i,s in enumerate(salas):
                print(i, s.nombreEspacio)

            sala_sel = salas[int(input("Seleccionar sala: "))]

            hora = input("Horario: ")
            precio = float(input("Precio base: "))

            nueva_func = funcion(idf, peli, sala_sel, hora, precio)

            emp.agregarFuncion(lista_funciones, nueva_func)

        elif op == "8" and emp.rol == Rol.ADMIN:

            codigo = input("Código: ")
            desc = input("Descripción: ")
            porc = float(input("Porcentaje (0.2 = 20%): "))
            fecha = input("Fecha expiración YYYY-MM-DD: ")

            nueva = promocion(codigo, desc, porc, fecha)

            emp.agregarPromocion(lista_promos, nueva)
        
        elif op == "9" and emp.rol == Rol.ADMIN:

            print("\n--- Salas disponibles ---")
            for i, s in enumerate(salas):
                print(i, s.nombreEspacio, "| capacidad:", s.capacidadTotal)

            seleccion = int(input("Seleccione sala: "))

            salas[seleccion].ajustarAforo()

while True:
    print("\n===== SISTEMA CINE =====")
    print("1. Iniciar sesión")
    print("2. Salir")

    op = input("Opción: ")

    if op == "1":
        loginSistema()
    elif op == "2":
        print("Adiós")
        break