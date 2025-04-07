#Ejemplificación de clases en Python
#Ejemplo de clase
import os
import Modulo

#Ejemplo de uso de la clase

option= 0 
while option != 3: 
   
    print("======Menú de ejemplo de clases======")
    print("1. Clase de Persona")
    print("2. Clase de Carro")
    print("3. Salir")
    option = int(input("Opción: "))
    
    match option: 
        case 1: 
            print("======================================")
            print("Ejemplo de uso de la clase Persona")
            NombrePersona = input("Ingrese el nombre: ")
            EdadPersona = input("Edad: ")
            persona = Modulo.Persona(NombrePersona, EdadPersona)
            persona.saludar()
            input()
        case 2: 
            
            print("=======================================")
            print("Ejemplo de uso de la clase Carro")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            año = input("Año: ")
            carro = Modulo.Coche(marca, modelo, año)
            carro.mostrar_info()
            carro.manejar()
            input()
        case _:
            print("Opción no válida")
            input()
            continue
    
    
        
            
            
            
            
            
                        





