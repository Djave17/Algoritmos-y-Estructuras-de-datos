

usuario = input("Usuario: ")
usuario = usuario.lower()
password = input("Contraseña: ")
password = password.lower()

if usuario == "admin" and password == "admin":
    print("Bienvenido administrador")
elif usuario != "admin" and password != "admin":
    print("Usuario incorrecto")
else:
    print("Usuario y contraseña incorrectos")
print("Fin del programa")
