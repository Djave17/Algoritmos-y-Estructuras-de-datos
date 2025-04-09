lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = numero + suma_pares
print(f"Suma pares:{suma_pares} ")
for numero in lista_numeros:
    if numero % 2 == 1:
        suma_impares = numero + suma_impares
print(f"Suma impares: {suma_impares}")


for i in range (0, 101, 2):
    if i % 2 == 0:
        suma_pares = i + suma_pares
    print(i)
print(f"Suma pares:{suma_pares} ")