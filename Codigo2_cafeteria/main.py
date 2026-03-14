from Models import *
print("\n")

#Creación de objetos (clientes)
cli1 = Cliente(101, "Tomás", "tomas@email.com", "pass1", 150)
cli2 = Cliente(102, "Mariana", "mari@email.com", "pass2", 40)
cli3 = Cliente(103, "Ignacio", "nacho@email.com", "pass3", 300)
cli4 = Cliente(104, "Camila", "cami@email.com", "pass4", 10)
cli5 = Cliente(105, "Bruno", "bruno@email.com", "pass5", 85)
cli6 = Cliente(106, "Lucía", "lu@email.com", "pass6", 120)
cli7 = Cliente(107, "Felipe", "felipe@email.com", "pass7", 5)
cli8 = Cliente(108, "Renata", "rena@email.com", "pass8", 210)
cli9 = Cliente(109, "Sebastian", "sebas@email.com", "pass9", 60)
cli10 = Cliente(110, "Victoria", "vicky@email.com", "pass10", 0)
clientes = [cli1, cli2, cli3, cli4, cli5, cli6, cli7, cli8, cli9, cli10]
for c in clientes:
    (c.mostrarDetalle())


print("\n")

print(cli8.login(108, "pass8"))
print(cli10.login(110, "contraseñaincorrecta"))

cli8.actualizarPerfil(nombre="Reny")
print(cli8.nombre)

(cli8.logout())

cli5.puntosFidelidad += 50 
print(f"Puntos tras la compra: {cli5.puntosFidelidad}")

#creamos productos y pedido para hacer la prueba
latte = Bebida(1,"Latte",30,10,"Mediano",Temperatura.CALIENTE)
brownie = Postre(2,"Brownie",25,5)
pedido1 = Pedido(1,[latte,brownie])
cli1.realizarPedido(pedido1,10)
cli1.consultarHistorial()
cli2.consultarHistorial()

print("\n")
#Creación de objetos (Empleados)
emp1 = Empleado(1, "Mateo", "mateo@cafe.com", "pass1", "E-001", Puesto.BARISTA)
emp2 = Empleado(2, "Valeria", "val@cafe.com", "pass2", "E-002", Puesto.MESERO)
emp3 = Empleado(3, "Lucas", "lucas@cafe.com", "pass3", "E-003", Puesto.GERENTE)
emp4 = Empleado(4, "Sofía", "sofi@cafe.com", "pass4", "E-004", Puesto.BARISTA)
emp5 = Empleado(5, "Andrés", "andres@cafe.com", "pass5", "E-005", Puesto.MESERO)
emp6 = Empleado(6, "Carla", "carla@cafe.com", "pass6", "E-006", Puesto.BARISTA)
emp7 = Empleado(7, "Julián", "juli@cafe.com", "pass7", "E-007", Puesto.GERENTE)
emp8 = Empleado(8, "Daniela", "dani@cafe.com", "pass8", "E-008", Puesto.MESERO)
emp9 = Empleado(9, "Ricardo", "richie@cafe.com", "pass9", "E-009", Puesto.BARISTA)
emp10 = Empleado(10, "Elena", "elena@cafe.com", "pass10", "E-010", Puesto.MESERO)
empleados=[emp1, emp2,emp3, emp4, emp5, emp6, emp7, emp7, emp8, emp9, emp10]
for e in empleados:
    (e.mostrarDetalle())

#creamos objetos para la prueba
latte = Bebida(1,"Latte",30,10,"Mediano",Temperatura.CALIENTE)
brownie = Postre(2,"Brownie",25,5)
inventario = Inventario()
inventario.agregarIngrediente("Latte",5)
inventario.agregarIngrediente("Brownie",5)
pedido2 = Pedido(2,[latte,brownie])
pedido2.inventario = inventario
#Prueba
print("Estado del pedido:", pedido2.estado)
pedido2.procesarPedido()
print("Estado del pedido:", pedido2.estado)
print(inventario.mostrarInventario())
emp7.actualizarInventario(inventario,"Latte",10)
emp8.actualizarInventario(inventario,"Brownie",5)
print(inventario.mostrarInventario())

print("\n")
# Creación de objetos (Bebida)
bev1 = Bebida(301, "Espresso", 2.50, 100, "Pequeño", "Caliente")
bev2 = Bebida(302, "Americano", 3.00, 150, "Mediano", "Caliente")
bev3 = Bebida(303, "Latte", 4.25, 80, "Grande", "Caliente")
bev4 = Bebida(304, "Cappuccino", 4.00, 60, "Mediano", "Caliente")
bev5 = Bebida(305, "Flat White", 3.75, 50, "Pequeño", "Caliente")
bev6 = Bebida(306, "Cold Brew", 4.50, 40, "Grande", "Frío")
bev7 = Bebida(307, "Iced Caramel Macchiato", 5.50, 30, "Grande", "Frío")
bev8 = Bebida(308, "Mocaccino", 4.80, 45, "Mediano", "Caliente")
bev9 = Bebida(309, "Té Matcha Latte", 5.00, 25, "Mediano", "Caliente")
bev10 = Bebida(310, "Frappuccino de Vainilla", 5.75, 20, "Grande", "Frío")
bebidas=[bev1,bev2,bev3,bev4,bev5,bev6,bev7,bev8,bev9,bev10]
for b in bebidas:
    print(f"Id: {b.idProducto}| Nombre: {b.nombreProducto}| Precio : {b.precioBase}| Stock: {b.stock}")

extra6  = Extra("Crema Batida", 0.60)
bev6.agregar_extra(extra6) #elegimos el extra que se le agrega a la bebida
print(f"La bebida mas el extra: \n {bev6.calcular_precio_final()}$") #calcula el precio final    con el agregado

print("\n")
# Creación de objetos (Postre)
postre1 = Postre(401, "Muffin de Arándanos", 3.50, 20)
postre2 = Postre(402, "Brownie de Chocolate", 3.00, 15)
postre3 = Postre(403, "Galleta de Avena y Pasas", 2.50, 25)
postre3.esVegano = True
postre4 = Postre(404, "Cheesecake de Frutos Rojos", 4.50, 10)
postre5 = Postre(405, "Tarta de Manzana", 4.00, 12)
postre6 = Postre(406, "Alfajor de Maicena", 2.00, 30)
postre6.sinGluten = True
postre7 = Postre(407, "Croissant de Mantequilla", 2.80, 18)
postre8 = Postre(408, "Budín de Limón y Amapola", 3.20, 10)
postre8.esVegano = True
postre8.sinGluten = True
postre9 = Postre(409, "Donut Glaseada", 2.25, 20)
postre10 = Postre(410, "Tiramisú", 5.00, 8)
postres=[postre1,postre2,postre3,postre4,postre5,postre6,postre7,postre8,postre9,postre10]
for p in postres:
    print(f"Id: {p.idProducto}| Nombre: {p.nombreProducto}| Precio : {p.precioBase}| Stock: {p.stock}")

print("\n")
#Prueba
top9 = Topping("Galleta Oreo Triturada", 0.90)
postre10.agregarTopping(top9)
print(f"\n El postre mas el topping: {postre10.calcular_precio_final()}$")

#Creación de extras para la bebida
extra1  = Extra("Leche de Almendras", 0.80)
extra2  = Extra("Leche de Avena", 0.90)
extra3  = Extra("Shot de Espresso adicional", 1.20)
extra4  = Extra("Sirope de Vainilla", 0.50)
extra5  = Extra("Sirope de Caramelo", 0.50)
extra7  = Extra("Chips de Chocolate", 0.40)
extra8  = Extra("Canela en polvo", 0.20)
extra9  = Extra("Hielo extra", 1.00)
extra10 = Extra("Endulzante de Monje", 0.30)

# Creación de toppings para el postre
top1 = Topping("Crema Batida", 0.60)
top2 = Topping("Chispas de Chocolate", 0.50)
top3 = Topping("Canela en Polvo", 0.20)
top4 = Topping("Sirope de Chocolate Hershey's", 0.70)
top5 = Topping("Caramelo Líquido", 0.70)
top6 = Topping("Nuez Picada", 0.85)
top7 = Topping("Malvaviscos Pequeños", 0.55)
top8 = Topping("Polvo de Cacao amargo", 0.30)
top10 = Topping("Ralladura de Naranja", 0.40)


print("\n")

mi_inventario = Inventario()

mi_inventario.ingredientes = {
    #Bebidas
    bev1.nombreProducto: bev1.stock,
    bev2.nombreProducto: bev2.stock,
    bev3.nombreProducto: bev3.stock,
    bev4.nombreProducto: bev4.stock,
    bev5.nombreProducto: bev5.stock,
    bev6.nombreProducto: bev6.stock,
    bev7.nombreProducto: bev7.stock,
    bev8.nombreProducto: bev8.stock,
    bev9.nombreProducto: bev9.stock,
    bev10.nombreProducto: bev10.stock,
    #Postres
    postre1.nombreProducto: postre1.stock,
    postre2.nombreProducto: postre2.stock,
    postre3.nombreProducto: postre3.stock,
    postre4.nombreProducto: postre4.stock,
    postre6.nombreProducto: postre6.stock,
    postre8.nombreProducto: postre8.stock,
    postre10.nombreProducto: postre10.stock
}

print(mi_inventario.mostrarInventario())
print("¿Hay stock?")
print(mi_inventario.validarStockProducto(postre6))

print("\n")
mi_inventario.reducirStock(bev10.nombreProducto, 10)
print("\n")
print(mi_inventario.mostrarInventario())
mi_inventario.reducirStock(bev10.nombreProducto, 80)


print("\n")
# Creación de objetos (Pedido)
ped1  = Pedido(2001, [bev1, postre7], EstadoPedido.PENDIENTE, 5.30)
ped2  = Pedido(2002, [bev3], EstadoPedido.PREPARANDO, 4.25)
ped3  = Pedido(2003, [bev10, postre2], EstadoPedido.ENTREGADO, 8.75)
ped4  = Pedido(2004, [bev6, postre6], EstadoPedido.PENDIENTE, 6.50)
ped5  = Pedido(2005, [bev7], EstadoPedido.PREPARANDO, 5.50)
ped6  = Pedido(2006, [bev2, postre3], EstadoPedido.ENTREGADO, 5.50)
ped7  = Pedido(2007, [bev9], EstadoPedido.PENDIENTE, 5.00)
ped8  = Pedido(2008, [bev4, postre1], EstadoPedido.PREPARANDO, 7.50)
ped9  = Pedido(2009, [bev5, postre8], EstadoPedido.ENTREGADO, 6.95)
ped10 = Pedido(2010, [bev8, postre4], EstadoPedido.PENDIENTE, 9.30)
pedidos=[ped1, ped2, ped3, ped5, ped6, ped7, ped8, ped9, ped10, ped4]
for ped in pedidos:
    print(f"Id del pedido: {ped.idPedido} | Estado: {ped.estado.name} | Total: {ped.total}")

ped7.inventario = mi_inventario

#calculo del costo sin puntos y con puntos
print(ped7.calcularTotal(0))
print(ped7.calcularTotal(3))

print(ped7.validarStock())
#vaciamos el stock
mi_inventario.reducirStock(bev9.nombreProducto,bev9.stock)
#intentamos procesar el pedido
ped7.procesarPedido()

#Menú interactivo
def menu_principal():
    while True:
        print("\n" + "="*30)
        print(">>> BIENVENIDO A COFFEE Fcc <<<")
        print("=======================================")
        print("1. Soy Cliente")
        print("2. Soy Empleado")
        print("3. Salir")
        
        tipo_usuario = input("Seleccione una opción: ")

        if tipo_usuario == "1":
            id_buscado = int(input("Ingrese su ID de Cliente: "))
            password = input("Ingrese su contraseña: ")
            
            cliente_logueado = next((c for c in clientes if c.login(id_buscado, password)), None)
            
            if cliente_logueado:
                menu_cliente(cliente_logueado)
            else:
                print("Credenciales incorrectas.")

        elif tipo_usuario == "2":
            id_buscado = int(input("Ingrese su ID de Empleado: "))
            password = input("Ingrese su contraseña: ")
            
            emp_logueado = next((e for e in empleados if e.login(id_buscado, password)), None)
            
            if emp_logueado:
                menu_empleado(emp_logueado)
            else:
                print("Credenciales incorrectas.")

        elif tipo_usuario == "3":
            print("Gracias por su preferencia")
            break

def buscar_producto_por_id(id_buscado):
    todas_las_opciones = bebidas + postres
    return next((p for p in todas_las_opciones if p.idProducto == id_buscado), None)

def menu_cliente(cliente):
    while True:
        print(f"\n--- BIENVENIDO {cliente.nombre.upper()} ---")
        print(f"Puntos acumulados: {cliente.puntosFidelidad}")
        print("1. Ver Menú y Realizar Pedido")
        print("2. Ver mi historial de compras")
        print("3. Cerrar Sesión")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--------- MENÚ ---------")
            print("BEBIDAS:")
            for b in bebidas:
                print(f"  [{b.idProducto}] {b.nombreProducto} - ${b.precioBase}")
            
            print("\nPOSTRES:")
            for p in postres:
                print(f"  [{p.idProducto}] {p.nombreProducto} - ${p.precioBase}")
            
            productos_seleccionados = []
            while True:
                id_p = int(input("\nIngrese el ID del producto para agregar (o 0 para finalizar selección): "))
                if id_p == 0: break
                
                prod = buscar_producto_por_id(id_p)
                if prod:
                    productos_seleccionados.append(prod)
                    print(f" {prod.nombreProducto} agregado.")
                else:
                    print(" ID no encontrado.")
                
                for prod in productos_seleccionados:
                    if isinstance(prod, Bebida):
                        resp = input(f"¿Deseas agregar un extra a tu {prod.nombreProducto}? (Escribe s si lo deseas/ escribe n de lo contrario): ")
                        if resp.lower() == "s":
                            print("Extras disponibles:")
                            extras_disponibles = [extra1, extra2, extra3, extra4, extra5, extra6, extra7, extra8, extra9, extra10]
                            for i, e in enumerate(extras_disponibles):
                                print(f"{i+1}. {e.nombre} - ${e.precio}")
                            opcion_extra = int(input("Selecciona el número del extra: "))
                            if 1 <= opcion_extra <= len(extras_disponibles):
                                prod.agregar_extra(extras_disponibles[opcion_extra-1])
                                print("Extra agregado.")

                    elif isinstance(prod, Postre):
                        resp = input(f"¿Deseas agregar un topping a tu {prod.nombreProducto}? (Escribe s si lo deseas/ escribe n de lo contrario): ")
                        if resp.lower() == "s":
                            print("Toppings disponibles:")
                            toppings_disponibles = [top1, top2, top3, top4, top5, top6, top7, top8, top9, top10]
                            for i, t in enumerate(toppings_disponibles):
                                print(f"{i+1}. {t.nombre} - ${t.precio}")
                            opcion_top = int(input("Selecciona el número del topping: "))
                            if 1 <= opcion_top <= len(toppings_disponibles):
                                prod.agregarTopping(toppings_disponibles[opcion_top-1])
                                print("Topping agregado.")

            if productos_seleccionados:
                nuevo_id_pedido = 2000 + len(pedidos) + 1
                nuevo_pedido = Pedido(nuevo_id_pedido, productos_seleccionados)
                nuevo_pedido.inventario = mi_inventario
                
                print(f"\nTotal previo: ${sum(p.calcular_precio_final() for p in productos_seleccionados)}")
                puntos = int(input(f"¿Cuántos puntos quieres canjear? (Tienes {cliente.puntosFidelidad}): "))
                
                cliente.realizarPedido(nuevo_pedido, puntos)
                pedidos.append(nuevo_pedido)
            else:
                print("No seleccionaste ningún producto.")

        elif opcion == "2":
            cliente.consultarHistorial()
            
        elif opcion == "3":
            cliente.logout()
            break

def menu_empleado(empleado):
    while True:
        print(f"\n--- PANEL DE CONTROL: {empleado.nombre} ({empleado.rol.name}) ---")
        
        if empleado.rol == Puesto.BARISTA:
            print("1. Ver pedidos PENDIENTES")
            print("2. Preparar siguiente pedido")
            
        elif empleado.rol == Puesto.GERENTE:
            print("1. Revisar Inventario ")
            print("2. Ver pedidos en progreso o finalizados")
            print("3. Modificar stock de ingredientes")
            
        elif empleado.rol == Puesto.MESERO:
            print("1. Marcar pedido como ENTREGADO")
        
        print("0. Salir")
        opcion = input("Seleccione acción: ")

        if opcion == "0":
            empleado.logout()
            break
            
        if empleado.rol == Puesto.BARISTA:
            if opcion == "1":
                for p in pedidos:
                    if p.estado == EstadoPedido.PENDIENTE:
                        print(f"Pedido #{p.idPedido} - Total: {p.total}")
            elif opcion == "2":
                ped_pend = next((p for p in pedidos if p.estado == EstadoPedido.PENDIENTE), None)
                if ped_pend:
                    empleado.cambiarEstadoPedido(ped_pend, EstadoPedido.PREPARANDO)
                else:
                    print("No hay pedidos pendientes.")

        elif empleado.rol == Puesto.GERENTE:
            #print("1. Revisar Inventario Completo")
            #print("2. Ver pedidos en progreso o finalizados")
            #print("3. Modificar Stock de Ingredientes")
            #print("0. Salir")
            
            #opcion = input("Seleccione acción: ")

            if opcion == "1":
                print("\n--- ESTADO DEL INVENTARIO ---")
                inv = mi_inventario.mostrarInventario()

                for nombre, cantidad in inv.items():
                    print(f"{nombre}: {cantidad}")

            elif opcion == "2":
                print("\n--- REPORTE DE VENTAS ---")
                for p in pedidos:
                    print(f"Pedido #{p.idPedido} | Total: ${p.total:.2f} | Estado: {p.estado.name}")

            elif opcion == "3":
                ingrediente = input("Nombre del ingrediente a modificar: ")
                try:
                    cantidad = int(input("Cantidad a añadir (ej. 10): "))
                    empleado.actualizarInventario(mi_inventario, ingrediente, cantidad)
                except ValueError:
                    print(" Error: Ingresa un número válido.")
            
            elif opcion == "0":
                break
        
        elif empleado.rol == Puesto.MESERO:
            if opcion == "1":
                id_p = int(input("ID del pedido entregado: "))
                ped_e = next((p for p in pedidos if p.idPedido == id_p), None)
                if ped_e:
                    empleado.cambiarEstadoPedido(ped_e, EstadoPedido.ENTREGADO)


menu_principal()