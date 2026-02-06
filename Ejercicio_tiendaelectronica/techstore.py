class producto():

    def __init__ (self, name, price, stock):
        self.nombre=name
        self.precio_base=price
        self.stock=stock
    
    def aplicar_descuento(self, porcentaje):
        descuento = self.precio_base * (porcentaje / 100)
        self.precio_base -= descuento
        #self.precio*=(1-porcentaje)
        #print(f"El nuevo precio es{self.precio}")

    def actualizar_stock(self, cantidad):
        if (self.stock + cantidad)<0:
            print("No hay suficiente stock")
        else:
            self.stock += cantidad
            print(f"El nuevo stock es de {self.nombre} es {self.stock}")


class categoria():

    def __init__ (self, nombre_categoria):
        self.nombre_categoria=nombre_categoria
        self.lista_productos=[]
    
    def agregar_producto(self, producto):
        self.lista_productos.append(producto)
        print(f"El producto {producto.nombre} se agrego a la lista")

    def valor_total_categoria(self):
        suma=0
        for m in self.lista_productos:
            suma+=m.precio_base*m.stock
        print(f"el precio total de la categoria {self.nombre_categoria} es {suma} pesos")
        
class pedido:

    def __init__(self, cliente, productos_comprados):
        self.cliente = cliente
        self.productos_comprados = productos_comprados  # lista de objetos Producto
        self.estado = "Pendiente"
        
    def calcular_total(self):
        subtotal = 0
        for producto in self.productos_comprados:
            subtotal += producto.precio_base

        iva = subtotal * 0.16
        total = subtotal + iva
        return total

    def finalizar_pedido(self):
        self.estado = "Completado"

        for producto in self.productos_comprados:
            producto.actualizar_stock(-1)
   