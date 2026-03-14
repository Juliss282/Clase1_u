from enum import Enum
from enum import Enum

class Puesto(Enum):
    BARISTA = 1
    MESERO = 2
    GERENTE = 3

class EstadoPedido(Enum):
    PENDIENTE = 1
    PREPARANDO = 2
    ENTREGADO = 3

from enum import Enum

class Temperatura(Enum):
    FRIA = "Fría"
    CALIENTE = "Caliente"
    


class Persona():
    def __init__(self, idPersona, nombre, email, contraseña):
        self.idPersona=idPersona
        self.nombre=nombre
        self.email=email
        self.contraseña=contraseña
        self.sesionActiva=False

    def login(self, idPersonaIngresado, contraseñaIngresada):
        if idPersonaIngresado == self.idPersona and contraseñaIngresada == self.contraseña:
            self.sesionActiva = True
            return True
        return False
    
    def logout(self):
        self.sesionActiva = False
        print(f"{self.nombre} cerró sesión")
    
    def actualizarPerfil(self, nombre=None, email=None):
        print("Actualizando perfil...")

        if nombre is not None:
            self.nombre = nombre
        if email is not None:
            self.email = email

        print(f"Perfil actualizado -> Id: {self.idPersona} Nombre: {self.nombre}, Email: {self.email}")
    
    def mostrarDetalle(self):
            print (f"El Cliente {self.idPersona}, de nombre  {self.nombre}, cuyo email es: {self.email}")

class Cliente (Persona):
    def __init__ (self, idPersona, nombre, email, contraseña, puntosFidelidad):
        super().__init__(idPersona, nombre, email, contraseña)
        self.puntosFidelidad=puntosFidelidad
        self.historialPedidos=[]

    def realizarPedido(self, pedido: 'Pedido', puntosACanjear): #'Pedido' se refiere a un objeto de Pedido
        total = pedido.calcularTotal(puntosACanjear)
        self.puntosFidelidad = max(0, self.puntosFidelidad - puntosACanjear)  
        self.historialPedidos.append(pedido)
        self.puntosFidelidad += int(total * 0.1)
        print(f"{self.nombre} realizó pedido #{pedido.idPedido}. Total: ${total:.2f}. Puntos actuales: {self.puntosFidelidad}")

    def consultarHistorial(self):
        if not self.historialPedidos:
            print(f"{self.nombre} no tiene pedidos en su historial.")
            return
        print(f"Historial de pedidos de {self.nombre}:")
        for pedido in self.historialPedidos:
            productos = ', '.join([p.nombreProducto for p in pedido.productos])
            print(f"Pedido #{pedido.idPedido}: {productos} - Total de $ en pedidos: ${pedido.total:.2f}")

    def mostrarDetalle(self):
        print (f"el usuario {self.idPersona}, de nombre  {self.nombre}. Puntos actuales: {self.puntosFidelidad}")


class Empleado(Persona):
    def __init__(self, idPersona, nombre, email, contraseña, idEmpleado, rol):
        super().__init__(idPersona, nombre, email, contraseña)
        self.idEmpleado=idEmpleado
        self.rol=rol

    def actualizarInventario(self, Inventario, nombreIngrediente: str, cantidad: int):
        if self.rol in [Puesto.GERENTE, Puesto.BARISTA]:
            Inventario.agregarIngrediente(nombreIngrediente, cantidad)
            print(f"{self.nombre} actualizó el inventario: {nombreIngrediente} + {cantidad}")
        else:
            print(f"{self.nombre} no tiene permiso para actualizar inventario.")

    def cambiarEstadoPedido(self, pedido, nuevoEstado):
        if nuevoEstado in [EstadoPedido.PREPARANDO, EstadoPedido.ENTREGADO]:
            pedido.estado = nuevoEstado
            print(f"{self.nombre} cambió el estado del pedido {pedido.idPedido} a {pedido.estado.name}")
        else:
            print(f"{self.nombre} no puede asignar el estado {nuevoEstado}")
    
    def mostrarDetalle(self):
        print (f"el empleado {self.idPersona}, de nombre  {self.nombre}, tiene email {self.email}, es {self.rol.name} con id {self.idEmpleado}")

#Modelado de productos
class ProductoBase():
    def __init__(self, idProducto, nombreProducto, precioBase, stock):
        self.idProducto=idProducto
        self.nombreProducto=nombreProducto
        self.precioBase=precioBase
        self.stock = stock

    def calcular_precio_final(self):
        return self.precioBase

class Extra:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Bebida(ProductoBase):
    def __init__(self, idProducto, nombreProducto, precioBase, stock, tamaño, temperatura):
        super().__init__(idProducto, nombreProducto, precioBase, stock)
        self.tamaño=tamaño
        self.temperatura=temperatura
        self.modificadores=[]
        self.extras = []

    def agregar_extra(self, extra):
        self.extras.append(extra)

    def calcular_precio_final(self):
        total = self.precioBase

        for extra in self.extras:
            total += extra.precio
        return total

class Topping:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Postre(ProductoBase):
    def __init__(self, idProducto, nombreProducto, precioBase, stock):
        super().__init__(idProducto, nombreProducto, precioBase, stock)
        self.esVegano=False
        self.sinGluten=False
        self.toppings=[]

    def agregarTopping(self, topping):
        self.toppings.append(topping)
    
    def calcular_precio_final(self):
        total = self.precioBase

        for topping in self.toppings:
            total += topping.precio
        return total

class Pedido():
    def __init__(self, idPedido, productos: list[ProductoBase], estado=None, total=0.0):
        self.idPedido = idPedido
        self.productos = productos
        self.estado = estado if estado else EstadoPedido.PENDIENTE
        self.total = total
        self.inventario = None
    
    def calcularTotal(self, puntosCanjeados):
        self.total = sum(producto.calcular_precio_final() for producto in self.productos)
        if puntosCanjeados > 0:
            self.total = max(0, self.total - puntosCanjeados)
        return self.total

    def validarStock(self):
        stock_detalle = {}
        for producto in self.productos:
            disponible = self.inventario.validarStockProducto(producto)
            stock_detalle[producto.nombreProducto] = "Disponible" if disponible else "Agotado"
        return stock_detalle
    
    def procesarPedido(self):
        stock = self.validarStock()

        for nombre, estado in stock.items():
            if estado == "Agotado":
                print(f"No se puede procesar el pedido. Falta {nombre}")
                return

        for producto in self.productos:
            self.inventario.reducirStock(producto.nombreProducto,1)

        self.estado = EstadoPedido.PREPARANDO

class Inventario:
    def __init__(self):
        self.ingredientes = {}

    def agregarIngrediente(self, nombre: str, cantidad: int):
        if nombre in self.ingredientes:
            self.ingredientes[nombre] += cantidad
        else:
            self.ingredientes[nombre] = cantidad

    def reducirStock(self, nombre: str, cantidad: int):
        if nombre in self.ingredientes:
            if self.ingredientes[nombre] >= cantidad:
                self.ingredientes[nombre] -= cantidad
            else:
                self.ingredientes[nombre] = 0
                self.notificarFaltante(nombre)
        else:
                self.notificarFaltante(nombre)

    def notificarFaltante(self, nombre: str):
        print(f"¡Atención! Se ha agotado el ingrediente: {nombre}")

    def validarStockProducto(self, producto):
        return self.ingredientes.get(producto.nombreProducto, 0) > 0

    def mostrarInventario(self):
        return self.ingredientes
    


