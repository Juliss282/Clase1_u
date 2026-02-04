from Atributoss import *

per1=Nombre("Bernardo", 18, "Ciencia de la compu")
per2=Nombre("Mich", 18, "Ciencia de la compu")
per3=Nombre("Lupita", 18, "Ciencia de datos")

print(str(per1))
print(repr(per2))

print(per1+per2) # def __add__(self,otra): dice que hacer cuando se suma uno mas otro, en este caso genera un enunciado
print(per2*per3) #Multiplica las edades, definido con    def __mul__(self,otra):
print(per1==per2) #Compara las carreras, al ser iguales regresa el boleano True    def __eq__(self,otra):
print(per1==per3)