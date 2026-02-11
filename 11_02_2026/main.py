from techstore import *

# Crear productos
p1 = producto("Mouse", 20, 5)
p2 = producto("Teclado", 45, 12)
p3 = producto("Monitor", 180, 8)
p4 = producto("Laptop", 850, 4)
p5 = producto("Auriculares", 35, 15)
p6 = producto("Cámara Web", 55, 10)
p7 = producto("Micrófono", 90, 6)
p8 = producto("Disco Duro", 120, 20)
p9 = producto("Memoria USB", 15, 50)
p10 = producto("Pad Mouse", 12, 30)
p11 = producto("Silla Gamer", 250, 3)
p12 = producto("Escritorio", 150, 5)
p13 = producto("Router Wi-Fi", 65, 14)
p14 = producto("Cable HDMI", 10, 40)
p15 = producto("Adaptador USB-C", 18, 25)


listaproductos = [
    p1, p2, p3, p4, p5, p6, p7, p8, p9, p10,
    p11, p12, p13, p14, p15
]

pedido1 = pedido("Sugey")
pedido1.agregar_producto(p10)
pedido1.agregar_producto(p8)
pedido1.agregar_producto(p6)
print("Productos en el pedido:")

pedido1.finalizar_pedido(listaproductos)
