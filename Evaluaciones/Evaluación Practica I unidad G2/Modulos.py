"""
David Joel Sánchez Acevedo
Algoritmos y Estructuras de Datos
CIF: 23020386
"""
#Modulo 
class Estudiante: 
    """
    nombre (str)
    edad (int)
    carrera (str)
    calificaciones (lista de floats)
    """
    def __init__(self, nombre, edad, carrera, calificaciones): 
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []
    
    def mostrar_Info(self):
        print("=======================================")
        print("Información del estudiante")
        print(f"Nombre: {self.nombre} \n Edad: {self.edad} \n Carrera: {self.carrera} \n Calificaciones: {self.calificaciones} ")
        #Si no hay calificaciones se printea "No hay calificaciones disponibles.""
        if (len(self.calificaciones) > 0):
            print(f"Promedio: {sum(self.calificaciones) / len(self.calificaciones):.2f}")
        else:
            print("No hay calificaciones disponibles.")
        print("=======================================")
        
    def agregar_Calificacion(self, calificacion):
        #Debe de ser entre 100 y 0 
        if calificacion > 100 or calificacion < 0:
            print("La calificación debe estar entre 0 y 100.")
            return
        self.calificaciones.append(calificacion)
        print(f"Calificación {calificacion} agregada.")
        
        
    def calcular_Promedio(self):
        #si no hay calificiones
        if len(self.calificaciones) == 0:
            print("No hay calificaciones para calcular el promedio.")
            return 
        promedio = sum(self.calificaciones) / len(self.calificaciones)
        print(f"El promedio de calificaciones es: {promedio:.2f}")
        return promedio 
    
    
        

       
                

        
        
       