from Models import *

print("----------Usuarios creados----------")
#creación de usuarios
u1 = Usuario(1, "Carlos Arenas", "carlos88@mail.com", "222101", "pass123", 0)
u2 = Usuario(2, "Ana Karenina", "anak@mail.com", "222102", "safe789", 0)
u3 = Usuario(3, "Roberto Gomez", "robert@mail.com", "222103", "gomez22", 0)
u4 = Usuario(4, "Lucia Mendez", "luci_m@mail.com", "222104", "mendez99", 0)
u5 = Usuario(5, "Fernando Soler", "fher_s@mail.com", "222105", "cine123", 0)
u6 = Usuario(6, "Mariana Rios", "marios@mail.com", "222106", "rios44", 0)
u7 = Usuario(7, "Jorge Negrete", "jnegrete@mail.com", "222107", "jorge01", 0)
u8 = Usuario(8, "Silvia Pinal", "silvia_p@mail.com", "222108", "pinal88", 0)
u9 = Usuario(9, "Pedro Infante", "p_infante@mail.com", "222109", "torito", 0)
u10 = Usuario(10, "Dolores Rio", "dolores_r@mail.com", "222110", "rio555", 0)

usuarios = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10]
for u in usuarios:
    print(f"ID: {u.idPersona} | Nombre: {u.nombre} | Correo: {u.email} | Puntos: {u.puntosFidelidad}")


print("----------Empleados creados----------")
#creación de empleados
e1 = empleado(101, "Juan Admin", "juan@cine.com", "5551", "admin1", 1, Rol.ADMIN, "Mañana")
e2 = empleado(102, "Pedro Vend", "pedro@cine.com", "5552", "vend2", 2, Rol.TAQUILLERO, "Tarde")
e3 = empleado(103, "Luis Vend", "luis@cine.com", "5553", "vend3", 3, Rol.LIMPIEZA, "Mañana")
e4 = empleado(104, "Marta Vend", "marta@cine.com", "5554", "vend4", 4, Rol.TAQUILLERO, "Tarde")
e5 = empleado(105, "Sofía Admin", "sofia@cine.com", "5555", "admin5", 5, Rol.ADMIN, "Noche")
e6 = empleado(106, "Gaby Vend", "gaby@cine.com", "5556", "vend6", 6, Rol.TAQUILLERO, "Mañana")
e7 = empleado(107, "Jose Vend", "jose@cine.com", "5557", "vend7", 7, Rol.LIMPIEZA, "Tarde")
e8 = empleado(108, "Dani Vend", "dani@cine.com", "5558", "vend8", 8, Rol.TAQUILLERO, "Noche")
e9 = empleado(109, "Kike Admin", "kike@cine.com", "5559", "admin9", 9, Rol.ADMIN, "Mañana")
e10 = empleado(110, "Leo Vend", "leo@cine.com", "5550", "vend10", 10, Rol.LIMPIEZA, "Tarde")

empleados = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
for e in empleados:
    print(f"Emp: {e.nombre} | Rol: {e.rol.name}")

print("\n--- salas creadas ---")
#creación de salas
s1 = sala(1, "Sala IMAX 1", "Planta Alta", "IMAX", 50, True)
s2 = sala(2, "Sala 2D Premium", "Planta Baja", "2D", 40, False)
s3 = sala(3, "Sala 3D Junior", "Planta Alta", "3D", 30, False)
s4 = sala(4, "Sala Macro XE", "Planta Baja", "Macro", 60, True)
s5 = sala(5, "Sala 4DX", "Planta Alta", "4DX", 24, True)
s6 = sala(6, "Sala 2D Estándar", "Planta Baja", "2D", 45, False)
s7 = sala(7, "Sala VIP 1", "Piso 2", "VIP", 20, True)
s8 = sala(8, "Sala VIP 2", "Piso 2", "VIP", 20, True)
s9 = sala(9, "Sala IMAX 2", "Planta Alta", "IMAX", 50, True)
s10 = sala(10, "Sala Experimental", "Sótano", "2D", 15, False)

salas = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
for s in salas:
    print(f"ID: {s.idEspacio} | Sala: {s.nombreEspacio} | Tipo: {s.tipoSala} | VIP: {s.esVip}")

print("-------------pelis----------------")
pel1 = pelicula("The Batman", 176, "B", "Acción", "Detective en Gotham")
pel2 = pelicula("Spiderman: No Way Home", 148, "A", "Acción", "Multiverso abierto")
pel3 = pelicula("Avengers: Endgame", 181, "B", "Sci-Fi", "Batalla final")
pel4 = pelicula("Dune: Parte 2", 166, "B", "Aventura", "Guerra en Arrakis")
pel5 = pelicula("Soul", 100, "AA", "Animación", "En busca del alma")
pel6 = pelicula("Super Mario Bros", 92, "AA", "Animación", "Reino Champiñón")
pel7 = pelicula("Oppenheimer", 180, "C", "Drama", "Bomba atómica")
pel8 = pelicula("Inception", 148, "B", "Suspenso", "Robo de sueños")
pel9 = pelicula("Toy Story", 81, "AA", "Animación", "Juguetes vivos")
pel10 = pelicula("Pulp Fiction", 154, "C", "Crimen", "Historias cruzadas")

lista_peliculas = [pel1, pel2, pel3, pel4, pel5, pel6, pel7, pel8, pel9, pel10]
for peli in lista_peliculas:
    print(f"Título: {peli.titulo} | Clasificación: {peli.clasificacion} | Duración: {peli.duracion} min")


print("-------------funciones--------")

fun1 = funcion(101, pel1, s1, "14:00", 80.0)
fun2 = funcion(102, pel2, s2, "15:30", 70.0)
fun3 = funcion(103, pel3, s3, "17:00", 75.0)
fun4 = funcion(104, pel4, s4, "18:45", 90.0)
fun5 = funcion(105, pel5, s5, "13:00", 65.0)
fun6 = funcion(106, pel6, s6, "16:15", 70.0) # <--- Aquí estaba el error, ya quedó corregido
fun7 = funcion(107, pel7, s7, "20:00", 120.0)
fun8 = funcion(108, pel8, s8, "21:30", 110.0)
fun9 = funcion(109, pel9, s9, "12:00", 60.0)
fun10 = funcion(110, pel10, s10, "22:00", 85.0)

lista_funciones = [fun1, fun2, fun3, fun4, fun5, fun6, fun7, fun8, fun9, fun10]
for f in lista_funciones:
    print(f"ID: {f.idFuncion} | Peli: {f.pelicula.titulo} | Horario: {f.horarioInicio}")


print("-------------reservas--------")
res1 = reserva(501, u1, fun1, ["A1", "A2"], 160.0)
res2 = reserva(502, u2, fun2, ["B5"], 70.0)
res3 = reserva(503, u3, fun3, ["C1", "C2", "C3"], 225.0)
res4 = reserva(504, u4, fun4, ["H10"], 90.0)
res5 = reserva(505, u5, fun5, ["A3", "A4"], 130.0)
res6 = reserva(506, u6, fun6, ["F1"], 70.0)
res7 = reserva(507, u7, fun7, ["VIP-01"], 120.0)
res8 = reserva(508, u8, fun8, ["VIP-05"], 110.0)
res9 = reserva(509, u9, fun9, ["D8", "D9"], 120.0)
res10 = reserva(510, u10, fun10, ["J1"], 85.0)

lista_reservas = [res1, res2, res3, res4, res5, res6, res7, res8, res9, res10]
for r in lista_reservas:
    print(f"Reserva: {r.idReserva} | Usuario: {r.usuario.nombre} | Total: ${r.montoTotal} | Estado: {r.estado}")

print(f"USUARIO: {u1.nombre} | PUNTOS: {u1.puntosFidelidad}")
print(f"SALA: {s3.nombreEspacio} | LIMPIA: {s3.esVip}")
print(f"RESERVAS PREVIAS: {len(u1.historialReserva)}")
u1.crearReserva(res1)
u1.puntosFidelidad += 50
s3.esVip = True
print("\n--- RESULTADOS DE LA VALIDACIÓN ---")
print(f"ID RESERVA GENERADA: {u1.historialReserva[0].idReserva}")
print(f"PELÍCULA: {u1.historialReserva[0].funcion.pelicula.titulo}")
print(f"NUEVOS PUNTOS {u1.nombre}: {u1.puntosFidelidad}")
print(f"SALA {s3.nombreEspacio} ACTUALIZADA - LIMPIA: {s3.esVip}")
print("="*50)
print("PRUEBA FINALIZADA CON ÉXITO")