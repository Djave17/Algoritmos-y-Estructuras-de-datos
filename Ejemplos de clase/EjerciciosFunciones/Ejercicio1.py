#Introducir un valor entero impar comprendido entre 1 y 19 
#A partir de este numero calcular la serie numerica de 1 + 3 + 5 + ... + n
#Calcular 1 * 2 * 3 * ... * n
#Salir del programa
import os 
import math
def suma_impares(n):
    suma = 0
    for i in range(1, n + 1, 2):
        suma += i
    return suma
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
op = 0
while op != 2:
    print("=========================================")
    print("Ejercicio 1 - Suma de impares y factorial")
    print("1. Ingresar número")
    print("2. Salir")
    print("=========================================")
    op = int(input("Ingrese la opción: "))
    if op == 1:
        n = int(input("Ingrese un número impar entre 1 y 19: "))
        if n % 2 != 0 and 1 <= n <= 19:
            suma = suma_impares(n)
            fact = factorial(n)
            print(f"Suma de impares hasta {n}: {suma}")
            print(f"Factorial de {n}: {fact}")
        else:
            print("Número inválido. Debe ser impar y entre 1 y 19.")
    elif op == 2:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Intente nuevamente.")
    input("Presione Enter para continuar...")
    os.system("clear")
# Fin del programa