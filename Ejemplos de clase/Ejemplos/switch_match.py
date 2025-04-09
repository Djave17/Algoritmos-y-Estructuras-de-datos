
def switch_match(value):
    value = int(input("Ingrese un número: "))
    match value:
        case 1:
            return "Uno"
        case 2:
            return "Dos"
        case 3:
            return "Tres"
        case _:
            return "Valor no reconocido"

print(switch_match(1))  # Uno
