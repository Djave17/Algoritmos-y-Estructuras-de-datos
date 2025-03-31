"""3. Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, 
ofreciendo un descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario. 
Además, por la compra de más de 3 docenas se obsequia una unidad del producto por cada 
docena en exceso sobre 3. Diseñe un programa que determine el monto de la compra,
el monto del descuento, el monto a pagar y el número de unidades de obsequio 
por la compra de cierta cantidad de docenas del producto."""
import os

def Calcular_Descuento(precio, cantidad):
    
    docenas = cantidad // 12
    if docenas > 3: 
        
        #obsequio - usar for para restar 1 por cada exceso\
        
        cantidad = cantidad - (docenas - 3)
        obsequio = (docenas - 3)
        subtotal = precio * cantidad
        descuento = subtotal * 0.15
        montoTotal = subtotal - (subtotal * 0.15)
            
   
    else:
        subtotal = precio * cantidad
        descuento = subtotal * 0.10
        obsequio = 0
        montoTotal = subtotal - descuento
        
    print("Subtotal: ", subtotal)
    print("Monto de la compra: ", montoTotal)
    print("Docenas: ", docenas)
    print("Cantidad: ", cantidad)
    print("Monto del descuento: ", descuento)
    print("Número de unidades de obsequio: ", obsequio)
option = 0
while option != 5:
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
            Calcular_Descuento(10, cantidad)
            input()
        case 2:
            os.system("clear")
            print("Manzana")
            Calcular_Descuento(15, cantidad)
            input()
        case 3:
            os.system("clear")
            print("Naranja")
            Calcular_Descuento(8, cantidad)
            input()
        case 4:
            os.system("clear")
            print("Sandia")
            Calcular_Descuento(70, cantidad)
            input()
        case 5:
            os.system("clear")
            print("Melon")
            Calcular_Descuento(50, cantidad)
            input()
        case 6:
            print("Gracias por su compra")
            break
        case _:
            print("Opción no válida")
            input()
            continue
  
            
    
    
