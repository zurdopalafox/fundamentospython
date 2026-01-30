nombres = dict()

for i in range(1, 6):
    nombre = input("Introduce un nombre: ")
    while nombre.upper() in nombres.keys():
        nombre = input("El nombre ya existe, introduce otro nombre: ")
    nombres[nombre.upper()] = nombre

for nombrevalue in nombres.values():
    print("Nombre:", nombrevalue)

print (nombres)
