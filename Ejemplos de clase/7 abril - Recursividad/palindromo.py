def es_palindromo(cadena):
    # caso base: cadena vacía o un solo carácter
    if len(cadena) <= 1:
        return True

    # comparar extremos
    if cadena[0] != cadena[-1]:
        return False

    # llamada recursiva eliminando extremos
    return es_palindromo(cadena[1:-1])

# ejemplos de uso:
print(es_palindromo("anitalavalatina"))  # True
print(es_palindromo("hola"))            # False

cadena = input("Ingrese una cadena: ")
print(f"La cadena '{cadena}' es un palíndromo: {es_palindromo(cadena)}")


""""
Primera llamada:
    cadena = "radar"
    cadena[0] == "r", cadena[-1] == "r" → Son iguales.
    Llamada recursiva con "ada".
    
Segunda llamada:

    cadena = "ada"
    cadena[0] == "a", cadena[-1] == "a" → Son iguales.
    Llamada recursiva con "d".
Tercera llamada:

    cadena = "d"
    Longitud de la cadena es 1 → Caso base, retorna True.

Resultado:

    Todas las llamadas recursivas retornan True, por lo que "radar" es un palíndromo.
"""