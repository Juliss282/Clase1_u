class producto():

    def __init__(self, name, price, stock):
        self.nombre = name
        self.precio_base = price
        self.stock = stock
    
    def aplicar_descuento(self, porcentaje):
        descuento = self.precio_base * (porcentaje / 100)
        self.precio_base -= descuento

    def actualizar_stock(self, cantidad):
        if (self.stock + cantidad) < 0:
            print("No hay suficiente stock")
        else:
            self.stock += cantidad
            print(f"El nuevo stock de {self.nombre} es {self.stock}")


class categoria():

    def __init__(self, nombre_categoria):
        self.nombre_categoria = nombre_categoria
        self.lista_comprados = []
    
    def agregar_producto(self, producto):
        self.lista_comprados.append(producto)
        print(f"El producto {producto.nombre} se agrego a la lista")

    def valor_total_categoria(self):
        suma = 0
        for m in self.lista_comprados:
            suma += m.precio_base * m.stock
        print(f"El precio total de la categoria {self.nombre_categoria} es {suma} pesos")
        

class pedido:

    def __init__(self, cliente):
        self.cliente = cliente
        self.lista_comprados = []
        self.estado = "Pendiente"

    def agregar_producto(self, producto):
        self.lista_comprados.append(producto)
        print(f"El producto {producto.nombre} se agrego a la lista")
        
    def calcular_total(self):
        subtotal = 0
        for producto in self.lista_comprados:
            subtotal += producto.precio_base

        iva = subtotal * 0.16
        total = subtotal + iva
        return total

    def finalizar_pedido(self, listab):
        for x in self.lista_comprados:
            for y in listab:
                if x.nombre == y.nombre:
                    if y.stock > 0:
                        y.stock -= 1
                        print(f"Al producto {y.nombre} se le quito un elemento")
                    else:
                        print(f"No hay stock suficiente de {y.nombre}")
        self.estado = "Completado"
