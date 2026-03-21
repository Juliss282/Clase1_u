from datetime import datetime, timedelta
class Material():
    def __init__(self, id_material, titulo, año_publicacion, autor):
        self.id_material = id_material
        self.titulo = titulo
        self.año_publicacion = año_publicacion
        self.autor=autor
        self.disponible = True

class Libro(Material):
    def __init__(self, id_material, titulo, año_publicacion, autor, isbn, genero):
        super().__init__(id_material, titulo, año_publicacion, autor)
        self.isbn = isbn
        self.genero =  genero

class MaterialDigital(Material):
    def __init__(self, id_material, titulo, año_publicacion, autor, tipo_archivo, url_descarga, tamaño_mb):
        super().__init__(id_material, titulo, año_publicacion, autor)
        self.tipo_archivo=tipo_archivo
        self.url_descarga=url_descarga
        self.tamaño_mb=tamaño_mb

class Revista(Material):
    def __init__(self, id_material, titulo, año_publicacion, autor, edicion, periodicidad):
        super().__init__(id_material, titulo, año_publicacion, autor)
        self.edicion = edicion
        self.periodicidad = periodicidad

class Prestamo:
    def __init__(self, id_prestamo, usuario, material, dias_prestamo=7):
        self.id_prestamo = id_prestamo
        self.usuario = usuario
        self.material = material
        self.fecha_inicio = datetime.now()
        self.fecha_limite = self.fecha_inicio + timedelta(days=dias_prestamo)
        self.fecha_devolucion = None
        self.activo = True

    def devolver(self):
        self.fecha_devolucion = datetime.now()
        self.activo = False
        self.material.disponible = True

    def esta_atrasado(self):
        if self.activo and datetime.now() > self.fecha_limite:
            return True
        return False

class Sucursal():
    def __init__(self, id_sucursal, nombre):
        self.id_sucursal=id_sucursal
        self.nombre=nombre
        self.catalogo_local=[]


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

class Usuario(Persona):
    def __init__(self, idPersona, nombre, email, contraseña):
        super().__init__(idPersona, nombre, email, contraseña)
        self.prestamos = []

    def listar_prestamos(self):
        if not self.prestamos:
            print(f"{self.nombre} no tiene préstamos.")
        else:
            print(f"Préstamos de {self.nombre}:")
            for prestamo in self.prestamos:
                estado = "Activo" if prestamo.activo else "Devuelto"
                print(f"- {prestamo.material.titulo} ({estado})")

    def devolver_libro(self, prestamo, sucursal):
        if prestamo in self.prestamos and prestamo.activo:
            prestamo.devolver()
            if prestamo.material not in sucursal.catalogo_local:
                sucursal.catalogo_local.append(prestamo.material)
            print(f"'{prestamo.material.titulo}' ha regresado a la sucursal {sucursal.nombre}")
        else:
            print("Este préstamo no es válido o ya fue devuelto.")


class Bibliotecario(Persona):
    def __init__(self, idPersona, nombre, email, contraseña):
        super().__init__(idPersona, nombre, email, contraseña)

    def gestionar_prestamo(self, libro, usuario, sucursal):
        if libro in sucursal.catalogo_local and libro.disponible:
            
            prestamo = Prestamo(
                id_prestamo=len(usuario.prestamos)+1,
                usuario=usuario,
                material=libro
            )

            usuario.prestamos.append(prestamo)
            sucursal.catalogo_local.remove(libro)
            libro.disponible = False

            print(f"Préstamo realizado: {libro.titulo} a {usuario.nombre}")
        else:
            print("El libro no está disponible")

    def transferir_material(self, libro, sucursal_origen, sucursal_destino):
        if libro in sucursal_origen.catalogo_local:
            sucursal_origen.catalogo_local.remove(libro)
            sucursal_destino.catalogo_local.append(libro)
            print(f"Libro '{libro.titulo}' transferido de {sucursal_origen.nombre} a {sucursal_destino.nombre}")
        else:
            print("El libro no está disponible en la sucursal de origen.")

    def mostrarDetalle(self):
        print (f"El Bibliotecario {self.idPersona}, de nombre  {self.nombre}, cuyo email es: {self.email}")

class Penalizacion:
    def __init__(self, usuario, monto=0, motivo=""):
        self.usuario = usuario
        self.monto = monto
        self.motivo = motivo
        self.pagada = False

    def calcular_multa(self, prestamo, multa_por_dia=5):
        if prestamo.esta_atrasado():
            dias_atraso = (datetime.now() - prestamo.fecha_limite).days
            self.monto = dias_atraso * multa_por_dia
            self.motivo = f"Retraso de {dias_atraso} días"
        else:
            self.monto = 0
            self.motivo = "Sin retraso"

        return self.monto

    def bloquear_usuario(self):
        if self.monto > 0 and not self.pagada:
            print(f"Usuario {self.usuario.nombre} bloqueado hasta pagar multa de ${self.monto}")
        else:
            print(f"Usuario {self.usuario.nombre} no tiene bloqueos.")


class Catalogo:
    def __init__(self, sucursales):
        self.sucursales = sucursales

    def buscar_por_autor(self, autor):
        resultados = []
        for sucursal in self.sucursales:
            for libro in sucursal.catalogo_local:
                if libro.autor.lower() == autor.lower():
                    resultados.append((libro, sucursal.nombre))
        return resultados

    def buscar_en_todas_sucursales(self, titulo):
        resultados = []
        for sucursal in self.sucursales:
            for libro in sucursal.catalogo_local:
                if libro.titulo.lower() == titulo.lower():
                    resultados.append((libro, sucursal.nombre))
        return resultados