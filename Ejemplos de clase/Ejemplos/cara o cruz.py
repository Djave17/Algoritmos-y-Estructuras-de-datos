
from random import choice


def lanzar_moneda():
    moneda = choice(["Cara", "Cruz"])
    return moneda


def probar_suerte(moneda, lista_numeros):
    if moneda == 'Cara':
        print("La lista se autodestruirá, perdiste")
        lista_numeros.clear()
        print(lista_numeros)
    else:
        print("La lista fue salvada, ganaste")
        print(lista_numeros)
        return lista_numeros


lista = [12, 123, 412, 123]

lanzar = lanzar_moneda()
probar_suerte(lanzar, lista)

