import libreria29numeronarcisista

#Comprobar si un número es narcisista
numeroentrada = input("Introduce un número : ")
if (libreria29numeronarcisista.narcisista(numeroentrada)):
    print("El número es narcisista")
else:
    print("El número no es narcisista")

#Buscar números narcisistas en un rango
rangoinferior = int(input("Introduce el rango inferior : "))
rangosuperior = int(input("Introduce el rango superior : "))
print("Números narcisistas entre", rangoinferior, "y", rangosuperior, " son:")
for numero in range(rangoinferior, rangosuperior + 1):
    if (libreria29numeronarcisista.narcisista(str(numero))):
        print(numero)   





