buscar = int(input('Ingrese un número: '))
cont = 20 
while cont <= 50 :
    if cont == buscar:
        print('Número encontrado')
        break
    cont += 1
else:   
    print('Número no encontrado')
    
#For y la rama else
listado = ["Juan", "Pedro", "María", "Luisa", "Ana"]
buscar = input('Ingrese un nombre: ')
for nombre in listado:
    if nombre == buscar:
        print('Nombre encontrado')
        break
else:
    print('Nombre no encontrado')