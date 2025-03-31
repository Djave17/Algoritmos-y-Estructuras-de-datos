"4. Diseñe un programa que lea un número de tres cifras y determine si es igual al revés del número."

import os 
def numero_reves(numero):
    # Convertir el número a cadena para invertirlo
    numero_str = str(numero)
    # Invertir la cadena
    numero_reves = numero_str[::-1]
    # Comparar el número original con el invertido
    return numero_str == numero_reves

# Función principal
#Menu 
opcion = 0
while opcion != 2:
    print("========== Menú de opciones ==========")
    print("1. Ingresar número")
    print("2. Salir")
    print("======================================")
    opcion = int(input("Ingrese la opción: "))
    os.system("clear")
    if opcion == 1:
        numero = int(input("Ingrese un número de tres cifras: "))
        if 100 <= numero <= 999:
            if numero_reves(numero):
                print(f"El número {numero} es igual al revés.")
            else:
                print(f"El número {numero} no es igual al revés.")
        else:
            print("El número debe ser de tres cifras.")
    elif opcion == 2:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Intente nuevamente.")
    input("Presione Enter para continuar...")
    os.system("clear")
