def numeros_persona(*args):
    suma_numeros = 0
    for n in args:
        suma_numeros = sum(args[1:])
    print(f"{args[0]}, la suma de tus números es {suma_numeros}")

numeros_persona('David', 12,12,41,15)