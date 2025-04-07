#Funcion que permita obtener el producto de dos numeros

def producto(a, b):
    return a * b

#Ingreso de datos
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultado = producto(num1, num2)
print(f"El producto de {num1} * {num2} es: {resultado}")
print("=========================================")

#Obtener la tabla de multiplicar
num = int(input("Ingrese el número para obtener su tabla de multiplicar: "))
for i in range(1, 13):
    resultado = producto(num, i)
    print(f"{num} * {i} = {resultado}")
print("=========================================")