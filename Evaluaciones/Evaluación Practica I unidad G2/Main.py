"""
David Joel Sánchez Acevedo
Algoritmos y Estructuras de Datos
Version: 1.0

"""
import Modulos as Mod

import os

# Lista de estudiantes
estudiantes = []
def seleccionar_estudiante():
    #Verifica si la lista estudiantes está vacía.
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return None

    #Menú de la lista de estudiantes
    #Se ocupa el indice para el "1."
    #enumerate da el índice (posición) de cada estudiante para numerarlos desde el 1.
    print("====== Lista de Estudiantes ======")
    for indice, estudiante in enumerate(estudiantes): 
        print(f"{indice + 1}. {estudiante.nombre}")
        print("==================================")

    #Entrada
    try:
        #Se usa seleccion - 1 porque las listas en Python comienzan desde 0.
        seleccion = int(input("Seleccione un estudiante (número): "))
        #Selección de estudiante
        if 1 <= seleccion <= len(estudiantes):
            return estudiantes[seleccion - 1]
        else:
            print("Selección inválida. Intente nuevamente.")
            return None
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return None

#Menu
option = 0 
while option != 5: 
    os.system("clear")
    print("====== Menú de Gestión de Estudiantes ======")
    print("1. Agregar información del estudiante")
    print("2. Agregar calificación")
    print("3. Mostrar información del estudiante")
    print("4. Calcular promedio de calificaciones")
    print("5. Salir")
    print("============================================")
    option = int(input("Opción: "))
        
    match option: 
        case 1: 
            os.system("clear")
            print("===== Agregar Información del Estudiante =====")
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            carrera = input("Carrera: ")
            #Clase
            estudiante = Mod.Estudiante(nombre, edad, carrera, [])
            #Se agrega la clase a la lista estudiantes (Importante)
            estudiantes.append(estudiante)
            print("Estudiante agregado exitosamente.")
            input("Presiona Enter para continuar...")

        case 2: 
            os.system("clear")
            print("===== Agregar Calificación =====")
            estudiante = seleccionar_estudiante()
            if estudiante:
                calificacion = float(input("Ingrese la calificación: "))
                estudiante.agregar_Calificacion(calificacion)
            input("Presiona Enter para continuar...")

        case 3: 
            os.system("clear")
            print("===== Mostrar Información =====")
            estudiante = seleccionar_estudiante()
            if estudiante:
                estudiante.mostrar_Info()
            input("Presiona Enter para continuar...")

        case 4:
            os.system("clear")
            print("===== Calcular Promedio =====")
            estudiante = seleccionar_estudiante()
            if estudiante:
                estudiante.calcular_Promedio()
            input("Presiona Enter para continuar...")

        case 5: 
            os.system("clear")
            print("Saliendo del programa...")
            input("Presiona Enter para salir.")

        case _:
            print("Opción no válida.")
            input("Presiona Enter para continuar.")
