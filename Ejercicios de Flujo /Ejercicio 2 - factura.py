"""2. Escribir un programa que permita emitir la FACTURA correspondiente,
a una compra de un artículo determinado, del que se adquieren una o varias unidades.
El IVA a aplicar es de 15% y si el Sub Total (precio de venta por cantidad),
es mayor de 1000, se aplicará un descuento del 12%.


"""
import os 

# Ingreso de datos
def Calcular_Precio(precio, cantidad):
    
    subtotal = precio * cantidad
    iva = subtotal * 0.15
    total = subtotal + iva
    if subtotal > 1000:
        descuento = total * 0.12           
        total = total - descuento
    print("Subtotal: ", subtotal)
    print("IVA: ", iva)
    print("Total: ", total)

opcion = 0
while opcion != 6: 
    #Menu de compras
    os.system("clear")
    print("========== Menú de compra ==========")
    print("1. Banano - 10 cordobas")
    print("2. Manzana - 15 cordobas")
    print("3. Naranja - 8 cordobas")
    print("4. Sandia - 70 cordobas")
    print("5. Melon - 50 cordobas")
    print("6. Salir")

    opcion = int(input("Ingrese la opción de compra: "))
    cantidad = int(input("Ingrese la cantidad de productos: "))
    
    match opcion:
        case 1: 
            os.system("clear")
            print("Banano")
            Calcular_Precio(10, cantidad)
            input()
        case 2:
            os.system("clear")
            print("Manzana")
            Calcular_Precio(15, cantidad)
            input()
        case 3:
            os.system("clear")
            print("Naranja")
            Calcular_Precio(8, cantidad)
            input()
        case 4:
            os.system("clear")
            print("Sandia")
            Calcular_Precio(70, cantidad)
            input() 
        case 5:
            os.system("clear")
            print("Melon")
            Calcular_Precio(50, cantidad)
            input()
            
        case 6:
            print("Saliendo del programa...")
            break;
        case _:
            print("Opción no válida")
            
    os.system("pause")
   
     
    
    
    

