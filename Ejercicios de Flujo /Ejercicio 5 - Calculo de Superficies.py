"""Se desea escribir un programa para el cálculo del área de diversas superficies: cuadrado, rectángulo,
círculo, triángulo y trapecio

Seguidamente leerá de la entrada estándar un valor que estará comprendido entre 1 y 5, indicando el tipo de 
superficie cuya área se desea calcular.  El programa leerá entonces los datos que necesite para calcular el 
área en cuestión.  El resultado se mostrará en la salida estándar, tras lo cual el programa terminará.
"""

import os 
import math

def area_cuadrado(lado):
    return pow(lado, 2)
def area_rectangulo(base, altura):
    return base * altura
def area_circulo(radio):
    return round(math.pi * pow(radio, 2))
def area_triangulo(base, altura):
    return (base * altura) / 2
def area_trapecio(base_menor, base_mayor, altura):
    return round(((base_menor + base_mayor) * altura) / 2)

# Función principal
#Menu
opcion = 0
while opcion != 6:
    os.system("clear")
    print("========== Menú de opciones ==========")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Círculo")
    print("4. Triángulo")
    print("5. Trapecio")
    print("6. Salir")
    print("======================================")

    opcion = int(input("Ingrese la opción: "))
    
    match opcion:
        case 1:
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = area_cuadrado(lado)
            print(f"Área del cuadrado: {area}")
        case 2:
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = area_rectangulo(base, altura)
            print("Área del rectángulo: ", area)
        case 3:
            radio = float(input("Ingrese el radio del círculo: "))
            area = area_circulo(radio)
            print(f"Área del círculo: {area}")
        case 4:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = area_triangulo(base, altura)
            print(f"Área del triángulo: {area}")
        case 5:
            base_menor = float(input("Ingrese la base menor del trapecio: "))
            base_mayor = float(input("Ingrese la base mayor del trapecio: "))
            altura = float(input("Ingrese la altura del trapecio: "))
            area = area_trapecio(base_menor, base_mayor, altura)
            print(f"Área del trapecio: {area}")
        case 6:
            print("Saliendo del programa...")
        case _:
            print("Opción no válida. Intente nuevamente.")
    
    input("Presione Enter para continuar...")