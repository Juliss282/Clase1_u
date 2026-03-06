from enum import Enum

class Rol(Enum):
    TAQUILLERO = 1
    ADMIN = 2
    LIMPIEZA = 3
class TipoSala(Enum):
    DOSD = "2D"
    TRESD = "3D"
    IMAX = "IMAX"

class persona():

    def __init__(self,idPersona, nombre, email, telefono, contraseña):
        self.idPersona=idPersona
        self.nombre=nombre
        self.email=email
        self.telefono=telefono
        self.contraseña=contraseña
        self.sesionActiva=False
    
    def login(self, idPersonaIngresado, contraseñaIngresada):
        if idPersonaIngresado == self.idPersona and contraseñaIngresada == self.contraseña:
            self.sesion_activa = True
            print(f"Bienvenido {self.nombre}")
            return True
        return False
     
    def logout(self):
        
        self.sesionActiva = False
        print(f"{self.nombre} cerró sesión")
    
    def actDatos(self, nombre=None, email=None, telefono=None):
        if nombre:
            self.nombre=nombre
        if email:
            self.email=email
        if telefono:
            self.telefono=telefono
 


class Usuario(persona):
    def __init__(self, idPersona, nombre, email, telefono, contraseña, puntosFidelidad):
        super().__init__(idPersona, nombre, email, telefono, contraseña)
        self.puntosFidelidad = puntosFidelidad
        self.historialReserva = []

    def crearReserva(self, reserva_obj):
        #revisar asiento ocupado
        if reserva_obj.funcion.reservarAsientos(reserva_obj.asientos):
            self.historialReserva.append(reserva_obj)
            self.puntosFidelidad += 10 
            print(f"Reserva #{reserva_obj.idReserva} creada exitosamente.")
        else:
            print(f"Error: No se pudo crear la reserva #{reserva_obj.idReserva} porque los asientos están ocupados.")

    def consultarPromociones(self, lista_promociones):
        print(f"--- Promociones para {self.nombre} ---")
        for promo in lista_promociones:
            print(f"Código: {promo.codigo} - {promo.descripcion}")

    def cancelarReserva(self, idReserva):
        for res in self.historialReserva:
            if res.idReserva == idReserva:
                res.estado = "CANCELADA"
                print(f"La reserva {idReserva} ha sido cancelada.")
                return
        print("Reserva no encontrada.")
    

class empleado(persona):
    def __init__(self, idPersona, nombre, email, telefono, contraseña, idEmpleado, rol, horario):
        super().__init__(idPersona, nombre, email, telefono, contraseña)
        self.idEmpleado = idEmpleado
        self.rol = rol
        self.horario = horario

    def marcarEntrada(self):
        print(f"{self.nombre} ha entrado")

    def gestionarFunciones(self):
        if self.rol == Rol.ADMIN:
            print("Gestionando funciones")
        else:
            print("No tiene permisos")

    def agregarPelicula(self, catalogo_peliculas, nueva_peli):
        if self.rol == Rol.ADMIN:
            catalogo_peliculas.append(nueva_peli)
            print(f"Pelicula '{nueva_peli.titulo}'")
        else:
            print("Error: Solo los administradores pueden agregar películas.")

    def agregarFuncion(self, cartelera, nueva_funcion):
        if self.rol == Rol.ADMIN:
            cartelera.append(nueva_funcion)
            print(f"La función con ID {nueva_funcion.idFuncion} ha sido programada")
        else:
            print("Acceso denegado: No eres administrador")

    def agregarPromocion(self, lista_promos, nueva_promo):
        
        if self.rol == Rol.ADMIN:
            lista_promos.append(nueva_promo)
            print(f"Promoción '{nueva_promo.codigo}' activada.")
        else:
            print("Operación cancelada: Requiere rol de Administrador.")

class espacio():
    def __init__(self,idEspacio, nombreEspacio, ubicacion):
        self.idEspacio=idEspacio
        self.nombreEspacio=nombreEspacio
        self.ubicacion=ubicacion
        self.estaDisponible = True

        #la verificación de disponibilidad en esta clase se refiere a que si el lugar en general esta dsponible, por ejemplo, sino hay alguna función a x hora
        #la verificación de disponibilidad en la clase asiento se enfoca en un asiento en específico
    def limpiarEspacio(self):
        print(f"{self.nombreEspacio} ha sido limpiado")
    
    def verificarDisponibilidad(self):
        return True #las clases hijas van a sobreescribir

class sala(espacio):
    def __init__(self, idEspacio, nombreEspacio, ubicacion, tipoSala: TipoSala, capacidadTotal, esVip):
        super().__init__(idEspacio, nombreEspacio, ubicacion)
        self.tipoSala = tipoSala
        self.capacidadTotal = capacidadTotal
        self.esVip = esVip
        self.funciones = []  # lista de objetos Funcion

    def ajustarAforo(self):
        print(f"Ingresar la nueva capacidad de la sala {self.idEspacio}")
        entrada = input(":")

        # se uso isdigit para asegurar que es un entero
        if entrada.isdigit():
            self.capacidadTotal = int(entrada)
            print(f"Capacidad actualizada a: {self.capacidadTotal}")
        else:
            print("Ingresar un número válido")


    def obtenerTipoDeSala(self):
        print(f"Tipo de sala: {self.tipoSala}")
        return self.tipoSala
        

    # verifica si la sala está disponible en un horario dado
    def estaDisponible(self, horario):
        for funcion in self.funciones:
            if funcion.horarioInicio == horario:
                return False
        return True

    def agregarFuncion(self, funcion):
        if self.estaDisponible(funcion.horarioInicio):
            self.funciones.append(funcion)
            print(f"Función de {funcion.pelicula.titulo} agregada a {self.nombreEspacio} a las {funcion.horarioInicio}")
        else:
            print(f"La sala no está disponible a las {funcion.horarioInicio}")

    def listarFunciones(self):
        if not self.funciones:
            print(f"No hay funciones en {self.nombreEspacio}")
        for f in self.funciones:
            print(f"- {f.pelicula.titulo} a las {f.horarioInicio}, precio: ${f.precioBase}")


class zonaComida(espacio):
    def __init__(self, idEspacio, nombreEspacio, ubicacion, productos, stock):
        super().__init__(idEspacio, nombreEspacio, ubicacion)
        self.listaProductos = productos
        self.stockActual = stock

    def venderProducto(self):
        print("\n--- Menú de ventas ---")
        for i, producto in enumerate(self.listaProductos):
            print(f"{i + 1}. {producto} (Stock: {self.stockActual[producto]})")

        eleccion = input("¿Qué producto desea vender? (Introduzca el número): ")
        if not eleccion.isdigit():
            print("Opción inválida")
            return

        eleccion = int(eleccion) - 1

        if eleccion < 0 or eleccion >= len(self.listaProductos):
            print("Opción inválida")
            return

        producto_elegido = self.listaProductos[eleccion]

        cantidad_input = input(f"¿Cuántos {producto_elegido} quiere el cliente?: ")
        if not cantidad_input.isdigit():
            print("Cantidad inválida")
            return

        cantidad = int(cantidad_input)
        if cantidad <= 0:
            print("Cantidad inválida")
            return

        if self.stockActual[producto_elegido] >= cantidad:
            self.stockActual[producto_elegido] -= cantidad #aquí se restan los productos comprados del stock
            print(f"Venta exitosa. Quedan {self.stockActual[producto_elegido]}.")
        else:
            print("No hay suficiente en stock")

    def actualizarInventario(self):
        print("\n--- actualizar stock ---")
        producto = input("Nombre del producto a surtir: ")
        cantidad_input = input("Cantidad que llegó: ")
        
        if not cantidad_input.isdigit():
            print("La cantidad debe ser un número ")
            return
            
        cantidad = int(cantidad_input)
        if cantidad <= 0:
            print("Cantidad inválida")
            return
        
        if producto in self.stockActual:
            self.stockActual[producto] += cantidad
        else:
            self.listaProductos.append(producto)
            self.stockActual[producto] = cantidad
        print(f"Inventario actualizado: {producto} ahora tiene {self.stockActual[producto]} unidades.")

class pelicula():
    def __init__(self,titulo,duracion,clasificacion,genero,sinopsis):
        self.titulo=titulo
        self.duracion=duracion
        self.clasificacion=clasificacion #Intrducir solo AA, A, B, B15 o C
        self.genero=genero
        self.sinopsis=sinopsis

    def obtenerSinopsis(self):
        if self.sinopsis:
            print(
                f"Titulo: {self.titulo} Duración: {self.duracion} "
                f"Genero: {self.genero} Sinopsis: {self.sinopsis}"
            )
            return self.sinopsis
        else:
            return "Sinopsis no disponible."
    def esAptaTodoPublico(self):
        if self.clasificacion == "A":
            return "Apta para todo público"
        else:
            return "No es apta para todo público"

class promocion():
    def __init__(self, codigo, descripcion, porcentajeDescuento, fechaExpiracion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.porcentajeDescuento = porcentajeDescuento  # 0.2 - 20%
        self.fechaExpiracion = fechaExpiracion  # YYYY-MM-DD

    def esValida(self, fecha_actual):
        if fecha_actual <= self.fechaExpiracion:
            print(f"Promoción {self.codigo} válida")
            return True
        else:
            print(f"Promoción {self.codigo} caducada")
            return False

    def aplicarDescuento(self, monto, fecha_actual):
        if self.esValida(fecha_actual):
            descuento = monto * self.porcentajeDescuento
            total = monto - descuento
            print(f"Descuento aplicado! Ahorraste: ${descuento:.2f}")
            return total
        else:
            print("No se puede aplicar descuento")
            return monto


class reserva():
    def __init__(self, idReserva, usuario, funcion, asientos, montoTotal):
        self.idReserva = idReserva
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos
        self.montoTotal = montoTotal
        self.estado = "PENDIENTE"

    def confirmarPago(self):
        self.estado = "PAGADA"
        print(f"Pago verificado para la reserva #{self.idReserva}. ¡Disfruta la peli!")

    def aplicarPromocion(self, promo, fecha_hoy):
        nuevo_total = promo.aplicarDescuento(self.montoTotal, fecha_hoy)
        self.montoTotal = nuevo_total

    def generarTicket(self):
        print("\n" + "==============================")
        print("      TICKET DE ENTRADA")
        print("===============================")
        print(f"Reserva: {self.idReserva} | Estado: {self.estado}")
        print(f"Cliente: {self.usuario.nombre}")
        print(f"Película: {self.funcion.pelicula.titulo}")
        print(f"Sala: {self.funcion.sala.nombreEspacio} ({self.funcion.sala.tipoSala})")
        print(f"Asientos: {', '.join(self.asientos)}")
        print(f"Total Pagado: ${self.montoTotal:.2f}")
        print("===============================" + "\n")


class funcion():
    def __init__(self, idFuncion, pelicula, sala, horarioInicio, precioBase):
        self.idFuncion = idFuncion
        self.pelicula = pelicula
        self.sala = sala
        self.horarioInicio = horarioInicio
        self.precioBase = precioBase
        self.asientosOcupados = []  # lista de strings o números

    def asientosLibres(self):
        return self.sala.capacidadTotal - len(self.asientosOcupados)

    def reservarAsientos(self, listaAsientos):
        if len(listaAsientos) > self.asientosLibres():
            print("No hay suficiente espacio en la sala.")
            return False
        # que asientos no están ocupados
        for asiento in listaAsientos:
            if asiento in self.asientosOcupados:
                print(f"El asiento {asiento} ya está ocupado")
                return False
        self.asientosOcupados.extend(listaAsientos)
        print(f"Asientos {listaAsientos} reservados")
        return True
    

    