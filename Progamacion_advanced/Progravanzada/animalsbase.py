class Animales:
    def __init__(self, nombre, color, nopatas):
        self.nombre=nombre
        self.color=color
        self.nopatas=nopatas
    def sonido(self):
        print("Sonido genérico")

class Conejo(Animales):
    def sonidoc(self):
        print("snif snif")

    def caracteristicas(self):
        print(f"Mi conejo se llama {self.nombre}, es de color {self.color} y tiene {self.nopatas}")

class Ornitorrinco(Animales):
    def __init__ (self, nombre, color, nopata, tamañopico):
        super().__init__(nombre, color, nopata)
        self.tamañopico=tamañopico
    def sonidoo(self):
        print ("ggrrr")
    def caracteristicas(self):
        print(f"Mi ornitorrinco se llama {self.nombre}, es de color {self.color}, tiene {self.nopatas} y su pico mide {self.tamañopico}")

class Dinosaurio(Animales):
    def __init__ (self, nombre, color, nopatas, tipo):
        super().__init__(nombre, color, nopatas)
        self.tipo=tipo
    def sonidino(self):
        print("Grr")
    def caracteristicas(self):
        print(f"Mi dino se llama nombre, es color {self.color}, tiene {self.nopatas} y es un {self.tipo}")