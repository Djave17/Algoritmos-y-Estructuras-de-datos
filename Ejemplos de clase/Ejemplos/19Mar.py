print("HOLA MUNDO")

x = 10 
y = 20
suma = x + y 
print(suma)
print("--" *20)
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
    
    
print("Hola, mucho gusto")
nombre = input("¿Cuál es tu nombre? ")
print(f"Mucho gusto, {nombre}")
edad = int(input("¿Cuántos años tienes? "))
print(f"Vaya, {nombre}, no pareces de {edad} años")
print(nombre, edad,sep=", ")
precio = float(input("¿Cuánto cuesta el producto? "))
print(f"El precio del producto es ${precio:.2f}")
cantidad = int(input("¿Cuántos productos quieres? "))
