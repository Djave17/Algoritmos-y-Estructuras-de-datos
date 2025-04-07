"""Clases:  Realizar un programa que conste de una Clase Estudiante que contenga los siguientes atributos:ue tenga
como atributos el nombre y la nota del estudiante. Definir un metodo, imprimir sus atributos y otro metodo que
que muestre el resultade de si el estudiante aprueba o reprueba. """

import os
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota 
        
    def imprimir_atributos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")
    def resultado(self):
        if self.nota >= 70:
            print(f"El estudiante {self.nombre} aprueba.")
        else:
            print(f"El estudiante {self.nombre}reprueba.")
#Fin de la clase

#Función principal
#Menu
opcion = 0
while opcion != 2:
    os.system("clear")
    print("========== Menú de opciones ==========")
    print("1. Ingresar estudiante")
    print("2. Salir")
    print("======================================")
    opcion = int(input("Ingrese la opción: "))
    
    if opcion == 1:
        os.system("clear")
        print("Ingreso de estudiante") 
        nombre = input("Ingrese el nombre del estudiante: ")
        nota = float(input("Ingrese la nota del estudiante: "))
        estudiante = Estudiante(nombre, nota)
        estudiante.imprimir_atributos()
        estudiante.resultado()
        input("Presione Enter para continuar...")
    elif opcion == 2:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Intente nuevamente.")