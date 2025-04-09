def decimalABinario(num):
    if num == 0:
        return ""
    else:
        return decimalABinario(num // 2) + str(num % 2)
    
num = int(input("Ingrese un numero: "))
print(decimalABinario(num))

"""
Llamada inicial: decimal_to_binary(5)
    num = 5, no es 0, así que entra al caso recursivo.

    Calcula decimal_to_binary(5 // 2) → decimal_to_binary(2) (porque 5 ÷ 2 = 2, división entera).

    Luego, concatena con str(5 % 2) → "1" (porque 5 mod 2 = 1).
    
Segunda llamada: decimal_to_binary(2)
    num = 2, no es 0.
    Calcula decimal_to_binary(2 // 2) → decimal_to_binary(1) (porque 2 ÷ 2 = 1).
    Concatena con str(2 % 2) → "0" (porque 2 mod 2 = 0).
    
Tercera llamada: decimal_to_binary(1)
    num = 1, no es 0.
    Calcula decimal_to_binary(1 // 2) → decimal_to_binary(0) (porque 1 ÷ 2 = 0).
    Concatena con str(1 % 2) → "1" (porque 1 mod 2 = 1).
    
Cuarta llamada: decimal_to_binary(0)
    num = 0, condición base.
    Devuelve "" (cadena vacía).
    
Por ejemplo, para 5:

5 ÷ 2 = 2, resto 1 → bit menos significativo.
2 ÷ 2 = 1, resto 0.
1 ÷ 2 = 0, resto 1 → bit más significativo.
Al concatenar en orden: "101".
"""

