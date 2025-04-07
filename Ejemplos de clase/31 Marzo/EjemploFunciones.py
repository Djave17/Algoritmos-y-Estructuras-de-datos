#Ejemplificando el uso de funciones

def suma(a, b):
    return a + b

print("Ejemplo de función suma:")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultado = suma(num1, num2)
print(f"La suma de {num1} + {num2} es: {resultado}")
print("=========================================")

print("Ejemplo de función de mensaje:")
def mensaje():
    print("Hola, este es un mensaje de ejemplo.")
    print(f"La suma de {num1} + {num2} es: {resultado}")
mensaje()



# def resta(a, b):
#     return a - b
# print("Ejemplo de función resta:")
# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))
# resultado = resta(num1, num2)
# print(f"La resta de {num1} - {num2} es: {resultado}")
# print("=========================================")
# def multiplicacion(a, b):
#     return a * b
# print("Ejemplo de función multiplicación:")
# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))
# resultado = multiplicacion(num1, num2)
# print(f"La multiplicación de {num1} * {num2} es: {resultado}")
# print("=========================================")
# def division(a, b):
#     if b == 0:
#         return "Error: División por cero no permitida."
#     else:
#         return a / b
# print("Ejemplo de función división:")                
