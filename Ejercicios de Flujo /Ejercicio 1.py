"""
Desarrolle un programa que calcule el importe a pagar por un vehículo al circular por una autopista. 
El vehiculo puede ser una bicicleta, una moto, un carro o un camion. Para definir el conjunto de vehiculo d
debe utilizar unq estructura adecuada. el importe se calcula segun: 
Bicicleta 100 cordboas
moto y carro 30 cordobas por km 
camiones 30 por cordobas km y 25 cordoba por tonelada.
El programa debe solicitar el tipo de vehiculo y la distancia recorrida en km.
"""
op = 0 
while op != 5:
    
    #Menu de opciones
    print("1. Bicicleta")
    print("2. Moto")    
    print("3. Carro")
    print("4. Camión")
    print("5. Salir")
    
    vehiculo = int(input("Ingrese el tipo de vehículo: "))
    vehiculo = vehiculo

    match vehiculo:
        case 1:
            print("Bicicleta")
            importe = 100
            print("El importe a pagar es de", importe, "cordobas")
        case 2:
            print("Moto")
            distancia = int(input("Ingrese la distancia recorrida en km: "))
            importe = 30 * distancia
            print("El importe a pagar es de", importe, "cordobas")
        case 3:
            print("Carro")
            distancia = int(input("Ingrese la distancia recorrida en km: "))
            importe = 30 * distancia
            print("El importe a pagar es de", importe, "cordobas")
        case 4:
            print("Camión")
            distancia = int(input("Ingrese la distancia recorrida en km: "))
            toneladas = int(input("Ingrese la cantidad de toneladas: "))
            importe = (30 * distancia) + (25 * toneladas)
            print("El importe a pagar es de", importe, "cordobas")
        case 5:
            print("Saliendo del programa...")
            break; 
        case _:
            print("Tipo de vehículo no válido.")
        
   


