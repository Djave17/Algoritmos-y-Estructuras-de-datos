
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
        
    #fin de la funcion 
#fin de la clase
class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        print(f"Coche: {self.marca} {self.modelo}, Año: {self.año}")
    
    def manejar(self): 
        print(f"El carro {self.marca} está corriendo a 80km por hora")

    